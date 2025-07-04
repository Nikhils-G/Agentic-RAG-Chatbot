import sys
import os
# Add project root directory to sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
print("Python PATH:", sys.path)
print("Working dir:", os.getcwd())
from mcp.message_dispatcher import MCPDispatcher, MCPMessage
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from vector_store.faiss_store import VectorStore
import parsers.pdf_parser as pdf
import parsers.pptx_parser as pptx
import parsers.docx_parser as docx
import parsers.csv_parser as csv
import parsers.txt_parser as txt
import streamlit as st

# ✅ Initialize Dispatcher and VectorStore
dispatcher = MCPDispatcher()
vector_store = VectorStore(dim=384)
parsers_dict = {
    "pdf": pdf.parse_pdf,
    "pptx": pptx.parse_pptx,
    "docx": docx.parse_docx,
    "csv": csv.parse_csv,
    "txt": txt.parse_txt
}

# ✅ Register agents
IngestionAgent(dispatcher, vector_store, parsers_dict)
RetrievalAgent(dispatcher, vector_store)
LLMResponseAgent(dispatcher)

# 🎨 Clean, Professional CSS
st.markdown("""
<style>
/* Import clean, modern font */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Remove default Streamlit styling */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {visibility: hidden;}

/* Global Variables */
:root {
    --primary-color: #2563eb;
    --primary-hover: #1d4ed8;
    --secondary-color: #64748b;
    --background: #C9B27C;
    --surface: #ffffff;
    --text-primary: #1e293b;
    --text-secondary: #64748b;
    --border: #e2e8f0;
    --success: #10b981;
    --info: #3b82f6;
    --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --radius: 8px;
    --radius-lg: 12px;
}

/* App Container */
.stApp {
    background-color: var(--background);
    font-family: 'Inter', sans-serif;
}

.main > div {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 800px;
    margin: 0 auto;
}

/* Header */
.app-header {
    text-align: center;
    margin-bottom: 3rem;
    padding: 2rem 0;
}

.app-title {
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
    line-height: 1.2;
}

.app-subtitle {
    font-size: 1.1rem;
    color: var(--text-secondary);
    font-weight: 400;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;
}

/* Cards */
.card {
    background: var(--surface);
    border-radius: var(--radius-lg);
    padding: 2rem;
    margin-bottom: 2rem;
    box-shadow: var(--shadow);
    border: 1px solid var(--border);
}

.card-header {
    display: flex;
    align-items: center;
    margin-bottom: 1.5rem;
}

.card-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin: 0;
}

.card-icon {
    width: 20px;
    height: 20px;
    margin-right: 0.75rem;
    color: var(--primary-color);
}

.card-description {
    color: var(--text-secondary);
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    line-height: 1.5;
}

/* File Upload Styling */
.stFileUploader {
    border: 2px dashed var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 2rem !important;
    background: var(--background) !important;
    transition: all 0.2s ease !important;
}

.stFileUploader:hover {
    border-color: var(--primary-color) !important;
    background: rgba(37, 99, 235, 0.05) !important;
}

.stFileUploader > div {
    color: var(--text-secondary) !important;
    font-family: 'Inter', sans-serif !important;
    text-align: center !important;
}

.stFileUploader label {
    color: var(--text-primary) !important;
    font-weight: 500 !important;
}

/* Text Input */
.stTextInput > div > div > input {
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 0.75rem 1rem !important;
    font-size: 1rem !important;
    font-family: 'Inter', sans-serif !important;
    background: var(--surface) !important;
    color: var(--text-primary) !important;
    transition: border-color 0.2s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: var(--primary-color) !important;
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
}

.stTextInput > div > div > input::placeholder {
    color: var(--text-secondary) !important;
}

/* Text Area */
.stTextArea > div > div > textarea {
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 1rem !important;
    font-size: 0.95rem !important;
    font-family: 'Inter', sans-serif !important;
    background: var(--surface) !important;
    color: var(--text-primary) !important;
    line-height: 1.6 !important;
    resize: vertical !important;
}

.stTextArea > div > div > textarea:focus {
    border-color: var(--primary-color) !important;
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
}

/* Success and Info Messages */
.stSuccess {
    background: rgba(16, 185, 129, 0.1) !important;
    border: 1px solid rgba(16, 185, 129, 0.2) !important;
    border-radius: var(--radius) !important;
    color: var(--success) !important;
    font-family: 'Inter', sans-serif !important;
}

.stInfo {
    background: rgba(59, 130, 246, 0.1) !important;
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    border-radius: var(--radius) !important;
    color: var(--text-primary);
    font-family: 'Inter', sans-serif !important;
}

/* Spinner */
.stSpinner {
    text-align: center !important;
}

.stSpinner > div {
    border-color: var(--primary-color) !important;
}

/* Expander */
.stExpander {
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    background: var(--surface) !important;
}

.stExpander > div > div {
    color: var(--text-secondary) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
}

/* Status Indicators */
.status-indicator {
    display: inline-flex;
    align-items: center;
    padding: 0.5rem 1rem;
    border-radius: var(--radius);
    font-size: 0.875rem;
    font-weight: 500;
    margin-bottom: 1rem;
}

.status-success {
    background: rgba(16, 185, 129, 0.1);
    color: var(--success);
    border: 1px solid rgba(16, 185, 129, 0.2);
}

.status-processing {
    background: rgba(59, 130, 246, 0.1);
    color: var(--info);
    border: 1px solid rgba(59, 130, 246, 0.2);
}

/* Responsive Design */
@media (max-width: 768px) {
    .main > div {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    
    .app-title {
        font-size: 2rem;
    }
    
    .card {
        padding: 1.5rem;
    }
}

/* Clean scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: var(--background);
}

::-webkit-scrollbar-thumb {
    background: var(--border);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--secondary-color);
}
</style>
""", unsafe_allow_html=True)

