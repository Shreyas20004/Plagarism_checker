# Plagiarism Checker 🧾

A free, offline plagiarism detection tool that uses AI-powered semantic analysis and TF-IDF algorithms to identify similarities between documents.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Shreyas20004/Plagarism_checker.git
cd Plagarism_checker

# Install dependencies
pip install -r requirements.txt

# Build a reference corpus (optional but recommended)
python build_corpus.py

# Run the application
streamlit run app.py
```

Then open your browser to `http://localhost:8501`

## ✨ Features

- 🔒 **Completely Offline** - Your documents never leave your machine
- 📄 **Multiple Formats** - Supports PDF and DOCX files
- 🤖 **Dual Analysis** - Combines TF-IDF and semantic similarity
- 📊 **Detailed Reports** - Generates professional PDF reports
- 📚 **Customizable Corpus** - Build your own reference database
- 🎨 **Easy to Use** - Simple Streamlit web interface

## 📖 Documentation

**Comprehensive documentation is available in the [Project Wiki](https://github.com/Shreyas20004/Plagarism_checker/wiki)**

### Quick Links

- **[🏠 Home](wiki/Home.md)** - Overview and introduction
- **[💾 Installation Guide](wiki/Installation.md)** - Detailed setup instructions
- **[🚀 Usage Guide](wiki/Usage.md)** - How to use the plagiarism checker
- **[📖 Building Corpus](wiki/Building-Corpus.md)** - Create your reference database
- **[🔧 API Reference](wiki/API-Reference.md)** - Technical documentation
- **[🏗️ Architecture](wiki/Architecture.md)** - System design details
- **[❓ FAQ](wiki/FAQ.md)** - Common questions and troubleshooting

## 🎯 How It Works

1. **Upload** your document (PDF or DOCX)
2. **Extract** and preprocess the text
3. **Compare** against local corpus using:
   - TF-IDF vectorization for statistical matching
   - Sentence transformers for semantic similarity
4. **View** detailed similarity scores
5. **Download** a comprehensive PDF report

## 🛠️ Technology Stack

- **Streamlit** - Web interface
- **scikit-learn** - TF-IDF vectorization
- **sentence-transformers** - Semantic similarity (AI)
- **NLTK** - Text preprocessing
- **PyPDF2** - PDF text extraction
- **python-docx** - DOCX file handling
- **ReportLab** - PDF report generation

## 📋 Requirements

- Python 3.7 or higher
- 4 GB RAM (8 GB recommended)
- 500 MB disk space (2 GB with corpus)
- Internet connection (for initial setup only)

## 🔧 Installation

### Prerequisites

```bash
# Ensure Python 3.7+ is installed
python --version
```

### Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

See the [Installation Guide](wiki/Installation.md) for detailed instructions and troubleshooting.

## 📚 Building a Corpus

A corpus is essential for plagiarism detection. It's the reference database your documents are compared against.

### Automated Corpus Building

```bash
# General purpose corpus (Wikipedia, arXiv, Gutenberg)
python build_corpus.py

# Research-focused corpus (900+ academic papers)
python build_research_corpus.py
```

### Manual Corpus Building

1. Convert documents to plain text (.txt)
2. Place them in the `corpus/` directory
3. Run the plagiarism check

See [Building Corpus Guide](wiki/Building-Corpus.md) for more details.

## 🎓 Use Cases

- **Academic Institutions** - Check student assignments for plagiarism
- **Content Creators** - Verify originality of articles and content
- **Researchers** - Compare papers against existing literature
- **Publishers** - Screen submissions for duplicate content
- **Businesses** - Validate content before publication

## 🔒 Privacy & Security

- ✅ All processing happens locally on your machine
- ✅ No data is sent to external servers
- ✅ Your documents remain completely private
- ✅ No cloud storage or third-party services
- ✅ Open source and auditable code

## 📊 Understanding Results

| Similarity Score | Interpretation |
|-----------------|----------------|
| 0-20% | Low similarity - Likely original content |
| 20-40% | Moderate similarity - Some common phrases |
| 40-60% | High similarity - Significant overlap |
| 60-80% | Very high similarity - Substantial copying likely |
| 80-100% | Extremely high similarity - Nearly identical |

**Note:** Always review flagged content manually. High similarity doesn't always indicate plagiarism.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests
- ⭐ Star the repository

## 📝 License

This project is open source and available for educational and research purposes.

## 🆘 Getting Help

- **Documentation:** Check the [Wiki](https://github.com/Shreyas20004/Plagarism_checker/wiki)
- **FAQ:** See [Frequently Asked Questions](wiki/FAQ.md)
- **Issues:** Report bugs on [GitHub Issues](https://github.com/Shreyas20004/Plagarism_checker/issues)

## 🗺️ Roadmap

Future enhancements under consideration:

- [ ] Support for more file formats (TXT, RTF, ODT)
- [ ] Batch processing of multiple documents
- [ ] REST API for programmatic access
- [ ] Enhanced visualization of results
- [ ] Multi-language support
- [ ] GPU acceleration for faster processing

## 📸 Screenshots

*Coming soon - Run the application to see the interface!*

## 🙏 Acknowledgments

This project uses several excellent open-source libraries:
- [Streamlit](https://streamlit.io/) for the web interface
- [sentence-transformers](https://www.sbert.net/) for semantic analysis
- [scikit-learn](https://scikit-learn.org/) for TF-IDF
- [NLTK](https://www.nltk.org/) for text processing

## ⚠️ Disclaimer

This tool is provided as-is for educational and research purposes. While it uses advanced algorithms, no automated plagiarism detector is perfect. Always:
- Review flagged content manually
- Consider context and field-specific terminology
- Use as part of a comprehensive evaluation process
- Combine with human judgment

---

**Made with ❤️ for the open-source community**

For detailed documentation, visit the [Project Wiki](https://github.com/Shreyas20004/Plagarism_checker/wiki)
