# this file load pdf, chunk pdf, generate emeddings, store in chromadb

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from utils.ocr_loader import extract_text_from_pdf


def create_vector_store():

    print("Loading PDF...")

    documents = extract_text_from_pdf()

    print("\nCreating chunks...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=400
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Total chunks created: {len(chunks)}")

    print("\nLoading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("\nCreating ChromaDB...")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./db/chroma_db"
    )

    print("✅ Vector Store Created Successfully")

    return vector_store