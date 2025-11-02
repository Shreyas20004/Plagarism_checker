# API Reference

Complete documentation for the Flask REST API endpoints.

## Table of Contents

- [Overview](#overview)
- [Base URL](#base-url)
- [Authentication](#authentication)
- [Response Format](#response-format)
- [Endpoints](#endpoints)
  - [Register User](#post-register)
  - [Upload Document](#post-upload)
  - [Check Document](#post-check)
  - [List Reports](#get-reportsuser_id)
  - [Download Report](#get-download_report)

---

## Overview

The Plagiarism Checker Flask API provides programmatic access to plagiarism detection functionality. It's perfect for:

- Integrating plagiarism detection into applications
- Automating batch processing
- Building custom frontends
- Programmatic report generation

## Base URL

```
http://localhost:5001
```

Default port is `5001`. Change in `app_flask.py` if needed.

## Authentication

Current version uses **simple username-based identification** (suitable for internal/demo use).

⚠️ **For production**, implement proper authentication:
- OAuth2
- JWT tokens
- API keys
- Password hashing

## Response Format

All responses are JSON. Error responses include an `error` field:

```json
{
  "error": "Description of what went wrong"
}
```

Success responses include the requested data.

---

## Endpoints

### POST `/register`

Register a new user or retrieve an existing user.

#### Request

```bash
curl -X POST -F "username=alice" http://localhost:5001/register
```

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| username | string | Yes | Unique username identifier |

#### Response

**Status**: `200 OK`

```json
{
  "user_id": 1,
  "username": "alice"
}
```

**Status**: `400 Bad Request`

```json
{
  "error": "username required"
}
```

#### Example

```bash
# Request
curl -X POST -F "username=john_doe" http://localhost:5001/register

# Response
{
  "user_id": 1,
  "username": "john_doe"
}
```

---

### POST `/upload`

Upload a document for plagiarism checking.

#### Request

```bash
curl -X POST \
  -F "username=alice" \
  -F "file=@document.pdf" \
  http://localhost:5001/upload
```

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| username | string | Optional | Username (for tracking) |
| file | file | Yes | PDF or DOCX file |

#### Response

**Status**: `200 OK`

```json
{
  "doc_id": 1,
  "filename": "document.pdf"
}
```

**Status**: `400 Bad Request`

```json
{
  "error": "file missing"
}
```

#### Example

```bash
# Upload PDF
curl -X POST \
  -F "username=alice" \
  -F "file=@thesis.pdf" \
  http://localhost:5001/upload

# Response
{
  "doc_id": 5,
  "filename": "thesis.pdf"
}
```

---

### POST `/check`

Run plagiarism check on an uploaded document.

#### Request

```bash
curl -X POST \
  -F "username=alice" \
  -F "doc_id=1" \
  http://localhost:5001/check
```

**Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| username | string | Optional | Username (for report tracking) |
| doc_id | integer | Yes | Document ID from upload endpoint |

#### Response

**Status**: `200 OK`

```json
{
  "overall_score": 34.56,
  "top_matches": [
    {
      "filename": "arxiv_cs_AI_42.txt",
      "score": 67.89,
      "doc_id": 42
    },
    {
      "filename": "arxiv_cs_AI_15.txt",
      "score": 45.23,
      "doc_id": 15
    }
  ],
  "report_path": "reports/report_1.pdf",
  "diff_html": "reports/diffs/diff_1.html"
}
```

**Status**: `404 Not Found`

```json
{
  "error": "document not found"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| overall_score | float | Average similarity percentage (0-100) |
| top_matches | array | List of matching documents (sorted by score) |
| top_matches[].filename | string | Name of matching reference document |
| top_matches[].score | float | Similarity score for this match (0-100) |
| top_matches[].doc_id | integer | Database ID of matching document |
| report_path | string | File path to generated PDF report |
| diff_html | string or null | File path to HTML diff (null if no matches) |

#### Score Interpretation

- **0-20%**: Very low similarity (likely original)
- **20-40%**: Low similarity (minor overlap)
- **40-60%**: Moderate similarity (notable overlap)
- **60-80%**: High similarity (substantial plagiarism)
- **80-100%**: Very high similarity (likely plagiarism)

#### Example

```bash
# Request
curl -X POST \
  -F "username=alice" \
  -F "doc_id=5" \
  http://localhost:5001/check

# Response
{
  "overall_score": 28.4,
  "top_matches": [
    {
      "filename": "arxiv_cs_AI_89.txt",
      "score": 56.7,
      "doc_id": 89
    },
    {
      "filename": "arxiv_cs_AI_23.txt",
      "score": 34.2,
      "doc_id": 23
    }
  ],
  "report_path": "reports/report_5.pdf",
  "diff_html": "reports/diffs/diff_5.html"
}
```

---

### GET `/reports/<user_id>`

Retrieve all plagiarism reports for a specific user.

#### Request

```bash
curl http://localhost:5001/reports/1
```

**URL Parameters:**
| Name | Type | Description |
|------|------|-------------|
| user_id | integer | User ID (from register endpoint) |

#### Response

**Status**: `200 OK`

```json
[
  {
    "id": 1,
    "report_path": "reports/report_1.pdf",
    "diff_path": "reports/diffs/diff_1.html",
    "overall_score": 34.56,
    "created_at": "2025-11-02T14:30:45.123456"
  },
  {
    "id": 2,
    "report_path": "reports/report_5.pdf",
    "diff_path": "reports/diffs/diff_5.html",
    "overall_score": 28.4,
    "created_at": "2025-11-02T15:45:20.987654"
  }
]
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| id | integer | Report ID |
| report_path | string | Path to PDF report file |
| diff_path | string or null | Path to HTML diff file |
| overall_score | float | Overall similarity score |
| created_at | string | ISO 8601 timestamp of check |

#### Example

```bash
# Request
curl http://localhost:5001/reports/1

# Response
[
  {
    "id": 1,
    "report_path": "reports/report_1.pdf",
    "diff_path": "reports/diffs/diff_1.html",
    "overall_score": 34.56,
    "created_at": "2025-11-02T14:30:45.123456"
  }
]
```

---

### GET `/download_report`

Download a report file (PDF or HTML).

#### Request

```bash
curl -o report.pdf \
  "http://localhost:5001/download_report?path=reports/report_1.pdf"
```

**Query Parameters:**
| Name | Type | Required | Description |
|------|------|----------|-------------|
| path | string | Yes | Path to report file (from check or reports endpoints) |

#### Response

**Status**: `200 OK`

Binary file content (PDF or HTML)

**Status**: `404 Not Found`

```json
{
  "error": "file not found"
}
```

#### Example

```bash
# Download PDF report
curl -o my_report.pdf \
  "http://localhost:5001/download_report?path=reports/report_1.pdf"

# Download HTML diff
curl -o differences.html \
  "http://localhost:5001/download_report?path=reports/diffs/diff_1.html"
```

---

## Common Workflows

### Workflow 1: Basic Check

```bash
# 1. Register user
USER_ID=$(curl -s -X POST -F "username=alice" \
  http://localhost:5001/register | python -c "import sys, json; print(json.load(sys.stdin)['user_id'])")

# 2. Upload document
DOC_ID=$(curl -s -X POST \
  -F "username=alice" \
  -F "file=@document.pdf" \
  http://localhost:5001/upload | python -c "import sys, json; print(json.load(sys.stdin)['doc_id'])")

# 3. Run check
curl -X POST \
  -F "username=alice" \
  -F "doc_id=$DOC_ID" \
  http://localhost:5001/check

# 4. Download report
curl -o report.pdf \
  "http://localhost:5001/download_report?path=reports/report_${DOC_ID}.pdf"
```

### Workflow 2: Batch Processing

```bash
#!/bin/bash

# Process multiple files
for file in documents/*.pdf; do
  # Upload
  DOC_ID=$(curl -s -X POST \
    -F "username=batch_user" \
    -F "file=@$file" \
    http://localhost:5001/upload | python -c "import sys, json; print(json.load(sys.stdin)['doc_id'])")
  
  # Check
  curl -s -X POST \
    -F "username=batch_user" \
    -F "doc_id=$DOC_ID" \
    http://localhost:5001/check | python -m json.tool > "results/${file%.pdf}.json"
done
```

### Workflow 3: Get All Reports

```bash
# Get all reports for user
USER_ID=1
curl "http://localhost:5001/reports/$USER_ID" | python -m json.tool
```

---

## Error Handling

Always check for errors in responses:

```python
import requests
import json

def check_plagiarism(doc_id, username):
    response = requests.post(
        "http://localhost:5001/check",
        data={"doc_id": doc_id, "username": username}
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"Score: {result['overall_score']:.2f}%")
        return result
    else:
        error = response.json()
        print(f"Error: {error['error']}")
        return None
```

---

## Rate Limiting

Current implementation has **no rate limiting**. For production:

1. Implement rate limiting middleware
2. Use Flask-Limiter: `pip install Flask-Limiter`
3. Configure per IP/user limits

---

## CORS (Cross-Origin Requests)

Add CORS support for browser-based clients:

```bash
pip install flask-cors
```

```python
# In app_flask.py
from flask_cors import CORS
CORS(app)
```

---

## Timeout Considerations

Large document comparisons may take time:

- **Small document** (< 1 page): 5-10 seconds
- **Medium document** (1-5 pages): 10-30 seconds
- **Large document** (> 5 pages): 30-60 seconds

Increase timeout in your HTTP client if needed.

---

## Python Client Example

```python
import requests
from pathlib import Path

class PlagiarismCheckerClient:
    def __init__(self, base_url="http://localhost:5001"):
        self.base_url = base_url
    
    def register(self, username):
        r = requests.post(f"{self.base_url}/register", data={"username": username})
        return r.json()
    
    def upload(self, file_path, username=None):
        with open(file_path, "rb") as f:
            data = {"username": username} if username else {}
            files = {"file": f}
            r = requests.post(f"{self.base_url}/upload", data=data, files=files)
        return r.json()
    
    def check(self, doc_id, username=None):
        data = {"doc_id": doc_id}
        if username:
            data["username"] = username
        r = requests.post(f"{self.base_url}/check", data=data)
        return r.json()
    
    def list_reports(self, user_id):
        r = requests.get(f"{self.base_url}/reports/{user_id}")
        return r.json()
    
    def download_report(self, path, output_file):
        r = requests.get(f"{self.base_url}/download_report", params={"path": path})
        with open(output_file, "wb") as f:
            f.write(r.content)

# Usage
client = PlagiarismCheckerClient()

# Register
user = client.register("alice")
print(f"User ID: {user['user_id']}")

# Upload
doc = client.upload("thesis.pdf", username="alice")
print(f"Doc ID: {doc['doc_id']}")

# Check
result = client.check(doc['doc_id'], username="alice")
print(f"Score: {result['overall_score']:.2f}%")

# List reports
reports = client.list_reports(user['user_id'])
print(f"Total reports: {len(reports)}")
```

---

## Support

For API issues:
- Check the README.md troubleshooting section
- Review INSTALLATION.md
- Open a GitHub issue

---

*Last updated: November 2, 2025*
