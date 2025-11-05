# GitHub Wiki Setup Instructions

This document provides step-by-step instructions for converting the markdown files in the `wiki/` directory into a GitHub Wiki for the Plagiarism Checker project.

## What Was Created

The following comprehensive documentation has been created:

1. **Home.md** (2.9 KB) - Project overview, features, and quick start
2. **Installation.md** (3.8 KB) - Complete installation guide for all platforms
3. **Usage.md** (5.5 KB) - Detailed usage instructions and workflows
4. **Building-Corpus.md** (7.4 KB) - Comprehensive corpus creation and management guide
5. **API-Reference.md** (9.8 KB) - Complete technical API documentation
6. **Architecture.md** (12.5 KB) - System architecture and design documentation
7. **FAQ.md** (13 KB) - Extensive FAQ covering common questions
8. **README.md** (2.9 KB) - Wiki navigation and setup instructions

**Total: 8 files, ~58 KB of comprehensive documentation**

## Publishing to GitHub Wiki

### Method 1: Manual Upload via GitHub Web Interface

This is the easiest method if you're not familiar with Git.

#### Step 1: Enable Wiki
1. Go to https://github.com/Shreyas20004/Plagarism_checker
2. Click on "Settings" tab
3. Scroll to "Features" section
4. Check "Wikis" if not already enabled

#### Step 2: Create Wiki Pages
1. Click on the "Wiki" tab
2. Click "Create the first page"
3. For the homepage:
   - Title: Leave as "Home"
   - Content: Copy and paste the content from `wiki/Home.md`
   - Click "Save Page"

4. For each additional page:
   - Click "New Page"
   - Enter the page title (use the filename without .md):
     - `Installation`
     - `Usage`
     - `Building-Corpus`
     - `API-Reference`
     - `Architecture`
     - `FAQ`
   - Copy and paste the content from the corresponding file
   - Click "Save Page"

#### Step 3: Verify Links
- Navigate through the wiki pages
- Ensure all internal links work correctly
- Fix any broken links if needed

### Method 2: Git Clone and Push (Recommended)

This method is faster and preserves the structure better.

#### Step 1: Enable Wiki
Same as Method 1, Step 1.

#### Step 2: Clone Wiki Repository
```bash
# Clone the wiki (creates a new directory)
git clone https://github.com/Shreyas20004/Plagarism_checker.wiki.git

# Navigate to wiki directory
cd Plagarism_checker.wiki
```

#### Step 3: Copy Files
```bash
# Copy all wiki markdown files (run from the main repository)
cp ../wiki/*.md .

# Or if you're in the wiki clone directory:
cp ../Plagarism_checker/wiki/*.md .
```

#### Step 4: Commit and Push
```bash
# Add all files
git add *.md

# Commit
git commit -m "Add comprehensive project documentation

- Home page with overview and quick start
- Installation guide for all platforms
- Detailed usage instructions
- Corpus building guide
- Complete API reference
- Architecture documentation
- Extensive FAQ section"

# Push to GitHub
git push origin master
```

#### Step 5: Verify
Visit https://github.com/Shreyas20004/Plagarism_checker/wiki to see your wiki!

### Method 3: Using GitHub CLI (Alternative)

If you have GitHub CLI installed:

```bash
# Navigate to wiki directory
cd wiki

# For each file, create a wiki page
for file in *.md; do
  title="${file%.md}"
  gh wiki create "$title" --body "$(cat $file)"
done
```

## Wiki Structure

The wiki will have the following structure:

```
Wiki Home
├── Installation
├── Usage
├── Building Corpus
├── API Reference
├── Architecture
└── FAQ
```

### Internal Links

The wiki uses internal linking:
- `[Installation](Installation.md)` becomes a link to the Installation page
- `[FAQ](FAQ.md)` becomes a link to the FAQ page

GitHub automatically handles the `.md` extension.

## Wiki Features

### Sidebar Navigation

