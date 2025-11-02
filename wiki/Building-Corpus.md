# Building Your Corpus

The corpus is a collection of reference documents that your uploaded files are compared against. A well-built corpus is essential for accurate plagiarism detection.

## What is a Corpus?

A **corpus** is a large collection of text documents used as a reference database. The plagiarism checker compares uploaded documents against all files in this corpus to identify similarities.

## Corpus Location

All corpus documents are stored in the `corpus/` directory in the project root.

```
Plagarism_checker/
├── corpus/              ← Your reference documents go here
│   ├── arxiv_cs_AI_0.txt
│   ├── Machine_Learning.txt
│   └── gutenberg_1342.txt
├── app.py
└── ...
```

## Quick Start: Automated Corpus Building

We provide two scripts to automatically build a corpus:

### Option 1: General Purpose Corpus

For a diverse corpus including academic papers, books, and encyclopedia content:

```bash
python build_corpus.py
```

**What it downloads:**
- 📘 **Wikipedia articles** on various topics (Machine Learning, AI, Climate Change, etc.)
- 📗 **Classic literature** from Project Gutenberg (Sherlock Holmes, Pride & Prejudice, etc.)
- 📙 **Research papers** from arXiv (Computational Linguistics category)

**Time required:** 10-30 minutes depending on internet speed

### Option 2: Research-Focused Corpus

For an academic/research-oriented corpus:

```bash
python build_research_corpus.py
```

**What it downloads:**
- 📚 **900+ research papers** from arXiv across multiple categories:
  - Computer Science (AI, Machine Learning, Computer Vision)
  - Computational Linguistics
  - Software Engineering
  - Statistics

**Time required:** 30-60 minutes

## Manual Corpus Building

You can also manually add documents to your corpus:

### Step 1: Prepare Your Documents

Convert your reference documents to plain text (.txt) format:

- **From PDF:** Use tools like `pdftotext` or online converters
- **From DOCX:** Save as .txt in Microsoft Word
- **From Web:** Copy and paste text content

### Step 2: Add to Corpus Folder

```bash
# Create the corpus folder if it doesn't exist
mkdir -p corpus

# Add your text files
cp /path/to/your/reference.txt corpus/
```

### Step 3: Organize Files

Use descriptive filenames:

```
corpus/
├── academic_paper_smith_2020.txt
├── textbook_chapter_3.txt
├── article_nature_genetics.txt
└── thesis_johnson_2019.txt
```

## Customizing Automated Corpus Building

### Modifying `build_corpus.py`

Edit the script to customize content:

```python
# Change Wikipedia topics
wikipedia_topics = [
    "Your Custom Topic 1",
    "Your Custom Topic 2", 
    "Biology", 
    "Chemistry"
]

# Change Gutenberg book IDs
gutenberg_ids = [
    1234,  # Your book ID
    5678   # Another book ID
]

# Change arXiv category and count
download_arxiv("cs.AI", 200)  # AI papers
download_arxiv("physics.gen-ph", 100)  # Physics papers
```

Available arXiv categories:
- `cs.AI` - Artificial Intelligence
- `cs.CL` - Computational Linguistics
- `cs.CV` - Computer Vision
- `cs.LG` - Machine Learning
- `cs.SE` - Software Engineering
- `math.ST` - Statistics
- `physics.*` - Various physics subcategories
- `q-bio.*` - Quantitative Biology

### Modifying `build_research_corpus.py`

Customize research paper categories and counts:

```python
CATEGORIES = [
    "cs.CL",   # Computational Linguistics
    "cs.AI",   # Artificial Intelligence
    "cs.LG",   # Machine Learning
    "cs.CV",   # Computer Vision
    "cs.SE",   # Software Engineering
    "stat.ML", # Statistics - Machine Learning
    "physics.comp-ph"  # Add your category
]

# Change number of papers per category
fetch_arxiv_papers(cat, max_results=300)  # Download 300 instead of 150
```

## Corpus Best Practices

### Size Recommendations

| Use Case | Recommended Corpus Size |
|----------|------------------------|
| Personal/Small Projects | 50-100 documents |
| Academic Classes | 200-500 documents |
| Research/Professional | 500-2000 documents |
| Large-Scale Detection | 2000+ documents |

### Quality Over Quantity

- ✅ Include relevant, high-quality documents
- ✅ Ensure diverse sources and topics
- ✅ Update corpus regularly
- ❌ Avoid duplicate or redundant content
- ❌ Don't include low-quality or spam content

### Domain-Specific Corpora

Build specialized corpora for specific fields:

**Computer Science Corpus:**
```bash
# Edit build_research_corpus.py to include only CS categories
CATEGORIES = ["cs.AI", "cs.LG", "cs.CV", "cs.SE"]
python build_research_corpus.py
```

**Literature Corpus:**
```bash
# Add classic literature from Project Gutenberg
# Edit gutenberg_ids in build_corpus.py with relevant book IDs
```

**Medical/Biology Corpus:**
```python
# Use arXiv bio categories
download_arxiv("q-bio.GN", 200)  # Genomics
download_arxiv("q-bio.QM", 200)  # Quantitative Methods
```

## Managing Your Corpus

### Viewing Corpus Statistics

```bash
# Count number of files
ls corpus/*.txt | wc -l

# Check total size
du -sh corpus/

# List all files
ls -lh corpus/
```

### Cleaning the Corpus

Remove all corpus files to start fresh:

```bash
rm -rf corpus/*
```

Remove specific files:

```bash
rm corpus/arxiv_*.txt  # Remove all arXiv papers
rm corpus/gutenberg_*.txt  # Remove all Gutenberg books
```

### Updating the Corpus

Periodically refresh your corpus:

```bash
# Backup existing corpus
cp -r corpus/ corpus_backup/

# Download fresh content
python build_corpus.py

# Merge old and new (remove duplicates manually)
```

## Corpus Text Preprocessing

All corpus documents are automatically preprocessed:
- Converted to lowercase
- Special characters removed
- Stop words filtered out
- Tokenized for efficient comparison

You don't need to preprocess manually added files - the system handles this automatically.

## Troubleshooting

### Issue: Download fails
- **Check internet connection**
- **Try reducing `max_results` in the scripts**
- **Some arXiv categories may have fewer papers**

### Issue: Corpus is too large
- **Remove unnecessary files**
- **Use more specific categories**
- **Limit `max_results` in download scripts**

### Issue: Not enough matches
- **Expand corpus with more diverse content**
- **Add documents from your specific domain**
- **Use both general and specialized corpus scripts**

### Issue: Too many false positives
- **Ensure corpus documents aren't too similar to each other**
- **Remove generic or template content**
- **Focus on high-quality, substantive documents**

## Advanced: Programmatic Corpus Building

Create custom corpus builders for specific sources:

```python
import os
from utils.preprocessor import clean_text

def add_custom_source(text_content, filename):
    """Add a custom document to the corpus."""
    os.makedirs("corpus", exist_ok=True)
    cleaned = clean_text(text_content)
    with open(f"corpus/{filename}", "w", encoding="utf-8") as f:
        f.write(cleaned)

# Example: Add content from a website
from bs4 import BeautifulSoup
import requests

def scrape_and_add(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    add_custom_source(text, filename)
```

## Next Steps

- Learn how to [Use the Plagiarism Checker](Usage.md)
- Understand the [System Architecture](Architecture.md)
- Check the [API Reference](API-Reference.md) for technical details
