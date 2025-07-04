## Agentic RAG Chatbot

### Overview

This project implements an **Agent-based Retrieval-Augmented Generation (RAG) Chatbot** capable of answering questions based on uploaded multi-format documents. The chatbot uses an **agentic architecture with a Model Context Protocol (MCP)** for message passing between agents, facilitating modularity and clear inter-agent communication.

The system supports document uploads in formats including **PDF, PPTX, DOCX, CSV, and TXT**, parses the content, semantically retrieves relevant context, and generates answers using a Large Language Model (LLM) via Cohere API.

---

## Features

* **Upload and Ingest Documents** (PDF, PPTX, DOCX, CSV, TXT)
* **Multi-Agent System Architecture**

  * Ingestion Agent: Parses and preprocesses documents.
  * Retrieval Agent: Embeds content and performs semantic search.
  * LLM Response Agent: Formats prompts and generates final answers.
* **Model Context Protocol (MCP) for message-based agent coordination**
* **FAISS vector store for fast similarity search**
* **Cohere LLM (command-r-plus) integration for response generation**
* **Clean, responsive Streamlit UI**
* **Multi-turn question answering on ingested document context**

---

## Project Structure

agentic_rag_chatbot/
├── agents/
│   ├── ingestion_agent.py
│   ├── retrieval_agent.py
│   └── llm_response_agent.py
│
├── mcp/
│   └── message_dispatcher.py
│
├── vector_store/
│   └── faiss_store.py
│
├── parsers/
│   ├── pdf_parser.py
│   ├── pptx_parser.py
│   ├── docx_parser.py
│   ├── csv_parser.py
│   └── txt_parser.py
│
├── embeddings/
│   └── embedder.py       
│
├── utils/
│   └── chunking.py               
│
├── ui/
│   └── streamlit_app.py
│
├── static/                      
│
├── main.py                      
├── README.md
├── requirements.txt
└── .gitignore


---

## System Flow

1. **User uploads document** via Streamlit UI.
2. **Ingestion Agent** parses and embeds document content into FAISS vector store.
3. User enters a question through the interface.
4. **Retrieval Agent** performs semantic similarity search to find top relevant chunks.
5. **LLM Response Agent** formats a prompt combining retrieved context and user query, sends it to the Cohere API.
6. Generated answer is displayed on the UI.

**All inter-agent communications are handled via MCP messages.**

---

## MCP (Model Context Protocol)

A lightweight, structured protocol for agent communication through in-memory message passing.
Typical MCP message format:

```json
{
  "sender": "RetrievalAgent",
  "receiver": "LLMResponseAgent",
  "type": "RETRIEVAL_RESULT",
  "trace_id": "rag-457",
  "payload": {
    "retrieved_context": ["context chunk 1", "context chunk 2"],
    "query": "What KPIs were tracked in Q1?"
  }
}
```

---

## Technologies Used

* **Python 3.11+**
* **Cohere API (command-r-plus model)**
* **FAISS (Facebook AI Similarity Search)**
* **Streamlit** for front-end UI
* **Sentence Transformers (all-MiniLM-L6-v2)** for text embeddings
* **python-pptx**, **python-docx**, **PyMuPDF**, **Pandas** for document parsing

---

## Installation and Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/agentic_rag_chatbot.git
cd agentic_rag_chatbot
```

2. **Create and activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your Cohere API key**

Replace the placeholder in `agents/llm_response_agent.py`:

```python
co = cohere.Client("YOUR_COHERE_API_KEY")
```

5. **Run the Streamlit app**

```bash
streamlit run ui/streamlit_app.py
```

---

## Deliverables

* Complete, clean, well-organized codebase
* Architecture diagram (MCP agent-based flow)
* System flow diagram (message passing structure)
* UI Screenshots
* PPT Presentation (included in `docs/`)
* (Optional) 5-minute walkthrough video

---

## Challenges Faced

* Managing seamless message passing and traceability via MCP
* Parsing inconsistencies between different document formats
* Embedding large documents efficiently into FAISS
* Handling multi-turn queries with context retention
* Dealing with third-party package compatibility issues in Python 3.11+

---

## Future Improvements

* Add support for Markdown and Excel formats
* Integrate other LLM providers like OpenAI, Mistral, or LLaMA 3
* Deploy as a web service using FastAPI and Docker
* Implement asynchronous message queues (e.g., RabbitMQ, Kafka)
* Multi-user support with chat history management
* Add PDF page-wise retrieval and context highlighting
