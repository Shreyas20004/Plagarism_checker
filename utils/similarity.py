import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def tfidf_similarity(text1, text2):
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    return cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0] * 100

def semantic_similarity(text1, text2):
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    score = util.cos_sim(emb1, emb2)
    return float(score[0][0]) * 100

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
