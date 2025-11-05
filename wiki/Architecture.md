# System Architecture

Understanding the design and architecture of the Plagiarism Checker.

## High-Level Overview

The Plagiarism Checker is built using a modular architecture that separates concerns into distinct components:

```
┌─────────────────────────────────────────────────────────┐
│                   User Interface Layer                   │
│                     (Streamlit)                          │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                 Application Layer                        │
│                      (app.py)                            │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┬──────────────┐
        ▼              ▼              ▼              ▼
┌─────────────┐ ┌────────────┐ ┌──────────┐ ┌───────────┐
│  Extractor  │ │Preprocessor│ │Similarity│ │  Report   │
│   Module    │ │   Module   │ │  Module  │ │  Module   │
└─────────────┘ └────────────┘ └──────────┘ └───────────┘
                                      │
                       ┌──────────────┴──────────────┐
                       ▼                             ▼
                ┌─────────────┐              ┌─────────────┐
                │   TF-IDF    │              │  Semantic   │
                │  Algorithm  │              │  Embedding  │
                └─────────────┘              └─────────────┘
                       │                             │
                       └──────────────┬──────────────┘
                                      ▼
                              ┌──────────────┐
                              │    Corpus    │
                              │  Documents   │
                              └──────────────┘
```

## Component Details

### 1. User Interface Layer (Streamlit)

**Responsibility:** Provides web-based interface for user interaction

**Key Features:**
- File upload widget
- Real-time processing feedback
- Results visualization
- Report download functionality

**Technologies:**
- Streamlit framework
- Python-based reactive UI
- Browser-based rendering

**File:** `app.py`

### 2. Application Layer

**Responsibility:** Orchestrates the plagiarism detection workflow

**Main Functions:**
1. Receive uploaded file
2. Coordinate text extraction
3. Manage preprocessing
4. Execute similarity analysis
5. Generate and deliver reports

**Workflow:**
```python
Upload → Extract → Clean → Compare → Report → Download
```

**File:** `app.py`

### 3. Text Extraction Module

**Responsibility:** Extract text from various document formats

**Component:** `utils.extractor`

**Supported Formats:**
- PDF (via PyPDF2)
- DOCX (via python-docx)

**Process Flow:**
```
File Input → Format Detection → Appropriate Parser → Raw Text
```

**Error Handling:**
- Validates file format
- Handles corrupted files
- Manages encoding issues

### 4. Preprocessing Module

**Responsibility:** Clean and normalize text for comparison

**Component:** `utils.preprocessor`

**Pipeline:**
```
Raw Text → Lowercase → Remove Punctuation → Remove Stopwords → Cleaned Text
```

**Key Operations:**
1. **Normalization:** Convert to lowercase
2. **Cleaning:** Remove special characters and numbers
3. **Filtering:** Remove stop words using NLTK
4. **Tokenization:** Split into words

**Dependencies:**
- NLTK (Natural Language Toolkit)
- Regular expressions (re module)

### 5. Similarity Analysis Module

**Responsibility:** Calculate similarity between documents

**Component:** `utils.similarity`

**Two-Algorithm Approach:**

#### Algorithm 1: TF-IDF Similarity

**Purpose:** Statistical text comparison

**Process:**
```
Text → Vectorization → TF-IDF Matrix → Cosine Similarity → Score
```

**How it works:**
1. Convert text to TF-IDF vectors
2. Each word gets a weight based on:
   - Term Frequency (TF): How often word appears in document
   - Inverse Document Frequency (IDF): How rare word is across documents
3. Calculate cosine similarity between vectors
4. Convert to percentage

**Best for:** Exact or near-exact matches

**Implementation:** scikit-learn's `TfidfVectorizer`

#### Algorithm 2: Semantic Similarity

**Purpose:** Meaning-based comparison

**Process:**
```
Text → Sentence Embedding → Vector → Cosine Similarity → Score
```

**How it works:**
1. Convert text to dense vector using pre-trained model
2. Embeddings capture semantic meaning
3. Similar meanings result in similar vectors
4. Calculate cosine similarity
5. Convert to percentage

