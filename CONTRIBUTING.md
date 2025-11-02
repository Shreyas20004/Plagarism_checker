# Contributing to Plagiarism Checker

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the Plagiarism Checker project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Commit Messages](#commit-messages)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)

---

## Code of Conduct

This project adheres to a Code of Conduct to ensure a welcoming and inclusive environment for all contributors. By participating, you are expected to uphold this code:

- **Be respectful** of others' opinions and ideas
- **Welcome diverse perspectives** and experiences
- **Focus on constructive feedback**
- **Respect privacy** and confidentiality
- **Report harassment** to maintainers

---

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Virtual environment knowledge
- Basic familiarity with the project structure

### Setup Development Environment

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/plagiarism-checker.git
   cd plagiarism-checker
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/ORIGINAL-OWNER/plagiarism-checker.git
   ```

4. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows
   ```

5. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # For development tools (if exists)
   ```

6. **Verify setup**:
   ```bash
   python -c "import streamlit; import flask; print('✓ Setup successful')"
   ```

---

## Development Workflow

### 1. Create a Feature Branch

Always create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
```

**Branch naming conventions:**
- `feature/add-oauth-auth` — for new features
- `fix/handle-pdf-errors` — for bug fixes
- `docs/update-readme` — for documentation
- `refactor/optimize-similarity` — for code improvements
- `test/add-integration-tests` — for tests

### 2. Make Changes

Edit files and test locally:

```bash
streamlit run app_streamlit.py  # Test the UI
python app_flask.py              # Test the API
```

### 3. Keep Your Fork Updated

Before submitting, sync with upstream:

```bash
git fetch upstream
git rebase upstream/main  # or upstream/master
```

### 4. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 5. Submit Pull Request

Go to GitHub and create a PR against the main repository.

---

## Coding Standards

### Python Style (PEP 8)

Use a code formatter for consistency:

```bash
pip install black flake8
black utils/ app_*.py
flake8 utils/ app_*.py
```

**Key guidelines:**
- Line length: 100 characters (adjusted from 79 for readability)
- Indentation: 4 spaces
- Use snake_case for variables and functions
- Use UPPER_CASE for constants

### Example: Well-Formatted Function

```python
def compare_with_db_corpus(submitted_text, top_k=5, threshold=50.0):
    """
    Compare submitted text against database corpus.
    
    Args:
        submitted_text (str): Text to check for plagiarism
        top_k (int): Number of top matches to return (default: 5)
        threshold (float): Similarity threshold in percentage (default: 50.0)
    
    Returns:
        tuple: (results_list, matches_list)
            - results_list: [(filename, score, doc_id), ...]
            - matches_list: [(submitted_chunk, ref_chunk, filename), ...]
    
    Raises:
        ValueError: If submitted_text is empty
    """
    if not submitted_text or not submitted_text.strip():
        raise ValueError("submitted_text cannot be empty")
    
    # Implementation here
    results = []
    matches = []
    return results, matches
```

### Docstrings

Use Google-style docstrings:

```python
def function_name(param1, param2):
    """
    Brief description.
    
    Longer description if needed.
    
    Args:
        param1 (type): Description
        param2 (type): Description
    
    Returns:
        type: Description
    
    Raises:
        ExceptionType: When this occurs
    
    Example:
        >>> function_name("arg1", "arg2")
        expected_output
    """
    pass
```

### Type Hints

Add type hints for clarity:

```python
from typing import List, Tuple, Optional

def get_similarity(
    text1: str, 
    text2: str, 
    method: str = "semantic"
) -> float:
    """Calculate similarity score between texts."""
    # Implementation
    return score
```

### Comments

Write clear comments for complex logic:

```python
# ✓ Good
# Split text by sentences for granular comparison
sentences = text.split('.')

# ✗ Avoid
# split by dot
s = text.split('.')
```

---

## Testing

### Running Tests

If tests exist:

```bash
pytest tests/
pytest tests/test_similarity.py -v
```

### Writing Tests

Create test files in `tests/` directory:

```python
# tests/test_similarity.py
import pytest
from utils.similarity import tfidf_similarity, semantic_similarity

def test_tfidf_similarity_identical():
    """Test TF-IDF similarity with identical texts."""
    text = "The quick brown fox"
    score = tfidf_similarity(text, text)
    assert score == 100.0

def test_semantic_similarity_similar():
    """Test semantic similarity detects related text."""
    text1 = "The cat sat on the mat"
    text2 = "A feline rested on the rug"
    score = semantic_similarity(text1, text2)
    assert score > 50.0  # Should be fairly similar

def test_semantic_similarity_different():
    """Test semantic similarity detects unrelated text."""
    text1 = "Programming is fun"
    text2 = "I like eating pizza"
    score = semantic_similarity(text1, text2)
    assert score < 40.0  # Should be quite different
```

### Manual Testing Checklist

- [ ] Streamlit app runs without errors
- [ ] Flask API responds to all endpoints
- [ ] Database initializes correctly
- [ ] Upload & check functionality works
- [ ] PDF reports generate correctly
- [ ] HTML diffs display properly
- [ ] User authentication works

---

## Commit Messages

Write clear, descriptive commit messages:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only
- `style`: Changes that don't affect code meaning (formatting, missing semicolons, etc.)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to build process, dependencies, etc.

### Examples

```
feat(db): add embedding caching for faster comparisons

Implement SQLAlchemy model to store pre-computed embeddings.
This reduces semantic similarity computation time by ~80%.

Closes #42
```

```
fix(similarity): handle empty chunks in text comparison

Previously, empty chunks from poor sentence splitting could cause
errors. Now we filter them out before processing.

Fixes #38
```

```
docs: update README with Flask API examples

Added curl examples and endpoint descriptions for better clarity.
```

---

## Pull Request Process

### Before Submitting

1. **Test your code**: Run the app and verify functionality
2. **Format code**: Run `black` and `flake8`
3. **Update docs**: If you changed functionality, update README/docstrings
4. **Write tests**: Add tests for new features or bug fixes
5. **Rebase**: Sync with upstream and resolve conflicts

### PR Template

```markdown
## Description

Brief description of changes.

## Type of Change

- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## How Has This Been Tested?

Describe testing here.

## Checklist

- [ ] Code follows PEP 8
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No new warnings generated
```

### After Submission

- **Respond to feedback** promptly and professionally
- **Make requested changes** in new commits (or squash if requested)
- **Keep branch up to date** with main if needed
- **Be patient**: Review takes time

---

## Reporting Issues

### Issue Title

Be specific and concise:

✓ **Good**: "PDF reports not generating when document contains special characters"
✗ **Bad**: "Bug with PDF"

### Issue Body

Include:

```markdown
## Description

Clear description of the problem.

## Steps to Reproduce

1. Step one
2. Step two
3. Step three

## Expected Behavior

What should happen

## Actual Behavior

What actually happens

## Environment

- OS: [Windows 10 / macOS 12 / Ubuntu 22.04]
- Python: [3.9 / 3.10 / 3.11]
- Streamlit version: [1.51.0]

## Error Message

```
Paste full error traceback here
```

## Additional Context

Screenshots, logs, or other relevant information
```

---

## Feature Requests

### Good Feature Request

```markdown
## Description

I would like to add support for comparing documents with Wikipedia to catch verbatim plagiarism.

## Motivation

Currently, the tool only compares against a local corpus. Many students plagiarize from Wikipedia and other online sources. Adding online search would improve detection.

## Proposed Solution

1. Add optional `enable_web_search` parameter to comparison functions
2. Use free Wikipedia API or Google Custom Search API
3. Store results in database for faster repeat checks

## Alternative Solutions

- Could use requests library to scrape Google results (less reliable)
- Could integrate with plagiarism API services (less "open source")

## Additional Context

This aligns with the roadmap item about web search integration.
```

---

## Questions?

- **Check existing issues** first
- **Search documentation** and README
- **Ask in discussions** or open an issue labeled "question"

---

## Thank You! 🙏

Your contributions make this project better for everyone. We truly appreciate your time and effort!

**Happy coding!**

---

*Last updated: November 2, 2025*
