# Frequently Asked Questions (FAQ)

Common questions and answers about the Plagiarism Checker.

## General Questions

### What is this plagiarism checker?

This is a free, offline plagiarism detection tool that compares uploaded documents against a local corpus of reference materials. It uses both statistical (TF-IDF) and semantic (AI-based) analysis to identify similarities.

### Is it really free?

Yes! This is completely free and open-source software. There are no hidden fees, subscription costs, or limitations on usage.

### Does it work offline?

Yes, once you've downloaded the required AI models and built your corpus, the entire system works offline. Your documents never leave your computer.

### How accurate is it?

The system uses two complementary algorithms (TF-IDF and semantic similarity) that together provide good accuracy. However, like all automated tools:
- It may produce false positives (flagging legitimate content)
- It may miss sophisticated paraphrasing
- Manual review of flagged content is always recommended

### What file formats are supported?

Currently supported:
- ✅ PDF (.pdf)
- ✅ Microsoft Word (.docx)

Not supported (yet):
- ❌ Plain text (.txt)
- ❌ RTF (.rtf)
- ❌ ODT (OpenDocument)
- ❌ Images with text

## Installation & Setup

### What are the system requirements?

**Minimum:**
- Python 3.7+
- 4 GB RAM
- 500 MB disk space

**Recommended:**
- Python 3.8+
- 8 GB RAM
- 2 GB disk space (for larger corpora)

### Why does installation take so long?

The first installation downloads several components:
- Python dependencies (~200MB)
- NLTK data (~100MB)
- Sentence transformer model (~80MB)

Subsequent runs are much faster.

### Do I need an internet connection?

**For setup:** Yes, to download dependencies and models

**For usage:** No, once set up, it works completely offline

**For corpus building:** Yes, if using the automated scripts to download reference materials

### Can I run this on Windows/Mac/Linux?

Yes! The application is cross-platform and works on:
- ✅ Windows 10/11
- ✅ macOS (Intel and Apple Silicon)
- ✅ Linux (Ubuntu, Debian, Fedora, etc.)

### Installation failed. What should I do?

Common solutions:
1. Make sure Python 3.7+ is installed: `python --version`
2. Update pip: `pip install --upgrade pip`
3. Try installing in a virtual environment
4. Check the [Installation Guide](Installation.md) for detailed steps
5. Check the error message for specific package issues

## Using the Application

### How do I start the application?

```bash
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

### Why is the first check so slow?

The first run downloads the sentence transformer model (~80MB). Subsequent checks are much faster.

### How long does a plagiarism check take?

Depends on:
- Document size (larger = slower)
- Corpus size (more documents = slower)
- Hardware (CPU speed)

Typical times:
- Small document (1-5 pages) + 100 corpus docs: 1-2 minutes
- Medium document (10-20 pages) + 500 corpus docs: 5-10 minutes
- Large document (50+ pages) + 1000 corpus docs: 15-30 minutes

### Can I check multiple documents at once?

Currently, no. The application processes one document at a time. For multiple documents, upload and check each one individually.

### What does the similarity percentage mean?

- **0-20%:** Low similarity - Likely original content
- **20-40%:** Moderate similarity - Some common phrases
- **40-60%:** High similarity - Significant overlap
- **60-80%:** Very high similarity - Substantial copying likely
- **80-100%:** Extremely high similarity - Nearly identical

**Note:** Context matters! Technical documents may have high similarity due to standard terminology.

### Why are my results showing 100% similarity?

Possible reasons:
1. You uploaded a document that's in your corpus
2. The document is identical or nearly identical to a corpus file
3. Very short documents with common phrases

### Why are all my results showing 0-5% similarity?

Possible reasons:
1. Your corpus doesn't contain relevant content
2. The document is in a different language
3. Highly technical or specialized vocabulary not in corpus
4. Empty or corrupted corpus files

### Can I check for plagiarism without a corpus?

No, the corpus is essential. The system compares your document against corpus files. Without a corpus, there's nothing to compare against.

See [Building Corpus](Building-Corpus.md) to create one.

## Corpus Building

### How many documents should be in my corpus?

**Recommendations:**
- **Minimum:** 50-100 documents for basic detection
- **Good:** 200-500 documents for most use cases
- **Better:** 500-1000 documents for comprehensive checking
- **Best:** 1000+ documents for professional use

Quality is more important than quantity!

### What should I include in my corpus?

Include documents relevant to what you'll be checking:

**For academic plagiarism:**
- Research papers in the field
- Textbooks and reference materials
- Wikipedia articles on key topics
- Previous student submissions (with permission)

**For content verification:**
- Published articles in your niche
- Common reference sources
- Competitor content
- Stock article templates

### How do I build a corpus automatically?

Use the provided scripts:

```bash
# General purpose corpus
python build_corpus.py

