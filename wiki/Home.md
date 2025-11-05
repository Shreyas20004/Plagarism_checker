# Plagiarism Checker

Welcome to the **Free, Offline Plagiarism Checker** wiki! This tool helps you detect plagiarism in PDF and DOCX documents by comparing them against a locally built corpus of reference documents.

## Overview

This plagiarism detection system uses a combination of **TF-IDF** (Term Frequency-Inverse Document Frequency) and **semantic similarity** analysis to identify potential plagiarism in uploaded documents. The tool operates completely offline, ensuring your documents remain private and secure.

## Key Features

- 🔒 **Offline & Private** - All processing happens locally on your machine
- 📄 **Multiple Format Support** - Works with PDF and DOCX files
- 🤖 **Dual Analysis** - Combines TF-IDF and semantic similarity for accurate detection
- 📊 **Detailed Reports** - Generates comprehensive PDF reports with match breakdowns
- 📚 **Customizable Corpus** - Build your own reference corpus from various sources
- 🎨 **User-Friendly Interface** - Simple Streamlit-based web interface

## How It Works

1. **Upload** your document (PDF or DOCX)
2. The system **extracts and preprocesses** the text
3. **Comparison** is performed against your local corpus using:
   - TF-IDF vectorization for statistical similarity
   - Sentence transformers for semantic similarity
4. **Results** show similarity scores for each corpus document
5. **Download** a detailed PDF report of the findings

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Build a corpus (optional but recommended)
python build_corpus.py

# Run the application
streamlit run app.py
```

## Use Cases

- **Academic Institutions** - Check student submissions for plagiarism
- **Content Creators** - Verify originality of written content
- **Researchers** - Compare research papers against existing literature
- **Publishers** - Screen submissions for duplicate content

## Documentation

Explore the following pages to learn more:

- **[Installation](Installation.md)** - Detailed setup instructions
- **[Usage](Usage.md)** - How to use the plagiarism checker
- **[Building Corpus](Building-Corpus.md)** - Create and manage your reference corpus
- **[API Reference](API-Reference.md)** - Technical documentation of modules
- **[Architecture](Architecture.md)** - System design and components
- **[FAQ](FAQ.md)** - Common questions and troubleshooting

## Technology Stack

- **Streamlit** - Web interface
- **scikit-learn** - TF-IDF vectorization
- **sentence-transformers** - Semantic similarity analysis
- **NLTK** - Text preprocessing
- **PyPDF2** - PDF text extraction
- **python-docx** - DOCX text extraction
- **ReportLab** - PDF report generation

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve the tool.

## License

This project is open source and available for educational and research purposes.
