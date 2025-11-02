from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_report(filename, scores, overall_score, diff_html_path=None, extra_notes=None):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Plagiarism Report")
    c.setFont("Helvetica", 11)
    c.drawString(100, 720, f"Overall Similarity: {overall_score:.2f}%")
    c.drawString(100, 700, "Comparison Details (top matches):")
    y = 680
    for file, score, doc_id in scores:
        c.drawString(120, y, f"{file}: {score:.2f}%")
        y -= 18
        if y < 110:
            c.showPage()
            y = 750
    if diff_html_path:
        c.drawString(100, y, f"Detailed difference HTML file: {diff_html_path}")
        y -= 18
    if extra_notes:
        c.drawString(100, y, "Notes:")
        y -= 18
        for line in extra_notes.splitlines():
            c.drawString(120, y, line)
            y -= 14
            if y < 110:
                c.showPage()
                y = 750
    c.save()
