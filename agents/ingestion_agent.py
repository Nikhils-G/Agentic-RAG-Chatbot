# agents/ingestion_agent.py

from utils.chunking import chunk_text
from embeddings.embedder import get_embeddings

class IngestionAgent:
    def __init__(self, dispatcher, vector_store, parsers):
        self.dispatcher = dispatcher
        self.vector_store = vector_store
        self.parsers = parsers
        dispatcher.register_agent("IngestionAgent", self.handle)

    def handle(self, message):
        file_path = message.payload["file_path"]
        file_type = message.payload["file_type"]
        text = self.parsers[file_type](file_path)
        chunks = chunk_text(text)
        embeddings = get_embeddings(chunks)
        self.vector_store.add_embeddings(embeddings, chunks)
        print(f"[IngestionAgent] Ingested {file_path}")
