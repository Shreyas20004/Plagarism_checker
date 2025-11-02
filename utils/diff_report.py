# utils/diff_report.py
import difflib
import os
from html import escape

def make_side_by_side_html(text_a, text_b, filename):
    """
    Create HTML file with side-by-side diff of text_a and text_b using HtmlDiff.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # Split into lines (we want sentence-level diffs -> we can split by sentences if needed)
    # For nicer results split by sentences using simple '.' split (you can replace with nltk.sent_tokenize)
    a_lines = [l.strip() for l in text_a.split('.') if l.strip()]
    b_lines = [l.strip() for l in text_b.split('.') if l.strip()]
    d = difflib.HtmlDiff(tabsize=4, wrapcolumn=80)
    html = d.make_file(a_lines, b_lines, fromdesc="Submitted", todesc="Reference")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    return filename

def make_combined_html_matches(matches, out_html):
    """
    matches: list of tuples (submitted_text_chunk, reference_text_chunk, filename)
    produce a single HTML with each side-by-side diff stacked.
    """
    os.makedirs(os.path.dirname(out_html), exist_ok=True)
    html_parts = ["<html><head><meta charset='utf-8'><title>Matches</title></head><body>"]
    for i, (a, b, source_fn) in enumerate(matches):
        html_parts.append(f"<h3>Match vs {escape(source_fn)}</h3>")
        a_lines = [l.strip() for l in a.split('.') if l.strip()]
        b_lines = [l.strip() for l in b.split('.') if l.strip()]
        d = difflib.HtmlDiff(tabsize=4, wrapcolumn=80)
        html_parts.append(d.make_table(a_lines, b_lines, fromdesc="Submitted", todesc=escape(source_fn)))
        html_parts.append("<hr/>")
    html_parts.append("</body></html>")
    with open(out_html, "w", encoding="utf-8") as f:
        f.write("\n".join(html_parts))
    return out_html