# 🏠 Header Section
st.markdown("""
<div class="app-header">
    <h1 class="app-title">🤖 Agentic RAG System</h1>
    <p class="app-subtitle">       </p>
</div>
""", unsafe_allow_html=True)

# 📁 Upload Section
st.markdown("""
<div class="card">
    <div class="card-header">
        <svg class="card-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
        </svg>
        <h2 class="card-title">Document Upload</h2>
    </div>
    <p class="card-description">Upload your document to begin intelligent analysis and querying</p>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a file", type=["pdf", "pptx", "docx", "csv", "txt"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]
    temp_path = f"temp_upload.{file_type}"
    
    with st.spinner("Processing document..."):
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        ingestion_msg = MCPMessage(
            sender="UI",
            receiver="IngestionAgent",
            type="DOCUMENT_UPLOAD",
            trace_id="trace-001",
            payload={"file_path": temp_path, "file_type": file_type}
        )
        dispatcher.send_message(ingestion_msg)
    
    st.success(f"✅ Document '{uploaded_file.name}' successfully processed and indexed")

st.markdown("</div>", unsafe_allow_html=True)

# 💬 Query Section
st.markdown("""
<div class="card">
    <div class="card-header">
        <svg class="card-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
        </svg>
        <h2 class="card-title">Ask a Question</h2>
    </div>
    <p class="card-description">Enter your question about the uploaded document</p>
</div>
""", unsafe_allow_html=True)

query = st.text_input("Your question", placeholder="What would you like to know about the document?")

if query:
    if not uploaded_file:
        st.markdown("""
        <div style="color: black; background-color: #fff3cd; border-left: 6px solid #ffeeba; padding: 1em; border-radius: 4px;">
            ⚠️ Please upload a document before asking a question.
        </div>
        """, unsafe_allow_html=True)
    else:
        with st.spinner("Analyzing your question..."):
            retrieval_msg = MCPMessage(
                sender="UI",
                receiver="RetrievalAgent",
                type="QUERY_REQUEST",
                trace_id="trace-002",
                payload={"query": query}
            )
            dispatcher.send_message(retrieval_msg)

    
    # Display response
if "llm_response" in st.session_state:
    st.markdown("### 🎯 Response")
    st.markdown(f"""
    <div style="
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        color: black;
        font-size: 1rem;
        line-height: 1.6;
        overflow: visible;
        white-space: pre-wrap;
    ">
    {st.session_state["llm_response"]}
    </div>
    """, unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)

# 🔧 System Status
with st.expander("🔧 System Information"):
    st.markdown("""
    **System Status:**
    - Vector Store: Active (384 dimensions)
    - Supported Formats: PDF, PPTX, DOCX, CSV, TXT
    - Agents: Ingestion, Retrieval, LLM Response
    - Message Dispatcher: Running
    """)

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');

.footer-container {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 2.5rem 1rem;
    border-top: 3px solid #64748b;
    font-family: 'Inter', sans-serif;
    text-align: center;
    animation: slideFadeIn 1.3s ease-in-out both;
    border-radius: 1.5rem 1.5rem 0 0;
    color: #f1f5f9;
    box-shadow: 0 -8px 24px rgba(0,0,0,0.2);
}

.footer-text {
    font-size: 1.2rem;
    margin-bottom: 1.5rem;
    font-weight: 600;
    color: #e2e8f0;
    animation: floatUp 1.4s ease forwards;
}

.footer-links {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 2rem;
}

.footer-links a {
    color: #38bdf8;
    font-weight: 500;
    font-size: 1.05rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    text-decoration: none;
    position: relative;
    transition: all 0.4s ease;
    transform: translateY(0);
    animation: bounceIn 1s ease both;
}

.footer-links a:hover {
    color: #7dd3fc;
    transform: scale(1.1) rotate(-1deg);
    filter: drop-shadow(0 0 6px #38bdf8);
}

.footer-links i {
    font-size: 1.2rem;
    transition: transform 0.3s ease;
}

.footer-links a:hover i {
    transform: rotate(10deg) scale(1.3);
}

/* Keyframe Animations */
@keyframes slideFadeIn {
    0% {
        opacity: 0;
        transform: translateY(50px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes floatUp {
    0% {
        opacity: 0;
        transform: translateY(20px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes bounceIn {
    0% {
        transform: scale(0.8);
        opacity: 0;
    }
    60% {
        transform: scale(1.1);
        opacity: 1;
    }
    100% {
        transform: scale(1);
    }
}
</style>

<div class="footer-container">
    <div class="footer-text"> Developed by <b>Nikhil Sukthe</b></div>
    <div class="footer-links">
        <a href="https://nikhilsukthe.vercel.app/" target="_blank"><i class="fas fa-rocket"></i>Portfolio</a>
        <a href="http://www.linkedin.com/in/nikhilsukthe" target="_blank"><i class="fab fa-linkedin"></i>LinkedIn</a>
        <a href="https://github.com/Nikhils-G" target="_blank"><i class="fab fa-github"></i>GitHub</a>
        <a href="https://www.instagram.com/nikh6l/" target="_blank"><i class="fab fa-instagram"></i>Instagram</a>
    </div>
</div>
""", unsafe_allow_html=True)
