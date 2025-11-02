import streamlit as st
import os
from utils.extractor import extract_text
from utils.preprocessor import clean_text
from utils.similarity import compare_with_corpus
from utils.report import generate_report

st.set_page_config(page_title="Free Plagiarism Checker", page_icon="🧾", layout="centered")
st.title("🧾 Free, Offline Plagiarism Checker")

uploaded = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])

if uploaded:
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", uploaded.name)
    with open(file_path, "wb") as f:
        f.write(uploaded.read())
    
    st.info("Extracting and processing text...")
    text = extract_text(file_path)
    cleaned_text = clean_text(text)

    st.success("Text extracted successfully!")

    if st.button("Run Plagiarism Check"):
        st.info("Comparing against local corpus...")
        os.makedirs("corpus", exist_ok=True)
        
        results = compare_with_corpus(cleaned_text, "corpus")
        if results:
            overall = sum([s for _, s in results]) / len(results)
            st.metric("Overall Similarity", f"{overall:.2f}%")
            st.write("### Match Breakdown")
            for file, score in results:
                st.write(f"- **{file}** → {score:.2f}%")
            
            report_path = f"reports/{uploaded.name}_report.pdf"
            generate_report(report_path, results, overall)
            with open(report_path, "rb") as pdf:
                st.download_button("📄 Download Report", pdf, file_name="Plagiarism_Report.pdf")
        else:
            st.warning("No corpus documents found. Add reference files to the 'corpus' folder.")
