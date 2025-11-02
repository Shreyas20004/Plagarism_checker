from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_report(filename, scores, overall_score):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Plagiarism Report")
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Overall Similarity: {overall_score:.2f}%")
    c.drawString(100, 700, "Comparison Details:")
    y = 680
    for file, score in scores:
        c.drawString(120, y, f"{file}: {score:.2f}%")
        y -= 20
        if y < 100:
            c.showPage()
            y = 750
    c.save()