**Best for:** Paraphrased content

**Implementation:** sentence-transformers library with `all-MiniLM-L6-v2` model

#### Combined Scoring

```python
final_score = (tfidf_score + semantic_score) / 2
```

**Rationale:**
- Balances statistical and semantic approaches
- Reduces false positives
- Improves overall accuracy

### 6. Report Generation Module

**Responsibility:** Create PDF reports

**Component:** `utils.report`

**Report Structure:**
```
┌────────────────────────────┐
│   Plagiarism Report        │
├────────────────────────────┤
│ Overall Score: XX%         │
├────────────────────────────┤
│ Comparison Details:        │
│  - file1.txt: XX%          │
│  - file2.txt: XX%          │
│  - ...                     │
└────────────────────────────┘
```

**Technology:** ReportLab library

**Features:**
- Professional formatting
- Automatic pagination
- Downloadable PDF format

### 7. Corpus Management

**Responsibility:** Maintain reference document database

**Structure:**
```
corpus/
├── arxiv_papers/
├── wikipedia_articles/
├── books/
└── custom_documents/
```

**Builder Scripts:**
- `build_corpus.py` - General purpose
- `build_research_corpus.py` - Academic focus

**Data Sources:**
1. **arXiv** - Research papers via RSS API
2. **Wikipedia** - Encyclopedia articles via API
3. **Project Gutenberg** - Classic literature via HTTP

## Data Flow Architecture

### Complete Plagiarism Check Flow

```
┌──────────┐
│  User    │
└────┬─────┘
     │ 1. Upload document (PDF/DOCX)
     ▼
┌──────────────────┐
│  Streamlit UI    │
└────┬─────────────┘
     │ 2. Pass file path
     ▼
┌──────────────────┐      3. Extract raw text
│   Extractor      │────────────────────────┐
└──────────────────┘                        │
                                            ▼
┌──────────────────┐      4. Clean text    ┌──────┐
│  Preprocessor    │◄───────────────────────┤ Text │
└────┬─────────────┘                        └──────┘
     │ 5. Preprocessed text
     ▼
┌──────────────────┐
│   Similarity     │◄──┐
│   Calculator     │   │ 6. For each corpus doc
└────┬─────────────┘   │
     │                 │
     │ 7. Read corpus  │
     ▼                 │
┌──────────────────┐   │
│  Corpus Files    │───┘
└──────────────────┘
     │
     │ 8. Compare & score
     ▼
┌──────────────────┐
│  Results List    │
└────┬─────────────┘
     │ 9. Generate report
     ▼
┌──────────────────┐
│  Report PDF      │
└────┬─────────────┘
     │ 10. Download
     ▼
┌──────────┐
│  User    │
└──────────┘
```

## Storage Architecture

### Directory Structure

```
Plagarism_checker/
├── app.py                  # Main application
├── build_corpus.py         # Corpus builder (general)
├── build_research_corpus.py # Corpus builder (research)
├── requirements.txt        # Dependencies
├── utils/                  # Core modules
│   ├── extractor.py
│   ├── preprocessor.py
│   ├── similarity.py
│   └── report.py
├── corpus/                 # Reference documents
│   ├── arxiv_*.txt
│   ├── *.txt
│   └── ...
├── uploads/                # Temporary uploaded files
│   └── *.pdf, *.docx
└── reports/                # Generated reports
    └── *_report.pdf
```

### Data Persistence

**Persistent Data:**
- Corpus documents (long-term storage)
- Generated reports (until manually deleted)

**Temporary Data:**
- Uploaded files (can be cleaned periodically)
- Processing intermediates (memory only)

**No Database Required:**
- File-based storage
- No SQL or NoSQL database
- Simple and portable

## Technology Stack

### Core Technologies

