# app_flask.py
import os
from flask import Flask, request, jsonify, send_file
from utils import extractor, preprocessor, similarity, report as report_mod, diff_report, db

app = Flask(__name__)
UPLOAD_DIR = "uploads"
REPORT_DIR = "reports"
HTML_DIFF_DIR = os.path.join(REPORT_DIR, "diffs")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(HTML_DIFF_DIR, exist_ok=True)
db.init_db()

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    if not username:
        return jsonify({"error": "username required"}), 400
    user = db.get_or_create_user(username)
    return jsonify({"user_id": user.id, "username": user.username})

@app.route("/upload", methods=["POST"])
def upload():
    username = request.form.get("username")
    if "file" not in request.files:
        return jsonify({"error":"file missing"}), 400
    file = request.files["file"]
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)
    file.save(file_path)
    # get or create user
    user = db.get_or_create_user(username) if username else None
    # extract text
    text = extractor.extract_text(file_path)
    cleaned = preprocessor.clean_text(text)
    doc_id = db.add_document(filename, cleaned, uploaded_by=(user.id if user else None))
    return jsonify({"doc_id": doc_id, "filename": filename})

@app.route("/check", methods=["POST"])
def check():
    # expects 'doc_id' and 'username'
    doc_id = request.form.get("doc_id", type=int)
    username = request.form.get("username")
    session = db.get_session()
    doc = session.query(db.Document).filter_by(id=doc_id).first()
    session.close()
    if not doc:
        return jsonify({"error":"document not found"}), 404
    submitted_text = doc.text
    results, matches = similarity.compare_with_db_corpus(submitted_text, top_k=10)
    overall = sum([r[1] for r in results]) / len(results) if results else 0.0

    # create diff html for top matches
    matches_for_html = matches[:5]
    diff_html_path = os.path.join(HTML_DIFF_DIR, f"diff_{doc_id}.html")
    if matches_for_html:
        diff_report.make_combined_html_matches(matches_for_html, diff_html_path)
    else:
        diff_html_path = None

    # create pdf report
    report_path = os.path.join(REPORT_DIR, f"report_{doc_id}.pdf")
    report_mod.generate_report(report_path, results, overall, diff_html_path)
    user = db.get_or_create_user(username) if username else None
    db.save_report(user.id if user else None, doc_id, report_path, diff_html_path, overall)

    return jsonify({
        "overall_score": overall,
        "top_matches": [{"filename": r[0], "score": r[1], "doc_id": r[2]} for r in results],
        "report_path": report_path,
        "diff_html": diff_html_path
    })

@app.route("/reports/<int:user_id>", methods=["GET"])
def list_reports(user_id):
    rep = db.list_reports_for_user(user_id)
    return jsonify(rep)

@app.route("/download_report", methods=["GET"])
def download_report():
    path = request.args.get("path")
    if not path or not os.path.exists(path):
        return jsonify({"error":"file not found"}), 404
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
