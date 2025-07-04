from mcp.message_dispatcher import MCPDispatcher
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from vector_store.faiss_store import VectorStore
import parsers.pdf_parser as pdf
import parsers.pptx_parser as pptx
import parsers.docx_parser as docx
import parsers.csv_parser as csv
import parsers.txt_parser as txt
from mcp.message_dispatcher import MCPMessage

dispatcher = MCPDispatcher()
vector_store = VectorStore(dim=384)

parsers = {
    "pdf": pdf.parse_pdf,
    "pptx": pptx.parse_pptx,
    "docx": docx.parse_docx,
    "csv": csv.parse_csv,
    "txt": txt.parse_txt
}

IngestionAgent(dispatcher, vector_store, parsers)
RetrievalAgent(dispatcher, vector_store)
LLMResponseAgent(dispatcher)