| Layer | Technology | Purpose |
|-------|-----------|---------|
| UI Framework | Streamlit | Web interface |
| ML/NLP | scikit-learn | TF-IDF vectorization |
| ML/NLP | sentence-transformers | Semantic embeddings |
| NLP | NLTK | Text preprocessing |
| Document | PyPDF2 | PDF text extraction |
| Document | python-docx | DOCX text extraction |
| Reporting | ReportLab | PDF generation |
| HTTP | requests | Download corpus |
| Parsing | BeautifulSoup | HTML parsing |
| APIs | feedparser | arXiv RSS feeds |
| APIs | wikipedia-api | Wikipedia content |

### Dependencies Graph

```
app.py
├── streamlit
├── utils.extractor
│   ├── PyPDF2
│   └── python-docx
├── utils.preprocessor
│   ├── nltk
│   └── re
├── utils.similarity
│   ├── scikit-learn
│   └── sentence-transformers
└── utils.report
    └── reportlab

build_corpus.py
├── wikipedia
├── requests
├── BeautifulSoup
├── feedparser
└── utils.preprocessor

build_research_corpus.py
├── feedparser
├── tqdm
└── utils.preprocessor
```

## Scalability Considerations

### Current Limitations

| Aspect | Limit | Impact |
|--------|-------|--------|
| Corpus size | ~2000 docs recommended | Processing time increases linearly |
| File size | ~50MB per document | Memory constraints |
| Concurrent users | 1 (local deployment) | Single-user application |
| Processing | Sequential | No parallel processing |

### Potential Optimizations

1. **Corpus Indexing:** Pre-compute TF-IDF vectors for corpus
2. **Caching:** Cache sentence embeddings
3. **Parallel Processing:** Multi-threaded corpus comparison
4. **Database:** Use vector database for faster similarity search
5. **API Mode:** Convert to REST API for multi-user support

## Security Architecture

### Data Privacy

- **No external transmission:** All processing is local
- **No cloud storage:** Files stay on your machine
- **No logging:** No sensitive data logged

### File Handling

- **Input validation:** File type checking
- **Safe parsing:** Error handling for malformed files
- **Temporary storage:** Uploads can be cleaned

### Dependencies

- **Open source:** All libraries are open source
- **Vetted packages:** PyPI standard libraries
- **Version pinning:** requirements.txt for reproducibility

## Deployment Architecture

### Local Deployment (Current)

```
Developer Machine
├── Python Runtime
├── Streamlit Server (localhost:8501)
└── Application Files
```

**Advantages:**
- Complete privacy
- No hosting costs
- Full control

**Disadvantages:**
- Single user only
- Requires Python installation
- Not accessible remotely

### Potential Deployment Options

**1. Docker Container:**
```dockerfile
FROM python:3.9
COPY . /app
RUN pip install -r requirements.txt
CMD streamlit run app.py
```

**2. Cloud Deployment:**
- Streamlit Cloud
- Heroku
- AWS EC2
- Google Cloud Run

**3. Shared Network:**
```bash
streamlit run app.py --server.address 0.0.0.0
```

## Design Principles

### Modularity
- Each utility is independent
- Clear separation of concerns
- Easy to test and maintain

### Simplicity
- File-based storage
- No complex database
- Straightforward workflow

### Extensibility
- Easy to add new document formats
- Simple to integrate new similarity algorithms
- Corpus can be expanded indefinitely

### Privacy-First
- Offline-first design
- No external API calls for core functionality
- User data never leaves the machine

## Future Architecture Enhancements

### Planned Improvements

1. **Batch Processing:** Handle multiple documents at once
2. **API Layer:** RESTful API for programmatic access
3. **Caching Layer:** Store pre-computed similarities
4. **Vector Database:** Faster similarity search
5. **User Management:** Multi-user support with authentication
6. **Real-time Analysis:** Stream processing for large documents
7. **Distributed Processing:** Handle larger corpora efficiently

### Extensibility Points

- **New Algorithms:** Add more similarity metrics
- **New Formats:** Support more document types
- **New Sources:** Integrate additional corpus sources
- **Enhanced Reports:** More detailed visualizations
- **Configuration:** User-configurable thresholds and settings

## See Also

- [API Reference](API-Reference.md) - Detailed function documentation
- [Usage Guide](Usage.md) - How to use the system
- [Building Corpus](Building-Corpus.md) - Corpus management
