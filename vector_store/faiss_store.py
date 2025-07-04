# vector_store/faiss_store.py

import faiss
import numpy as np

class VectorStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.chunks = []

    def add_embeddings(self, embeddings, chunks):
        self.index.add(np.array(embeddings))
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k=3):
        D, I = self.index.search(np.array([query_embedding]), top_k)
        return [self.chunks[i] for i in I[0]]
