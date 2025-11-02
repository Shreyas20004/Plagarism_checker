# 🧾 Plagiarism Checker — Free, Offline, Multi-user

A comprehensive, open-source plagiarism detection tool featuring multi-user support, SQLite database integration, REST API access, and detailed similarity reports with side-by-side HTML diffs.

## ✨ Features

- **Hybrid Similarity Detection**: Combines TF-IDF and semantic similarity (transformer-based embeddings)
- **Multi-user Dashboard**: Streamlit-based web interface with user authentication and report history
- **REST API**: Flask-based API for programmatic access and integration
- **SQLite Database**: Persistent storage for users, documents, and reports
- **HTML Diff Reports**: Side-by-side highlighting of matched sentences
- **PDF Reports**: Professional PDF reports with detailed comparison breakdowns
- **Local & Offline**: No external APIs or cloud dependencies—everything runs locally
- **Modular Architecture**: Clean separation of concerns (extraction, preprocessing, comparison, reporting)

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Streamlit Dashboard](#streamlit-dashboard)
  - [Flask REST API](#flask-rest-api)
  - [Direct Python Usage](#direct-python-usage)
- [API Documentation](#api-documentation)
- [Configuration & Tuning](#configuration--tuning)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## 🚀 Installation

### Prerequisites

- **Python 3.8+** (recommended: 3.9 or 3.10)
- **pip** (Python package manager)
- **Virtual environment** (recommended)

### Step 1: Clone or Download

```bash
git clone https://github.com/your-username/plagiarism-checker.git
cd plagiarism-checker
```

### Step 2: Create Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `streamlit` — Web UI framework
- `Flask` — REST API framework
- `PyPDF2`, `python-docx` — Document extraction
- `nltk` — Natural language processing
- `scikit-learn` — TF-IDF vectorization
- `sentence-transformers` — Semantic embeddings
- `reportlab` — PDF generation
- `sqlalchemy` — Database ORM
- `pandas` — Data manipulation

### Step 4: First-Time Setup

The first time you run the application, dependencies (like the sentence-transformer model) will be downloaded automatically. This may take 5-10 minutes on first run.

```bash
python app_streamlit.py  # or python app_flask.py
```

---

## 📁 Project Structure

```
plagiarism_checker/
│
├── app_streamlit.py        # Multi-user Streamlit dashboard
├── app_flask.py            # Flask REST API server
├── app.py                  # Legacy Streamlit interface (basic version)
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── utils/
│   ├── __init__.py
│   ├── extractor.py       # PDF/DOCX text extraction
│   ├── preprocessor.py    # Text cleaning & tokenization
│   ├── similarity.py      # TF-IDF and semantic similarity
│   ├── report.py          # PDF report generation
│   ├── diff_report.py     # HTML diff generation (NEW)
│   └── db.py              # SQLite database models & helpers (NEW)
│
├── corpus/                # Reference documents (*.txt files)
│   ├── arxiv_cs_AI_0.txt
│   ├── arxiv_cs_AI_1.txt
│   └── ...
│
├── uploads/               # User-uploaded documents (temp storage)
├── reports/               # Generated PDF reports
│   └── diffs/            # HTML diff files
│
└── plagiarism.db         # SQLite database (created on first run)
```

---

## 🎯 Quick Start

### 1. Start the Streamlit Dashboard (Recommended)

```bash
streamlit run app_streamlit.py
```

Then open your browser to **`http://localhost:8501`**

**Features:**
- Login with username (no password required for demo)
- Upload PDF or DOCX files
- Run plagiarism checks against the corpus
- View results with side-by-side HTML diffs
- Download PDF reports
- View report history

### 2. Start the Flask REST API (Optional)

```bash
python app_flask.py
```

The API will be available at **`http://localhost:5001`**

See [API Documentation](#api-documentation) for endpoint details.

### 3. Using the Basic App (Legacy)

```bash
streamlit run app.py
```

This is the original simpler interface (corpus-folder based).

---

## 💻 Usage

### Streamlit Dashboard

#### Login
1. Type your username in the text input
2. Click Enter (no password required for demo purposes)

#### Upload a Document
1. Click **"Upload document (pdf/docx)"**
2. Select a file from your computer
3. The file will be extracted, cleaned, and stored in the database

#### Run a Check
1. Under **"Your documents"**, select a document
2. Click **"Run Check"**
3. Wait for the system to compare against all corpus documents
4. View the **"Overall Similarity"** percentage
5. See the **"Top matches"** list

#### View Results
- **PDF Report**: Download a detailed PDF with all comparisons
- **HTML Diff**: View side-by-side HTML showing matched sentences highlighted
- **Report History**: Access previous reports from your dashboard

### Flask REST API

#### 1. Register a User

```bash
curl -X POST -F "username=alice" http://127.0.0.1:5001/register
```

**Response:**
```json
{
  "user_id": 1,
  "username": "alice"
}
```

#### 2. Upload a Document

```bash
curl -X POST \
  -F "username=alice" \
  -F "file=@/path/to/document.pdf" \
  http://127.0.0.1:5001/upload
```

**Response:**
```json
{
  "doc_id": 1,
  "filename": "document.pdf"
}
```

#### 3. Check Document for Plagiarism

```bash
curl -X POST \
  -F "username=alice" \
  -F "doc_id=1" \
  http://127.0.0.1:5001/check
```

**Response:**
```json
{
  "overall_score": 34.56,
  "top_matches": [
    {
      "filename": "arxiv_cs_AI_42.txt",
      "score": 67.89,
      "doc_id": 42
    }
  ],
  "report_path": "reports/report_1.pdf",
  "diff_html": "reports/diffs/diff_1.html"
}
```

#### 4. List User Reports

```bash
curl http://127.0.0.1:5001/reports/1
```

**Response:**
```json
[
  {
    "id": 1,
    "overall_score": 34.56,
    "created_at": "2025-11-02T10:30:45.123456",
    "report_path": "reports/report_1.pdf",
    "diff_path": "reports/diffs/diff_1.html"
  }
]
```

#### 5. Download a Report

```bash
curl -o report.pdf "http://127.0.0.1:5001/download_report?path=reports/report_1.pdf"
```

### Direct Python Usage

```python
from utils import extractor, preprocessor, similarity, report, db

# Initialize database
db.init_db()

# Extract text from a document
text = extractor.extract_text("document.pdf")
cleaned = preprocessor.clean_text(text)

# Add to corpus
doc_id = db.add_document("document.pdf", cleaned)

# Compare against corpus (from file system)
results = similarity.compare_with_corpus(cleaned, "corpus")
print(f"Overall similarity: {sum([s for _, s in results]) / len(results) if results else 0:.2f}%")

# Or compare against database documents
results, matches = similarity.compare_with_db_corpus(cleaned, top_k=5)

# Generate report
report.generate_report("report.pdf", results, 45.2, "report.html")
```

---

## 📚 API Documentation

### Endpoints

#### POST `/register`
Register a new user (or retrieve existing user)

**Parameters:**
- `username` (form data, required): Username string

**Returns:**
```json
{
  "user_id": <int>,
  "username": <string>
}
```

---

#### POST `/upload`
Upload a document

**Parameters:**
- `username` (form data): Username (optional)
- `file` (file upload, required): PDF or DOCX file

**Returns:**
```json
{
  "doc_id": <int>,
  "filename": <string>
}
```

---

#### POST `/check`
Run plagiarism check on an uploaded document

**Parameters:**
- `username` (form data): Username (optional)
- `doc_id` (form data, required): Document ID from upload

**Returns:**
```json
{
  "overall_score": <float>,
  "top_matches": [
    {
      "filename": <string>,
      "score": <float>,
      "doc_id": <int>
    }
  ],
  "report_path": <string>,
  "diff_html": <string or null>
}
```

---

#### GET `/reports/<user_id>`
Retrieve all reports for a user

**Parameters:**
- `user_id` (URL path, required): User ID

**Returns:**
```json
[
  {
    "id": <int>,
    "report_path": <string>,
    "diff_path": <string or null>,
    "overall_score": <float>,
    "created_at": <ISO 8601 timestamp>
  }
]
```

---

#### GET `/download_report`
Download a report file

**Parameters:**
- `path` (query, required): Path to report file

**Returns:** Binary file (PDF or HTML)

---

## ⚙️ Configuration & Tuning

### Similarity Thresholds

Edit `utils/similarity.py` to adjust detection sensitivity:

```python
if s_score > 50.0:  # Lower = more sensitive (catches minor matches)
    # ...
    if best_score > 40:  # Lower = more lenient
        matches.append((chunk, best, d["filename"]))
```

**Recommended ranges:**
- **Conservative** (fewer false positives): `50` and `45`
- **Balanced** (default): `50` and `40`
- **Aggressive** (catches more matches): `40` and `30`

### Chunk Size

Adjust text chunking for granularity:

```python
def chunk_text(text, chunk_size=200):  # Words per chunk
    # ...
```

- **Smaller chunks** (e.g., 100): Finds smaller plagiarized sections
- **Larger chunks** (e.g., 300): Finds substantial matches only

### Model Selection

The app uses the `all-MiniLM-L6-v2` sentence transformer by default. For more accuracy or different languages:

```python
# In utils/similarity.py
model = SentenceTransformer('all-mpnet-base-v2')  # Slower, more accurate
```

Available models: https://www.sbert.net/models.html

### Database

The SQLite database file is created as `plagiarism.db` in the project root. To reset:

```bash
rm plagiarism.db  # or delete plagiarism.db on Windows
python app_streamlit.py  # Will recreate on next run
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### Report Issues

Found a bug? Open an issue on GitHub with:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment (OS, Python version)

### Submit Changes

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature/my-feature`
3. **Make changes** and test thoroughly
4. **Commit**: `git commit -m "Add feature: description"`
5. **Push**: `git push origin feature/my-feature`
6. **Create a Pull Request** with a clear description

### Development Setup

```bash
git clone https://github.com/your-username/plagiarism-checker.git
cd plagiarism-checker
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt

# Make changes, then test
python app_streamlit.py
```

### Coding Standards

- **PEP 8**: Follow Python style guidelines
- **Docstrings**: Document functions with clear descriptions
- **Type hints**: Use type annotations where possible
- **Error handling**: Gracefully handle edge cases

### Ideas for Contribution

- [ ] Add support for more file formats (RTF, ODT, etc.)
- [ ] Implement embedding caching for faster repeated checks
- [ ] Add OAuth2 authentication
- [ ] Create Docker containerization
- [ ] Add web search integration (requires API keys)
- [ ] Improve UI/UX in Streamlit
- [ ] Add admin dashboard for corpus management
- [ ] Support for non-English languages
- [ ] Performance optimizations for large corpora

---

## 🐛 Troubleshooting

### "No module named 'streamlit'"

**Solution:**
```bash
pip install -r requirements.txt
```

Ensure you're in the virtual environment (check prompt starts with `(venv)`).

### "Model download failed" or "Connection timeout"

The sentence-transformer model downloads on first run. This requires internet.

**Solutions:**
1. Check internet connection
2. Increase timeout: Wait 10-15 minutes on first run
3. Manually download model:
   ```python
   from sentence_transformers import SentenceTransformer
   model = SentenceTransformer('all-MiniLM-L6-v2')
   ```

### "Port 8501 already in use" (Streamlit)

**Solution:**
```bash
streamlit run app_streamlit.py --server.port 8502
```

### "Port 5001 already in use" (Flask)

**Solution:** Edit `app_flask.py`:
```python
if __name__ == "__main__":
    app.run(debug=True, port=5002)  # Change port
```

### Database locked errors

**Solution:** Close other instances of the app, then restart.

### PDF report not generating

**Solution:** Check `reports/` folder has write permissions:
```bash
chmod 755 reports/  # On macOS/Linux
```

### Slow similarity checking

**Solutions:**
1. Reduce top_k matches: `similarity.compare_with_db_corpus(text, top_k=3)`
2. Increase chunk_size: `chunk_text(text, chunk_size=300)`
3. Use a simpler model: Switch to `distiluse-base-multilingual-cased-v2`

---

## 📝 Performance Notes

### Memory Usage

- **Corpus size**: Can handle 100+ documents without issues
- **Embedding model**: ~500MB on disk, ~1GB RAM during execution
- **Database**: Negligible; grows ~10KB per document

### Speed Benchmarks (on typical machine)

| Task | Time |
|------|------|
| Extract text from PDF | 0.5–2 seconds |
| Clean text | 0.1 seconds |
| Compare vs 50 documents | 5–30 seconds |
| Generate PDF report | 0.5 seconds |
| Generate HTML diff | 0.2 seconds |

### Optimization Tips

1. **Cache embeddings** in DB (future enhancement)
2. **Batch processing** for multiple uploads
3. **Reduce embedding dimensions** using PCA
4. **Use lighter model** (`distiluse-base-multilingual-cased-v2`)

---

## 🔒 Security & Privacy Notes

⚠️ **This is a demo application. For production use:**

1. **Authentication**: Implement OAuth2 or proper password hashing (currently username-only)
2. **File uploads**: Add file size limits and type validation
3. **Database**: Use PostgreSQL instead of SQLite for multi-concurrent access
4. **Encryption**: Add TLS/SSL for Flask API
5. **Audit logging**: Log all checks and accesses
6. **Data retention**: Implement automatic document/report deletion policies

### Privacy

- **Local storage**: All data stored locally; no cloud sync
- **No external APIs**: No data sent to third parties
- **User isolation**: Each user sees only their own documents and reports

---

## 📄 License

This project is licensed under the **MIT License** — see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Sentence Transformers**: Semantic similarity embeddings
- **Scikit-learn**: TF-IDF vectorization
- **ReportLab**: PDF generation
- **SQLAlchemy**: Database ORM
- **Streamlit**: Web UI framework
- **Flask**: REST API framework

---

## 📧 Support

For questions or issues:

1. **Check the FAQ** above
2. **Search existing issues** on GitHub
3. **Open a new issue** with detailed description
4. **Contact**: Email or open a discussion thread

---

## 🚀 Future Roadmap

- [ ] Web search integration for online plagiarism detection
- [ ] Advanced analytics dashboard
- [ ] Batch processing API
- [ ] Mobile app (React Native)
- [ ] Deployment templates (Docker, Heroku, AWS)
- [ ] Internationalization (multi-language support)
- [ ] Real-time collaboration features
- [ ] Machine learning model improvements
- [ ] Citation detection
- [ ] Paraphrase detection

---

## 📚 Resources

- **Sentence Transformers Docs**: https://www.sbert.net/
- **Scikit-learn Documentation**: https://scikit-learn.org/
- **Streamlit Docs**: https://docs.streamlit.io/
- **Flask Docs**: https://flask.palletsprojects.com/
- **SQLAlchemy Docs**: https://docs.sqlalchemy.org/

---

**Happy detecting! 🔍**

---

*Last updated: November 2, 2025*
