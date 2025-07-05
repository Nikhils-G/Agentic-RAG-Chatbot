# agents/retrieval_agent.py

from embeddings.embedder import get_embeddings
from mcp.message_dispatcher import MCPMessage

class RetrievalAgent:
    def __init__(self, dispatcher, vector_store):
        self.dispatcher = dispatcher
        self.vector_store = vector_store
        dispatcher.register_agent("RetrievalAgent", self.handle)

    def handle(self, message):
        query = message.payload["query"]
        query_embedding = get_embeddings([query])[0]
        top_chunks = self.vector_store.search(query_embedding)
        response = MCPMessage(
            sender="RetrievalAgent",
            receiver="LLMResponseAgent",
            type="RETRIEVAL_RESULT",
            trace_id=message.trace_id,
            payload={"retrieved_context": top_chunks, "query": query}
        )
        self.dispatcher.send_message(response)
