import chromadb
from chromadb.config import Settings

class ChromaVectorStore:
    def __init__(self, collection_name="rag_chatbot"):
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory="./vector_store"
        ))
        self.collection = self.client.get_or_create_collection(collection_name)

    def add_documents(self, ids, embeddings, metadatas):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def query(self, query_embedding, n_results=3):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results
