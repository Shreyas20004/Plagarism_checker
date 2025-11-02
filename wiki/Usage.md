# Usage Guide

Learn how to use the Plagiarism Checker to detect similarities in your documents.

## Starting the Application

Once you've completed the [Installation](Installation.md), start the application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Using the Plagiarism Checker

### Step 1: Upload Your Document

1. Click the **"Upload PDF or DOCX"** button
2. Select a PDF or DOCX file from your computer
3. Wait for the file to upload

Supported formats:
- ✅ PDF (.pdf)
- ✅ Microsoft Word (.docx)

### Step 2: Text Extraction

Once uploaded, the system will automatically:
- Extract text from your document
- Clean and preprocess the text (remove stopwords, punctuation, etc.)
- Display a success message when complete

### Step 3: Run Plagiarism Check

1. Click the **"Run Plagiarism Check"** button
2. The system will compare your document against all files in the `corpus` folder
3. Processing time depends on:
   - Size of your document
   - Number of corpus documents
   - Complexity of the text

### Step 4: Review Results

The results page shows:

#### Overall Similarity Score
- A percentage indicating how similar your document is to the corpus
- Calculated as the average of all individual match scores

#### Match Breakdown
- A list of all corpus documents with their similarity scores
- Sorted from highest to lowest similarity
- Each entry shows:
  - Filename of the matched document
  - Similarity percentage (0-100%)

#### Interpretation Guide
- **0-20%**: Low similarity - Likely original content
- **20-40%**: Moderate similarity - Some common phrases or topics
- **40-60%**: High similarity - Significant overlap
- **60-80%**: Very high similarity - Substantial copying likely
- **80-100%**: Extremely high similarity - Nearly identical content

### Step 5: Download Report

1. Click the **"📄 Download Report"** button
2. A PDF report will be generated and downloaded
3. The report includes:
   - Overall similarity score
   - Detailed comparison with each corpus document
   - Professional formatting for sharing

## Example Workflow

### Academic Use Case

```
1. Professor receives student assignment (essay.docx)
2. Upload essay.docx to the plagiarism checker
3. System compares against corpus of academic papers
4. Results show 45% similarity with a specific paper
5. Download report for review and student feedback
```

### Content Verification Use Case

```
1. Editor receives article submission (article.pdf)
2. Upload article.pdf to the checker
3. Compare against database of published articles
4. Results show 15% similarity (acceptable)
5. Approve article for publication
```

## Understanding the Similarity Algorithms

The plagiarism checker uses two complementary methods:

### 1. TF-IDF Similarity
- **What it measures:** Statistical word frequency patterns
- **Good for:** Detecting exact or near-exact copying
- **How it works:** Compares word importance across documents

### 2. Semantic Similarity
- **What it measures:** Meaning and context
- **Good for:** Detecting paraphrased content
- **How it works:** Uses AI to understand sentence meaning

### Combined Score
The final similarity score is the average of both methods, providing a balanced and accurate assessment.

## Tips for Best Results

### Build a Quality Corpus
- Include diverse, relevant reference documents
- Regularly update your corpus with new content
- See [Building Corpus](Building-Corpus.md) for guidance

### Upload Clean Documents
- Ensure PDFs have extractable text (not scanned images)
- Use standard DOCX formatting
- Avoid password-protected files

### Interpret Scores Carefully
- High similarity doesn't always mean plagiarism
- Common knowledge and standard phrases will match
- Consider the context and field-specific terminology
- Review the actual matched content manually

### Processing Large Documents
- Larger documents take longer to process
- Consider breaking very large files into sections
- Ensure adequate system resources

## Stopping the Application

To stop the Streamlit server:

1. Go to the terminal where the app is running
2. Press `Ctrl+C` (Windows/Linux) or `Cmd+C` (macOS)
3. Confirm shutdown if prompted

## Configuration Options

### Changing the Port

To run on a different port:

```bash
streamlit run app.py --server.port 8080
```

### Running on a Network

To allow access from other devices on your network:

```bash
streamlit run app.py --server.address 0.0.0.0
```

Then access from other devices using: `http://YOUR_IP_ADDRESS:8501`

## Batch Processing

Currently, the application processes one document at a time. For batch processing:

1. Upload and check each document individually
2. Download each report
3. Compare reports manually

## Data Privacy

### What Gets Stored
- Uploaded files are temporarily stored in the `uploads/` folder
- Reports are saved in the `reports/` folder
- Corpus files remain in the `corpus/` folder

### What Doesn't Get Stored
- No data is sent to external servers
- All processing happens locally on your machine
- Your documents remain completely private

### Cleaning Up
To remove processed files:

```bash
# Remove uploaded files
rm -rf uploads/*

# Remove generated reports
rm -rf reports/*
```

## Next Steps

- Learn how to [Build and Customize Your Corpus](Building-Corpus.md)
- Explore the [API Reference](API-Reference.md) for advanced usage
- Check the [FAQ](FAQ.md) for common questions
