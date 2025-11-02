import os
import feedparser
from tqdm import tqdm
from utils.preprocessor import clean_text

# Categories of research fields
CATEGORIES = [
    "cs.CL",  # Computational Linguistics
    "cs.AI",  # Artificial Intelligence
    "cs.LG",  # Machine Learning
    "cs.CV",  # Computer Vision
    "cs.SE",  # Software Engineering
    "stat.ML" # Statistics (Machine Learning)
]

os.makedirs("corpus", exist_ok=True)

def fetch_arxiv_papers(category, max_results=200):
    """Download abstracts from arXiv for a given category."""
    print(f"📚 Fetching {max_results} papers from arXiv category {category}...")
    base_url = "http://export.arxiv.org/api/query?search_query=cat:{}&start=0&max_results={}"
    url = base_url.format(category, max_results)
    
    feed = feedparser.parse(url)
    for i, entry in enumerate(tqdm(feed.entries, desc=f"{category}")):
        title = entry.title
        summary = entry.summary
        authors = ", ".join([a.name for a in entry.authors])
        text = f"Title: {title}\nAuthors: {authors}\nAbstract: {summary}"
        text = clean_text(text)
        filename = f"corpus/arxiv_{category.replace('.', '_')}_{i}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

if __name__ == "__main__":
    for cat in CATEGORIES:
        fetch_arxiv_papers(cat, max_results=150)
    print("\n✅ Research paper corpus built successfully in 'corpus/' folder.")
