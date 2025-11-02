# Wiki Navigation

This directory contains comprehensive documentation for the Plagiarism Checker project.

## 📚 Documentation Pages

### [🏠 Home](Home.md)
Main landing page with project overview, features, and quick start guide.

### [💾 Installation](Installation.md)
Complete setup and installation instructions for all platforms.

### [🚀 Usage](Usage.md)
Step-by-step guide on using the plagiarism checker.

### [📖 Building Corpus](Building-Corpus.md)
How to create and manage your reference document corpus.

### [🔧 API Reference](API-Reference.md)
Technical documentation of all modules and functions.

### [🏗️ Architecture](Architecture.md)
System design, architecture, and technical details.

### [❓ FAQ](FAQ.md)
Frequently asked questions and troubleshooting.

---

## Quick Links

- **Getting Started:** [Installation](Installation.md) → [Usage](Usage.md)
- **Building Reference Corpus:** [Building Corpus](Building-Corpus.md)
- **Technical Details:** [Architecture](Architecture.md) → [API Reference](API-Reference.md)
- **Need Help?** [FAQ](FAQ.md)

## Setting Up GitHub Wiki

To publish these pages as a GitHub Wiki:

### Option 1: Using GitHub Web Interface

1. Go to your repository on GitHub
2. Click on the "Wiki" tab
3. Click "Create the first page"
4. For each markdown file in this directory:
   - Click "New Page"
   - Copy the filename (without .md) as the page title
   - Copy the content from the file
   - Click "Save Page"

### Option 2: Using Git (Recommended)

```bash
# Clone the wiki repository
git clone https://github.com/Shreyas20004/Plagarism_checker.wiki.git

# Copy all wiki files
cp wiki/*.md Plagarism_checker.wiki/

# Commit and push
cd Plagarism_checker.wiki/
git add .
git commit -m "Add comprehensive project documentation"
git push origin main
```

### Wiki Page Naming Convention

GitHub Wiki uses the following conventions:
- `Home.md` becomes the wiki homepage
- Other pages are accessible via their filename (without .md)
- Internal links use: `[Link Text](Page-Name)`

## Maintaining the Wiki

### Adding New Pages

1. Create a new `.md` file in the `wiki/` directory
2. Write your content using Markdown
3. Add links to the new page from existing pages
4. Publish to GitHub Wiki following the steps above

### Updating Pages

1. Edit the `.md` file in the `wiki/` directory
2. Update the GitHub Wiki page with new content

### Best Practices

- Use clear, descriptive page titles
- Include navigation links between related pages
- Keep the Home page updated with links to all major sections
- Use proper Markdown formatting
- Add code examples where appropriate
- Include images/diagrams if helpful (store in an `images/` folder)

---

**Note:** These documentation files are maintained in the repository under the `wiki/` directory for version control. To make them accessible as a GitHub Wiki, follow the setup instructions above.
