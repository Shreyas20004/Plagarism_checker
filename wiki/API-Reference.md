# API Reference

Technical documentation for the Plagiarism Checker modules and functions.

## Module Overview

The application is organized into the following modules:

```
Plagarism_checker/
├── app.py                      # Main Streamlit application
├── build_corpus.py             # General corpus builder
├── build_research_corpus.py    # Research-focused corpus builder
└── utils/
    ├── extractor.py           # Text extraction from files
    ├── preprocessor.py        # Text cleaning and preprocessing
    ├── similarity.py          # Similarity algorithms
    └── report.py              # PDF report generation
```

---

## `app.py`

Main application entry point using Streamlit.

### Configuration

```python
st.set_page_config(
    page_title="Free Plagiarism Checker",
    page_icon="🧾",
    layout="centered"
)
```

### Workflow

1. File upload handling
2. Text extraction via `extractor.extract_text()`
3. Text preprocessing via `preprocessor.clean_text()`
4. Similarity comparison via `similarity.compare_with_corpus()`
5. Report generation via `report.generate_report()`

---

## `utils.extractor`

Handles text extraction from various file formats.

### `extract_text(file_path)`

Extracts text content from PDF or DOCX files.

**Parameters:**
- `file_path` (str): Path to the file to extract text from

**Returns:**
- `str`: Extracted text content

**Raises:**
- `ValueError`: If file format is not supported

**Example:**
```python
from utils.extractor import extract_text

text = extract_text("document.pdf")
print(text)
```

**Supported Formats:**
- PDF (`.pdf`) - Uses PyPDF2
- DOCX (`.docx`) - Uses python-docx

**Implementation Details:**
- PDF: Iterates through all pages and extracts text
- DOCX: Extracts text from all paragraphs
- Returns empty string for pages/sections without text

---

## `utils.preprocessor`

Text cleaning and normalization functions.

### `clean_text(text)`

Cleans and preprocesses text for comparison.

**Parameters:**
- `text` (str): Raw text to clean

**Returns:**
- `str`: Cleaned and preprocessed text

**Example:**
```python
from utils.preprocessor import clean_text

raw = "The Quick Brown Fox! Jumps over the lazy dog."
cleaned = clean_text(raw)
# Output: "quick brown fox jumps lazy dog"
```

**Processing Steps:**
1. Convert to lowercase
2. Remove all non-alphabetic characters (except spaces)
3. Remove English stop words (using NLTK)
4. Join tokens with spaces

**Stop Words:**
- Uses NLTK's English stop words corpus
- Includes: "the", "a", "an", "is", "are", "was", etc.

**Note:** NLTK stop words are downloaded automatically on first use.

---

## `utils.similarity`

Similarity calculation algorithms.

### Module-Level Variables

```python
model = SentenceTransformer('all-MiniLM-L6-v2')
```
- Pre-loaded sentence transformer model for semantic similarity
- Downloaded automatically on first use (~80MB)

### `tfidf_similarity(text1, text2)`

Calculates TF-IDF based similarity between two texts.

**Parameters:**
- `text1` (str): First text
- `text2` (str): Second text

**Returns:**
- `float`: Similarity score (0-100)

**Example:**
```python
from utils.similarity import tfidf_similarity

score = tfidf_similarity("machine learning is great", "deep learning is awesome")
print(f"Similarity: {score:.2f}%")
```

**Algorithm:**
1. Create TF-IDF vectors for both texts
2. Calculate cosine similarity
3. Convert to percentage (0-100)

**Use Case:** Best for detecting exact or near-exact word matches.

### `semantic_similarity(text1, text2)`

Calculates semantic similarity using sentence embeddings.

**Parameters:**
- `text1` (str): First text
- `text2` (str): Second text

**Returns:**
- `float`: Similarity score (0-100)

**Example:**
```python
from utils.similarity import semantic_similarity

score = semantic_similarity(
    "The cat sat on the mat",
    "A feline rested on the rug"
)
print(f"Semantic similarity: {score:.2f}%")
```

**Algorithm:**
1. Generate embeddings using SentenceTransformer
2. Calculate cosine similarity between embeddings
3. Convert to percentage (0-100)

**Use Case:** Best for detecting paraphrased or reworded content.

### `compare_with_corpus(input_text, corpus_folder)`

Compares input text against all documents in the corpus.

**Parameters:**
- `input_text` (str): Text to check for plagiarism
- `corpus_folder` (str): Path to corpus directory

**Returns:**
- `list`: List of tuples `(filename, similarity_score)` sorted by score (highest first)

**Example:**
```python
from utils.similarity import compare_with_corpus
from utils.preprocessor import clean_text

text = clean_text("Your document text here")
results = compare_with_corpus(text, "corpus")

for filename, score in results[:5]:  # Top 5 matches
    print(f"{filename}: {score:.2f}%")
```

**Processing:**
1. Iterates through all files in `corpus_folder`
2. For each file:
   - Reads content
   - Calculates TF-IDF similarity
   - Calculates semantic similarity
   - Computes average score