After publishing, you can create a sidebar for easy navigation:

1. In the wiki, click "Add a custom sidebar"
2. Title it `_Sidebar`
3. Add navigation links:

```markdown
### Navigation

**Getting Started**
- [Home](Home)
- [Installation](Installation)
- [Usage](Usage)

**Documentation**
- [Building Corpus](Building-Corpus)
- [API Reference](API-Reference)
- [Architecture](Architecture)

**Help**
- [FAQ](FAQ)
```

### Footer

You can also add a custom footer:

1. Click "Add a custom footer"
2. Title it `_Footer`
3. Add content like:

```markdown
---
📚 [Full Documentation](Home) | 🐛 [Report Issues](https://github.com/Shreyas20004/Plagarism_checker/issues) | ⭐ [Star on GitHub](https://github.com/Shreyas20004/Plagarism_checker)
```

## Maintaining the Wiki

### Updating Documentation

**From the Repository:**
1. Update the `.md` file in the `wiki/` directory
2. Commit and push changes
3. Clone the wiki repository (or pull if already cloned)
4. Copy updated files
5. Commit and push to wiki

**Directly in GitHub Wiki:**
1. Navigate to the wiki page
2. Click "Edit"
3. Make changes
4. Click "Save Page"

**Note:** If you edit directly in the wiki, those changes won't be reflected in the repository's `wiki/` directory automatically.

### Version Control

GitHub Wiki has its own Git repository:
- Clone URL: `https://github.com/Shreyas20004/Plagarism_checker.wiki.git`
- All changes are versioned
- You can view history and revert changes

### Adding New Pages

1. Create a new `.md` file in the `wiki/` directory
2. Write your content
3. Add links to the new page from existing pages
4. Follow one of the methods above to publish

## Troubleshooting

### Wiki Tab Not Visible
- Check repository settings to enable Wikis
- Refresh the page
- You may need repository admin permissions

### Links Not Working
- Ensure links use the format: `[Text](Page-Name)`
- Page names are case-sensitive
- Use hyphens for spaces: `Building-Corpus` not `Building Corpus`

### Images Not Displaying
- Upload images directly in the wiki editor
- Or use absolute URLs to images hosted elsewhere
- GitHub wiki supports image uploads

### Formatting Issues
- Ensure proper Markdown syntax
- Check for unclosed code blocks
- Verify list formatting (proper indentation)

## Best Practices

### Content Organization
- ✅ Keep Home page as overview with links to other pages
- ✅ Use descriptive page titles
- ✅ Include navigation links between related pages
- ✅ Add a table of contents for long pages

### Writing Style
- ✅ Use clear, concise language
- ✅ Include code examples where appropriate
- ✅ Add screenshots for UI features
- ✅ Keep content up-to-date with code changes

### Maintenance
- ✅ Review and update documentation regularly
- ✅ Fix broken links promptly
- ✅ Respond to documentation issues
- ✅ Keep repository and wiki in sync

## Additional Resources

- [GitHub Wiki Documentation](https://docs.github.com/en/communities/documenting-your-project-with-wikis)
- [Markdown Guide](https://www.markdownguide.org/)
- [GitHub Flavored Markdown](https://github.github.com/gfm/)

## Summary

You now have:
- ✅ 8 comprehensive markdown files ready for publication
- ✅ Clear instructions for publishing to GitHub Wiki
- ✅ Guidance on maintaining and updating the wiki
- ✅ Best practices for wiki management

The documentation covers:
- Project overview and features
- Complete installation guide
- Detailed usage instructions
- Corpus building and management
- Technical API reference
- System architecture
- Extensive FAQ

**Next Steps:**
1. Choose a publishing method (Method 2 recommended)
2. Follow the steps to publish to GitHub Wiki
3. Verify all pages and links work correctly
4. Optionally add a sidebar and footer
5. Share the wiki with users!

**Wiki URL (after publishing):**
https://github.com/Shreyas20004/Plagarism_checker/wiki
