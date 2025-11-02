# Setup Checklist

Use this checklist to ensure everything is properly installed and configured.

## ✅ Pre-Installation

- [ ] Python 3.8+ installed (check with `python --version`)
- [ ] Git installed (optional, for cloning repo)
- [ ] Internet connection available (for downloading dependencies)
- [ ] Administrator access (may be needed for Windows)

## ✅ Installation

- [ ] Project cloned or downloaded
- [ ] Virtual environment created (`python -m venv venv`)
- [ ] Virtual environment activated
- [ ] pip upgraded (`python -m pip install --upgrade pip`)
- [ ] Dependencies installed (`pip install -r requirements.txt`)

## ✅ Verification

- [ ] Python version verified (`python --version`)
- [ ] Virtual environment shows `(venv)` in prompt
- [ ] No import errors (`python -c "import streamlit; import flask"`)
- [ ] All utilities importable:
  ```bash
  python -c "from utils import extractor, preprocessor, similarity, db, report, diff_report; print('OK')"
  ```

## ✅ Directory Structure

- [ ] `corpus/` folder exists
- [ ] `uploads/` folder exists
- [ ] `reports/` folder exists
- [ ] `utils/` folder contains:
  - [ ] `__init__.py`
  - [ ] `extractor.py`
  - [ ] `preprocessor.py`
  - [ ] `similarity.py`
  - [ ] `report.py`
  - [ ] `diff_report.py` (new)
  - [ ] `db.py` (new)

## ✅ Files Present

- [ ] `app_streamlit.py` (multi-user dashboard)
- [ ] `app_flask.py` (REST API)
- [ ] `app.py` (basic app)
- [ ] `requirements.txt` (dependencies)
- [ ] `README.md` (documentation)
- [ ] `CONTRIBUTING.md` (contribution guide)
- [ ] `INSTALLATION.md` (setup guide)
- [ ] `QUICKSTART.md` (quick start)
- [ ] `.gitignore` (git configuration)

## ✅ First Run

### Streamlit Dashboard

```bash
streamlit run app_streamlit.py
```

- [ ] No errors on startup
- [ ] Browser opens to `http://localhost:8501`
- [ ] Can type username and login
- [ ] Can upload files
- [ ] Can run checks (if corpus documents exist)

### Flask API

```bash
python app_flask.py
```

- [ ] Server starts on port 5001
- [ ] Can access `http://localhost:5001/register`
- [ ] API responses are valid JSON
- [ ] No import or connection errors

## ✅ Database

- [ ] `plagiarism.db` created in project root after first run
- [ ] Database contains tables: `users`, `documents`, `reports`
- [ ] Can create users via API or Streamlit
- [ ] Can store documents in database

## ✅ Functionality

- [ ] Upload PDF documents ✓
- [ ] Upload DOCX documents ✓
- [ ] Extract text successfully ✓
- [ ] Clean/preprocess text ✓
- [ ] Calculate similarity scores ✓
- [ ] Generate PDF reports ✓
- [ ] Generate HTML diffs ✓
- [ ] Store results in database ✓
- [ ] Retrieve user history ✓

## ✅ Optional: Advanced Setup

- [ ] Created `.streamlit/config.toml` (optional)
- [ ] Configured similarity thresholds (optional)
- [ ] Set up custom port configuration (optional)
- [ ] Added reference documents to `corpus/` folder
- [ ] Tested GPU acceleration (optional)

## ✅ Documentation

- [ ] Read README.md ✓
- [ ] Reviewed CONTRIBUTING.md ✓
- [ ] Checked INSTALLATION.md ✓
- [ ] Skimmed QUICKSTART.md ✓
- [ ] Understood project structure ✓

## ✅ Ready to Use

- [ ] All checks pass ✓
- [ ] Ready to run production use ✓
- [ ] Ready to contribute code ✓
- [ ] Ready to deploy ✓

## 🔧 Troubleshooting Checklist

If something doesn't work:

- [ ] Verify Python version is 3.8+
- [ ] Check virtual environment is activated
- [ ] Ensure all dependencies installed: `pip list`
- [ ] Try reinstalling requirements: `pip install -r requirements.txt --force-reinstall`
- [ ] Check file permissions
- [ ] Review error messages carefully
- [ ] Check README.md troubleshooting section
- [ ] Check INSTALLATION.md troubleshooting section
- [ ] Consult CONTRIBUTING.md for reporting issues
- [ ] Open GitHub issue with full error message

---

**All checks complete? You're ready to go! 🚀**
