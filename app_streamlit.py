# app_streamlit.py
import streamlit as st
import os
from utils import extractor, preprocessor, similarity, report as report_mod, diff_report, db

st.set_page_config(page_title="Plagiarism Checker (Multi-user)", layout="centered")
db.init_db()
st.title("🧾 Plagiarism Checker — Multi-user Dashboard")

# Simple username login (no password)
username = st.text_input("Enter your username")
if not username:
    st.info("Type a username to continue (this is a simple auth for demo).")
    st.stop()

user = db.get_or_create_user(username)
st.success(f"Logged in as {user.username}")

# Upload file
uploaded = st.file_uploader("Upload document (pdf/docx)", type=["pdf", "docx"])
if uploaded:
    save_path = os.path.join("uploads", uploaded.name)
    with open(save_path, "wb") as f:
        f.write(uploaded.read())
    raw_text = extractor.extract_text(save_path)
    cleaned = preprocessor.clean_text(raw_text)
    doc_id = db.add_document(uploaded.name, cleaned, uploaded_by=user.id)
    st.success(f"Uploaded and stored as doc_id: {doc_id}")

# Run check on any uploaded doc by user
st.write("### Your documents")
docs = db.list_documents_for_user(user.id)
if docs:
    doc_choice = st.selectbox("Select document to check", options=[(d["id"], d["filename"]) for d in docs], format_func=lambda x: x[1])
    if st.button("Run Check"):
        selected_id = doc_choice[0]
        session = db.get_session()
        doc = session.query(db.Document).filter_by(id=selected_id).first()
        session.close()
        results, matches = similarity.compare_with_db_corpus(doc.text, top_k=10)
        overall = sum([r[1] for r in results]) / len(results) if results else 0.0
        st.metric("Overall Similarity", f"{overall:.2f}%")
        st.write("Top matches:")
        for f, s, did in results:
            st.write(f"- {f} → {s:.2f}%")
        # Make diffs + report
        diff_html_path = None
        if matches:
            diff_html_path = os.path.join("reports", "diffs", f"diff_{selected_id}.html")
            diff_report.make_combined_html_matches(matches[:5], diff_html_path)
            st.markdown(f"[Open detailed diff]({diff_html_path})")
        report_pdf_path = os.path.join("reports", f"report_{selected_id}.pdf")
        report_mod.generate_report(report_pdf_path, results, overall, diff_html_path)
        db.save_report(user.id, selected_id, report_pdf_path, diff_html_path, overall)
        with open(report_pdf_path, "rb") as f:
            st.download_button("Download PDF report", f, file_name=f"report_{selected_id}.pdf")
else:
    st.info("You have no uploaded documents yet.")

# Show report history
st.write("### Your report history")
reports = db.list_reports_for_user(user.id)
if reports:
    for r in reports:
        st.write(f"- {r['created_at']} — score: {r['overall_score']:.2f} — [PDF]({r['report_path']}) — [Diff]({r['diff_path']})")
else:
    st.write("No reports yet.")
