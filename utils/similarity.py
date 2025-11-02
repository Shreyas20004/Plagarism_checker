import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util
from utils import db

model = SentenceTransformer('all-MiniLM-L6-v2')

def tfidf_similarity(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    return cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0] * 100

def semantic_similarity(text1, text2):
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2)
    return float(score[0][0]) * 100

def chunk_text(text, chunk_size=200):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks

def compare_with_corpus(input_text, corpus_folder):
    results = []
    for file in os.listdir(corpus_folder):
        path = os.path.join(corpus_folder, file)
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        tfidf_score = tfidf_similarity(input_text, content)
        sem_score = semantic_similarity(input_text, content)
        avg_score = (tfidf_score + sem_score) / 2
        results.append((file, avg_score))
    return sorted(results, key=lambda x: x[1], reverse=True)

def compare_with_db_corpus(submitted_text, top_k=5, corpus_folder="corpus"):
    """
    Compare submitted_text against BOTH:
      1. All documents stored in database
      2. All files in the corpus folder
    
    Returns:
      - summary list: [(filename, avg_score, doc_id/source)]
      - matches: list of (submitted_chunk, reference_chunk, filename) for creating diffs
    """
    results = []
    matches = []
    submitted_chunks = chunk_text(submitted_text, chunk_size=200)

    # ===== CHECK DATABASE DOCUMENTS =====
    docs = db.list_documents()
    for d in docs:
        ref_text = d["text"]
        # coarse TF-IDF and semantic on full text
        tfidf_score = tfidf_similarity(submitted_text, ref_text)
        sem_score = semantic_similarity(submitted_text, ref_text)
        avg_score = (tfidf_score + sem_score) / 2.0

        # find per-chunk best matches for highlighting
        for chunk in submitted_chunks:
            try:
                s_score = semantic_similarity(chunk, ref_text)
            except Exception:
                s_score = 0
            if s_score > 50.0:  # threshold for "interesting" match
                ref_chunks = chunk_text(ref_text, chunk_size=200)
                best = None
                best_score = 0
                for rchunk in ref_chunks:
                    sc = semantic_similarity(chunk, rchunk)
                    if sc > best_score:
                        best_score = sc
                        best = rchunk
                if best_score > 40:
                    matches.append((chunk, best, d["filename"]))
        results.append((d["filename"], avg_score, d["id"]))

    # ===== CHECK CORPUS FOLDER =====
    if os.path.exists(corpus_folder):
        for file in os.listdir(corpus_folder):
            path = os.path.join(corpus_folder, file)
            if os.path.isfile(path):
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    tfidf_score = tfidf_similarity(submitted_text, content)
                    sem_score = semantic_similarity(submitted_text, content)
                    avg_score = (tfidf_score + sem_score) / 2.0

                    # find per-chunk best matches for highlighting
                    for chunk in submitted_chunks:
                        try:
                            s_score = semantic_similarity(chunk, content)
                        except Exception:
                            s_score = 0
                        if s_score > 50.0:
                            ref_chunks = chunk_text(content, chunk_size=200)
                            best = None
                            best_score = 0
                            for rchunk in ref_chunks:
                                sc = semantic_similarity(chunk, rchunk)
                                if sc > best_score:
                                    best_score = sc
                                    best = rchunk
                            if best_score > 40:
                                matches.append((chunk, best, f"{file} (corpus)"))
                    results.append((f"{file} (corpus)", avg_score, file))
                except Exception as e:
                    print(f"Error processing {file}: {e}")

    results = sorted(results, key=lambda x: x[1], reverse=True)
    return results[:top_k], matches