3. Returns results sorted by similarity (descending)

**Error Handling:**
- Ignores files that can't be read (encoding errors)
- Handles empty corpus gracefully

---

## `utils.report`

PDF report generation.

### `generate_report(filename, scores, overall_score)`

Generates a PDF plagiarism report.

**Parameters:**
- `filename` (str): Output path for the PDF report
- `scores` (list): List of tuples `(file, score)` from similarity comparison
- `overall_score` (float): Overall similarity percentage

**Returns:**
- `None` (writes PDF file to disk)

**Example:**
```python
from utils.report import generate_report

results = [
    ("paper1.txt", 45.5),
    ("paper2.txt", 32.1),
    ("paper3.txt", 28.7)
]
overall = 35.4

generate_report("reports/my_report.pdf", results, overall)
```

**Report Contents:**
- Title: "Plagiarism Report"
- Overall similarity score
- Detailed breakdown of all matches
- Professional formatting

**Layout:**
- Page size: Letter (8.5" x 11")
- Fonts: Helvetica Bold (title), Helvetica (body)
- Automatic pagination when content exceeds one page

**Auto-Creates:**
- Creates output directory if it doesn't exist
- Overwrites existing reports with the same filename

---

## `build_corpus.py`

Script for building a general-purpose corpus.

### `download_arxiv(category, max_results)`

Downloads research papers from arXiv.

**Parameters:**
- `category` (str): arXiv category code (e.g., "cs.CL")
- `max_results` (int): Maximum number of papers to download

**Example:**
```python
download_arxiv("cs.AI", 100)
```

### `download_wikipedia(topics)`

Downloads articles from Wikipedia.

**Parameters:**
- `topics` (list): List of Wikipedia article titles

**Example:**
```python
download_wikipedia(["Machine Learning", "Python"])
```

### `download_gutenberg(book_ids)`

Downloads books from Project Gutenberg.

**Parameters:**
- `book_ids` (list): List of Gutenberg book ID numbers

**Example:**
```python
download_gutenberg([1342, 2701])  # Pride & Prejudice, Moby Dick
```

---

## `build_research_corpus.py`

Script for building a research-focused corpus.

### `fetch_arxiv_papers(category, max_results)`

Fetches academic papers from arXiv with metadata.

**Parameters:**
- `category` (str): arXiv category code
- `max_results` (int): Maximum papers to download (default: 200)

**Example:**
```python
fetch_arxiv_papers("cs.LG", max_results=300)
```

**Downloaded Content:**
- Paper title
- Authors
- Abstract
- All preprocessed and saved as text files

---

## Data Structures

### Similarity Result Tuple

```python
(filename: str, score: float)
```

**Example:**
```python
("arxiv_cs_AI_42.txt", 67.5)
```

### Comparison Results List

```python
[
    (filename: str, score: float),
    (filename: str, score: float),
    ...
]
```

Sorted by score in descending order.

---

## Constants and Configuration

### File Paths

```python
CORPUS_DIR = "corpus"
UPLOADS_DIR = "uploads"
REPORTS_DIR = "reports"
```

### Model Configuration

```python
SENTENCE_TRANSFORMER_MODEL = 'all-MiniLM-L6-v2'
```

### NLTK Configuration

```python
STOPWORDS = set(stopwords.words('english'))
```

---

## Error Handling

### Common Exceptions

**`ValueError`** - Raised by `extract_text()` for unsupported file formats

**`FileNotFoundError`** - When corpus folder or files don't exist

**`UnicodeDecodeError`** - Handled internally in `compare_with_corpus()`

### Best Practices

```python
try:
    text = extract_text("document.pdf")
except ValueError as e:
    print(f"Unsupported format: {e}")
except FileNotFoundError:
    print("File not found")
```

---

## Performance Considerations

### Processing Time

| Operation | Typical Time |
|-----------|-------------|
| Extract text (PDF) | < 1 second |
| Clean text | < 0.1 seconds |
| TF-IDF similarity | < 0.5 seconds per comparison |
| Semantic similarity | 1-3 seconds per comparison |
| Full corpus comparison (100 docs) | 2-5 minutes |

### Memory Usage

- Sentence Transformer model: ~400MB RAM
- Each corpus document: ~10-100KB in memory
- PDF/DOCX processing: Varies with file size

### Optimization Tips

- Limit corpus size for faster comparisons
- Use TF-IDF only for quick scans
- Batch process multiple documents separately
- Consider preprocessing corpus files once

---

## Version Information

This API reference is based on the current version of the plagiarism checker. 

**Dependencies:**
- Python: 3.7+
- Streamlit: Latest
- scikit-learn: Latest
- sentence-transformers: Latest
- NLTK: Latest
- PyPDF2: Latest
- python-docx: Latest
- reportlab: Latest

---

## See Also

- [Usage Guide](Usage.md) - Learn how to use these functions
- [Architecture](Architecture.md) - Understand the system design
- [Building Corpus](Building-Corpus.md) - Create reference documents
