# Installation & Setup Guide

Detailed step-by-step instructions for installing and configuring the Plagiarism Checker.

## Table of Contents

- [System Requirements](#system-requirements)
- [Installation Methods](#installation-methods)
  - [Method 1: Automated Setup (Windows)](#method-1-automated-setup-windows)
  - [Method 2: Manual Setup](#method-2-manual-setup)
  - [Method 3: Docker (Optional)](#method-3-docker-optional)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Post-Installation Configuration](#post-installation-configuration)

---

## System Requirements

### Minimum

- **OS**: Windows 10+, macOS 10.14+, Ubuntu 18.04+ (or other Linux)
- **Python**: 3.8 or higher (3.10+ recommended)
- **RAM**: 2GB (4GB+ recommended for large corpora)
- **Disk Space**: 2GB (1GB for dependencies + 1GB for database/reports)
- **Internet**: Required for first-time model download (~500MB)

### Recommended

- **OS**: Windows 11, macOS 12+, Ubuntu 22.04+
- **Python**: 3.10 or 3.11
- **RAM**: 8GB
- **Disk Space**: 5GB+
- **GPU**: Optional but speeds up similarity checking (NVIDIA/CUDA)

---

## Installation Methods

### Method 1: Automated Setup (Windows)

For Windows users, we provide a setup script.

**Step 1: Download Setup Script**

Download `setup_windows.bat` from the project (or create it):

```batch
@echo off
REM Plagiarism Checker Setup for Windows

echo ========================================
echo Plagiarism Checker Setup
echo ========================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found in PATH
    echo Please install Python 3.8+ from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo Next steps:
echo 1. Run: venv\Scripts\activate.bat
echo 2. Run: streamlit run app_streamlit.py
echo.
pause
```

**Step 2: Run Setup**

```bash
setup_windows.bat
```

**Step 3: Activate Environment & Run**

```powershell
.\venv\Scripts\Activate.ps1
streamlit run app_streamlit.py
```

---

### Method 2: Manual Setup

Follow these steps for any operating system.

#### Step 1: Verify Python Installation

```bash
python --version
```

Should show **Python 3.8+**. If not installed, download from https://www.python.org

#### Step 2: Clone Repository

```bash
git clone https://github.com/your-username/plagiarism-checker.git
cd plagiarism-checker
```

Or download ZIP and extract.

#### Step 3: Create Virtual Environment

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**You should see `(venv)` in your terminal prompt**

#### Step 4: Upgrade pip

```bash
python -m pip install --upgrade pip
```

#### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

**Installation should take 5-15 minutes depending on internet speed.**

#### Step 6: Verify Installation

```bash
python -c "import streamlit; import flask; import torch; print('✓ All dependencies installed')"
```

---

### Method 3: Docker (Optional)

For containerized deployment.

**Create Dockerfile** in project root:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Expose ports
EXPOSE 8501 5001

# Default command
CMD ["streamlit", "run", "app_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Build Docker image:**

```bash
docker build -t plagiarism-checker .
```

**Run container:**

```bash
docker run -p 8501:8501 -p 5001:5001 plagiarism-checker
```

Access at `http://localhost:8501`

---

## Verification

### Quick Test

Run this Python script to verify all components:

```python
# verify_installation.py
import sys

def verify():
    checks = []
    
    # Check Python version
    py_version = sys.version_info
    py_ok = py_version.major >= 3 and py_version.minor >= 8
    checks.append(("Python 3.8+", py_ok, f"Python {py_version.major}.{py_version.minor}"))
    
    # Check imports
    modules = [
        ("streamlit", "Web UI"),
        ("flask", "REST API"),
        ("PyPDF2", "PDF extraction"),
        ("docx", "DOCX extraction"),
        ("nltk", "NLP processing"),
        ("sklearn", "TF-IDF similarity"),
        ("sentence_transformers", "Semantic similarity"),
        ("reportlab", "PDF generation"),
        ("sqlalchemy", "Database ORM"),
        ("pandas", "Data handling"),
    ]
    
    for module, desc in modules:
        try:
            __import__(module)
            checks.append((desc, True, "✓"))
        except ImportError:
            checks.append((desc, False, "✗"))
    
    # Print results
    print("\n" + "="*50)
    print("Installation Verification")
    print("="*50 + "\n")
    
    all_ok = True
    for name, ok, detail in checks:
        status = "✓" if ok else "✗"
        print(f"{status} {name:.<35} {detail}")
        if not ok:
            all_ok = False
    
    print("\n" + "="*50)
    if all_ok:
        print("✓ All checks passed! Installation successful.")
    else:
        print("✗ Some checks failed. See above.")
    print("="*50 + "\n")
    
    return all_ok

if __name__ == "__main__":
    sys.exit(0 if verify() else 1)
```

**Run verification:**

```bash
python verify_installation.py
```

### Run Applications

**Streamlit Dashboard:**

```bash
streamlit run app_streamlit.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**Flask API:**

```bash
python app_flask.py
```

Expected output:
```
 * Running on http://127.0.0.1:5001
 * Debug mode: on
```

---

## Troubleshooting

### Python Not Found

**Error**: `'python' is not recognized as an internal or external command`

**Solutions:**

1. **Reinstall Python** with "Add Python to PATH" checked
2. **Use python3** instead of python:
   ```bash
   python3 --version
   ```
3. **Add Python to PATH manually:**
   - Windows: Search "Environment Variables" → Edit PATH → Add Python folder
   - macOS/Linux: Add to `~/.bashrc` or `~/.zshrc`:
     ```bash
     export PATH="/usr/local/bin/python3:$PATH"
     ```

### Virtual Environment Not Activating

**Error**: `(venv)` doesn't appear in terminal

**Solutions:**

1. **Check script location:**
   ```bash
   # macOS/Linux
   source venv/bin/activate
   
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   
   # Windows CMD
   venv\Scripts\activate
   ```

2. **Fix PowerShell execution policy** (Windows):
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **Try `python -m pip` instead of `pip`:**
   ```bash
   python -m pip install -r requirements.txt
   ```

### Dependency Installation Fails

**Error**: `error: Microsoft Visual C++ 14.0 or greater is required`

**Solutions:**

1. **Windows**: Install Visual C++ Build Tools from https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. **Alternative**: Use pre-built wheels:
   ```bash
   pip install --only-binary :all: -r requirements.txt
   ```

### Model Download Fails

**Error**: `Connection timeout` or `SSL certificate verify failed`

**Solutions:**

1. **Check internet connection**
2. **Increase timeout:**
   ```python
   # In utils/similarity.py
   import os
   os.environ['HF_HUB_TIMEOUT'] = '600'  # 10 minutes
   ```

3. **Pre-download model:**
   ```python
   from sentence_transformers import SentenceTransformer
   model = SentenceTransformer('all-MiniLM-L6-v2')
   print(model)  # Should complete successfully
   ```

### Port Already in Use

**Error**: `Address already in use`

**Solutions:**

1. **Change port for Streamlit:**
   ```bash
   streamlit run app_streamlit.py --server.port 8502
   ```

2. **Change port for Flask** (edit `app_flask.py`):
   ```python
   app.run(port=5002)
   ```

3. **Kill process using port:**
   
   **Windows (PowerShell):**
   ```powershell
   Get-Process -Id (Get-NetTCPConnection -LocalPort 8501).OwningProcess | Stop-Process
   ```
   
   **macOS/Linux:**
   ```bash
   lsof -ti:8501 | xargs kill -9
   ```

### Out of Memory

**Error**: `MemoryError` or process killed

**Solutions:**

1. **Close other applications**
2. **Reduce corpus size** temporarily
3. **Use lighter model:**
   ```python
   # In utils/similarity.py
   model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v2')
   ```
4. **Increase swap space:**
   - Windows: Virtual memory settings
   - Linux: Add swap file

### Database Errors

**Error**: `database is locked` or `OperationalError`

**Solutions:**

1. **Close all instances** of the application
2. **Reset database:**
   ```bash
   rm plagiarism.db  # macOS/Linux
   del plagiarism.db  # Windows
   ```
3. **Restart application** (database will be recreated)

---

## Post-Installation Configuration

### Add Corpus Documents

Place reference documents in the `corpus/` folder:

```bash
mkdir corpus
cp reference1.txt corpus/
cp reference2.txt corpus/
```

Documents will be automatically loaded when you run checks.

### Configure Similarity Thresholds

Edit `utils/similarity.py` to adjust detection sensitivity:

```python
# Line ~60
if s_score > 50.0:  # Lower = more sensitive
    # ...
    if best_score > 40:  # Lower = more matches
        matches.append((chunk, best, d["filename"]))
```

### Set Flask Port

Edit `app_flask.py`:

```python
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Change port here
```

### Database Location

Database is created in project root as `plagiarism.db`. To change:

Edit `utils/db.py`:

```python
DB_FILE = "/custom/path/plagiarism.db"  # Change here
```

### Streamlit Configuration

Create `.streamlit/config.toml` in project root:

```toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"

[server]
headless = false
port = 8501
```

---

## Next Steps

1. **Read the README** for usage instructions
2. **Try the Streamlit app**: `streamlit run app_streamlit.py`
3. **Explore the Flask API** for programmatic access
4. **Add reference documents** to the corpus folder
5. **Run your first plagiarism check**!

---

## Getting Help

- **Check logs** for error messages
- **Search issues** on GitHub
- **Read documentation** in README.md
- **Open an issue** with details

---

**Installation complete! Enjoy using Plagiarism Checker! 🎉**

*Last updated: November 2, 2025*
