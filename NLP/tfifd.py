import argparse
from typing import List, Dict
from glob import glob
import PyPDF2
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from functools import reduce 
import numpy as np
from tqdm import tqdm
from pathlib import Path

nltk.download('stopwords')

def parse_args() -> str:
    parser = argparse.ArgumentParser(description="Document search service")
    parser.add_argument("query", type=str, help="query")
    parser.add_argument("path", type=str, help="document path")
    return parser.parse_args()

def inverse_document_frequency(df: int, document_nums: int):
    return np.log(document_nums/df)

def document_frequency(corpus: List[str], query: List[str]) -> List[str]:
    result = []
    for q in query: 
        num = 0
        for document in corpus:
            S = set(document.split())
            if q in S: 
                num += 1
                break
        result.append(num)
    return np.array(result)

def term_frequency(corpus: List[str], query: List[str]) -> float:
    result = np.zeros([len(query), len(corpus)])
    for i, q in enumerate(query):
        for j, document in enumerate(corpus):
            V = 171476 
            freqs = bag_of_word(document, stopwords)
            f = freqs.get(q, 0)
            result[i][j] = f
    return np.array(result)

def bag_of_word(text: str, stopwords: List[str]) -> Dict[str, int]:
    words = text.split()
    freqs = {w:0 for w in set(words)}
    for w in words:
        if w in stopwords: 
            continue
        freqs[w] += 1
    freqs = dict(sorted(freqs.items(), key=lambda item: -item[1]))
    return freqs

def add(freq1: Dict[str, int], freq2: Dict[str, int] ) -> Dict[str, int]: 
    F = {}
    keys = list(freq1.keys()) + list(freq2.keys())
    for k in keys:
        v1 = freq1.get(k, 0)
        v2 = freq2.get(k, 0)
        F[k] = v1 + v2
    return F

def score(corpus: List[str], query: List[str]):
    # 1xQ
    dfs = document_frequency(corpus, query)
    # QxD
    tfs = term_frequency(corpus, query)
    idf = inverse_document_frequency(dfs, len(corpus))
    return (tfs*idf)[0]

if __name__ == "__main__":
    ds = parse_args()
    query = [ds.query]
    path  = ds.path
    stopwords = stopwords.words('english')

    docs  = []
    files = []
    for file in glob(f"{path}/*"):
        pdf_reader = PyPDF2.PdfReader(file)
        freqs = {}
        document = ""
        for page_num in tqdm(range(len(pdf_reader.pages))):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            document += page_text + "\n"
        docs.append(document)
        files.append(file)
    scores = score(docs, query)
    print("-----------")
    for f, s in zip(files, scores):
        print(f"{Path(f).stem}: {round(s,3)}")
    print("-----------")


