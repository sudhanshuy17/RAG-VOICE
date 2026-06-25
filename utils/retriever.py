from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def get_retriever():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        persist_directory="./db/chroma_db",
        embedding_function=embeddings
    )

    return vector_store.as_retriever(
        search_kwargs={"k": 3}
    )