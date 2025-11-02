# 🚀 Quick Start Guide

Get up and running in 5 minutes!

## Installation (One-time)

### Windows
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**⏱️ Takes 10-15 minutes on first run** (downloads AI model)

---

## Running the App

### Option 1: Streamlit Dashboard (Recommended)

```bash
streamlit run app_streamlit.py
```

Opens in browser at **`http://localhost:8501`**

**Features:**
- ✅ Login with username
- ✅ Upload documents
- ✅ Run plagiarism checks
- ✅ View results & download reports

---

### Option 2: Flask REST API

```bash
python app_flask.py
```

API runs at **`http://localhost:5001`**

**Example:**
```bash
# Register user
curl -X POST -F "username=alice" http://127.0.0.1:5001/register

# Upload document
curl -X POST -F "username=alice" -F "file=@document.pdf" \
  http://127.0.0.1:5001/upload

# Check for plagiarism
curl -X POST -F "username=alice" -F "doc_id=1" \
  http://127.0.0.1:5001/check
```

---

## What to Do First

### 1. Add Reference Documents

Place reference PDFs/DOCX files in the `corpus/` folder:

```bash
mkdir corpus
cp my_reference_document.pdf corpus/
```

### 2. Upload a Document

In Streamlit:
1. Enter your username
2. Click "Upload document"
3. Select a PDF or DOCX file

### 3. Run a Check

1. Select your document from "Your documents"
2. Click "Run Check"
3. View results!

### 4. Download Report

- **PDF Report**: Professional summary
- **HTML Diff**: Side-by-side comparison

---

## Common Commands

| Task | Command |
|------|---------|
| Activate environment | `source venv/bin/activate` (macOS/Linux) or `.\venv\Scripts\Activate.ps1` (Windows) |
| Run Streamlit | `streamlit run app_streamlit.py` |
| Run Flask API | `python app_flask.py` |
| Run basic app | `streamlit run app.py` |
| Deactivate environment | `deactivate` |
| Reset database | `rm plagiarism.db` (macOS/Linux) or `del plagiarism.db` (Windows) |

---

## Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt
```

### "Port already in use"
```bash
streamlit run app_streamlit.py --server.port 8502
```

### Slow on first run
First run downloads the AI model (~500MB). Be patient! ⏳

### More help?
See **INSTALLATION.md** or **README.md**

---

## Features Overview

🔍 **Similarity Detection**
- TF-IDF algorithm
- Semantic similarity (AI-powered)

📊 **Reporting**
- PDF reports with match breakdown
- HTML diffs showing exact matches

🗄️ **Database**
- Stores users, documents, reports
- SQLite (automatic, local storage)

👥 **Multi-user**
- Each user has their own workspace
- Access history and old reports

🔌 **API Access**
- REST endpoints for integration
- Perfect for automation

---

## Next Steps

1. **Read README.md** for full documentation
2. **Check CONTRIBUTING.md** to help improve the project
3. **Explore the code** in the `utils/` folder
4. **Customize settings** in configuration files

---

**Enjoy detecting plagiarism! 🎉**
