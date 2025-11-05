# Installation Guide

This guide will walk you through setting up the Plagiarism Checker on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7+** (Python 3.8 or higher recommended)
- **pip** (Python package installer)
- **Git** (for cloning the repository)

## Step 1: Clone the Repository

```bash
git clone https://github.com/Shreyas20004/Plagarism_checker.git
cd Plagarism_checker
```

## Step 2: Create a Virtual Environment (Recommended)

Creating a virtual environment helps keep dependencies isolated:

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3: Install Dependencies

Install all required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Key Dependencies

The `requirements.txt` includes:

- **streamlit** - Web application framework
- **scikit-learn** - Machine learning library for TF-IDF
- **sentence-transformers** - For semantic similarity analysis
- **nltk** - Natural language processing toolkit
- **PyPDF2** - PDF text extraction
- **python-docx** - DOCX file handling
- **reportlab** - PDF report generation
- **beautifulsoup4** - HTML parsing (for corpus building)
- **wikipedia-api** - Wikipedia content retrieval
- **feedparser** - RSS/Atom feed parsing (for arXiv)
- **tqdm** - Progress bars

## Step 4: Download NLTK Data

The application uses NLTK for text preprocessing. Download the required data:

```python
python -c "import nltk; nltk.download('stopwords')"
```

This is also done automatically when you first run the application.

## Step 5: Download Sentence Transformer Model

On first run, the application will automatically download the `all-MiniLM-L6-v2` model (~80MB). This might take a few minutes depending on your internet speed.

## Step 6: Create Required Directories

The application will create these directories automatically, but you can create them manually:

```bash
mkdir corpus
mkdir uploads
mkdir reports
```

## Step 7: Verify Installation

Test that everything is installed correctly:

```bash
python -c "import streamlit, sklearn, sentence_transformers, nltk, PyPDF2, docx, reportlab; print('All dependencies installed successfully!')"
```

## Troubleshooting

### Common Issues

#### Issue: `ModuleNotFoundError`
**Solution:** Make sure you've activated your virtual environment and installed all requirements:
```bash
pip install -r requirements.txt
```

#### Issue: SSL Certificate Error during model download
**Solution:** If you're behind a corporate firewall, you may need to set up proxy settings or download the model manually.

#### Issue: Permission errors on Windows
**Solution:** Run your terminal as Administrator or check folder permissions.

#### Issue: `nltk` stopwords not found
**Solution:** Manually download NLTK data:
```python
import nltk
nltk.download('stopwords')
```

#### Issue: Out of memory errors
**Solution:** The sentence transformer model requires some RAM. Close other applications or consider using a machine with more memory.

## Next Steps

Once installation is complete:

1. **[Build a Corpus](Building-Corpus.md)** - Create your reference document collection
2. **[Run the Application](Usage.md)** - Start using the plagiarism checker

## System Requirements

### Minimum Requirements
- **RAM:** 4 GB
- **Storage:** 500 MB (plus space for corpus documents)
- **CPU:** Any modern processor

### Recommended Requirements
- **RAM:** 8 GB or more
- **Storage:** 2 GB or more (for larger corpora)
- **CPU:** Multi-core processor for faster processing

## Updating the Application

To update to the latest version:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```
