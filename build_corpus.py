import os
import wikipedia
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from utils.preprocessor import clean_text
import feedparser

os.makedirs("corpus", exist_ok=True)

def download_arxiv(category="cs.CL", max_results=100):
    print(f"📙 Downloading {max_results} papers from arXiv category {category}...")
    url = f"http://export.arxiv.org/api/query?search_query=cat:{category}&max_results={max_results}"
    feed = feedparser.parse(url)
    for i, entry in enumerate(feed.entries):
        text = clean_text(entry.title + " " + entry.summary)
        with open(f"corpus/arxiv_{category}_{i}.txt", "w", encoding="utf-8") as f:
            f.write(text)

def download_wikipedia(topics):
    print("📘 Downloading from Wikipedia...")
    for topic in tqdm(topics):
        try:
            page = wikipedia.page(topic)
            text = clean_text(page.content)
            with open(f"corpus/{topic.replace(' ', '_')}.txt", "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            print(f"Skipped {topic}: {e}")

def download_gutenberg(book_ids):
    print("📗 Downloading from Project Gutenberg...")
    base = "https://www.gutenberg.org/files/{id}/{id}-0.txt"
    for book_id in tqdm(book_ids):
        try:
            url = base.format(id=book_id)
            text = requests.get(url, timeout=10).text
            text = clean_text(text)
            with open(f"corpus/gutenberg_{book_id}.txt", "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            print(f"Error with {book_id}: {e}")

if __name__ == "__main__":
    wikipedia_topics = [
        "Machine Learning", "Artificial Intelligence", "Climate Change", 
        "Computer Networks", "Quantum Computing", "Economics", 
        "Blockchain", "Data Science", "Cybersecurity", "Genetics"
    ]
    gutenberg_ids = [1661, 1342, 2701, 74, 84]  # Sherlock Holmes, Pride & Prejudice, etc.

    download_wikipedia(wikipedia_topics)
    download_gutenberg(gutenberg_ids)
    download_arxiv("cs.CL", 100)

    print("✅ Corpus built successfully in /corpus folder")