# Research-focused corpus
python build_research_corpus.py
```

See [Building Corpus](Building-Corpus.md) for details.

### Can I add my own documents to the corpus?

Yes! Simply:
1. Convert documents to plain text (.txt)
2. Copy them to the `corpus/` folder
3. They'll be included in the next plagiarism check

### How do I update my corpus?

```bash
# Add new documents
cp new_document.txt corpus/

# Remove old documents
rm corpus/old_document.txt

# Rebuild from scratch
rm corpus/*
python build_corpus.py
```

### Is it legal to use copyrighted material in my corpus?

**Legal disclaimer:** We're not lawyers. General guidance:

- ✅ **Academic use:** Generally permitted under fair use
- ✅ **Personal use:** Typically acceptable
- ❌ **Commercial use:** May require permissions
- ❌ **Redistribution:** Don't share copyrighted corpus

Always comply with copyright laws in your jurisdiction.

## Technical Questions

### What algorithms are used?

Two algorithms work together:

1. **TF-IDF (Term Frequency-Inverse Document Frequency)**
   - Statistical word matching
   - Good for exact or near-exact copying

2. **Semantic Similarity (Sentence Transformers)**
   - AI-based meaning analysis
   - Good for paraphrased content

Final score = average of both

### What is the sentence transformer model?

`all-MiniLM-L6-v2` is a pre-trained neural network that:
- Converts sentences to numerical vectors
- Captures semantic meaning
- Enables comparison of paraphrased text
- Runs locally (no cloud API needed)

### Can I use a different similarity algorithm?

Yes! The code is modular. You can:
1. Edit `utils/similarity.py`
2. Add your custom algorithm
3. Modify `compare_with_corpus()` to use it

Example algorithms you could add:
- Levenshtein distance
- Jaccard similarity
- LSA (Latent Semantic Analysis)
- BERT embeddings

### Does it detect paraphrasing?

Yes, partially. The semantic similarity algorithm can detect some paraphrasing, but:
- ✅ Simple paraphrasing (synonym replacement)
- ✅ Sentence restructuring
- ❌ Sophisticated human paraphrasing
- ❌ Complete rewording while keeping ideas

No automated tool catches everything!

### Does it work with non-English text?

**Currently:** No, the system is optimized for English:
- NLTK uses English stopwords
- The sentence transformer model is trained primarily on English

**Possible modifications:**
- Change NLTK language: `stopwords.words('spanish')`
- Use multilingual sentence transformer: `paraphrase-multilingual-MiniLM-L12-v2`

### Where is my data stored?

All data is stored locally:
- **Uploads:** `uploads/` folder
- **Corpus:** `corpus/` folder
- **Reports:** `reports/` folder

Nothing is sent to external servers.

### Is my data secure?

Yes! The application:
- ✅ Runs entirely on your machine
- ✅ Doesn't connect to external APIs (except during corpus building)
- ✅ Doesn't log sensitive information
- ✅ Doesn't require internet for core functionality

### Can I delete uploaded files?

Yes, uploaded files are just stored in the `uploads/` folder:

```bash
# Delete all uploads
rm -rf uploads/*

# Delete specific upload
rm uploads/myfile.pdf
```

## Performance & Optimization

### The application is slow. How can I speed it up?

**Quick fixes:**
1. Reduce corpus size - remove unnecessary files
2. Use a faster computer or upgrade RAM
3. Check only smaller document sections
4. Close other memory-intensive programs

**Advanced:**
1. Pre-compute corpus embeddings (requires code modification)
2. Use GPU acceleration (if available)
3. Implement parallel processing

### Can I use GPU acceleration?

The sentence transformer library supports GPU, but requires:
1. NVIDIA GPU with CUDA
2. PyTorch with CUDA support
3. Code modification to enable GPU

For most use cases, CPU is sufficient.

### Why is the application using so much RAM?

RAM usage comes from:
- Sentence transformer model (~400MB)
- Document processing (~100MB per document)
- Corpus loading (varies with size)

**Solutions:**
- Close other applications
- Use a smaller corpus
- Upgrade RAM if possible

## Troubleshooting

### The application won't start

**Check:**
1. Python version: `python --version` (must be 3.7+)
2. Streamlit installed: `pip show streamlit`
3. In correct directory: `ls app.py` should work
4. Try: `streamlit run app.py --logger.level=debug`

### "Module not found" error

```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or install specific package
pip install streamlit
```

### PDF text extraction returns empty text

**Possible causes:**
1. PDF is scanned image (not searchable)
2. PDF is password-protected
3. PDF uses unsupported encoding

**Solutions:**
1. Use OCR software to make PDF searchable
2. Remove password protection
3. Try converting to DOCX first

### DOCX extraction fails

**Possible causes:**
1. Corrupted DOCX file
2. Unsupported Word version
3. File is actually a different format

**Solutions:**
1. Open and re-save in Microsoft Word
2. Try converting to PDF first
3. Check file extension is truly .docx

### Report generation fails

**Check:**
1. `reports/` folder exists (created automatically)
2. Disk space available
3. Write permissions

```bash
mkdir -p reports
chmod 755 reports
```

### Download button doesn't work

**Try:**
1. Use a different browser (Chrome, Firefox recommended)
2. Check browser allows downloads from localhost
3. Try right-click → "Save As"

## Comparison with Other Tools

### How does this compare to Turnitin?

| Feature | This Tool | Turnitin |
|---------|-----------|----------|
| Cost | Free | Paid subscription |
| Privacy | Completely offline | Uploads to cloud |
| Corpus | You build it | Massive database |
| Accuracy | Good | Excellent |
| Speed | Moderate | Fast |
| Database | Custom | Billions of documents |

**Use this for:** Privacy, cost savings, custom corpora
**Use Turnitin for:** Comprehensive academic checking

### How does this compare to Grammarly?

Different tools! 
- **Grammarly:** Writing assistance and basic plagiarism
- **This tool:** Focused plagiarism detection with custom corpus

### Is this better than online plagiarism checkers?

**Advantages:**
- ✅ Completely private
- ✅ Free
- ✅ Customizable corpus
- ✅ Offline capability

**Disadvantages:**
- ❌ Smaller database
- ❌ Requires technical setup
- ❌ Less convenient than web tools

## Contributing & Support

### How can I contribute?

Contributions welcome! You can:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation
- Share corpus building techniques

### Where can I get help?

1. Check this FAQ first
2. Review other [wiki pages](Home.md)
3. Check the GitHub issues
4. Submit a new issue with details

### Can I use this commercially?

Check the project license. Generally:
- ✅ Internal business use
- ❌ Selling as a service (without modifications)
- ❌ Removing attribution

### How do I report a bug?

Submit a GitHub issue with:
1. What you were trying to do
2. What happened instead
3. Error messages (if any)
4. Your system info (OS, Python version)

## Future Development

### What features are planned?

Potential future additions:
- More file format support
- Batch processing
- API mode
- Better visualization
- Advanced reporting
- Multi-language support

### Can I request features?

Yes! Submit feature requests as GitHub issues.

### Is this project maintained?

Check the GitHub repository for recent activity and commits.

---

## Still have questions?

- Check the [Home](Home.md) page
- Review the [Usage Guide](Usage.md)
- Read the [API Reference](API-Reference.md)
- See the [Architecture](Architecture.md) documentation
