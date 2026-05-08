from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

def search_docs(query: str) -> str:
    try:
        results = vectordb.similarity_search(query, k=4)
        if not results:
            return ""
        return "\n\n".join([doc.page_content for doc in results])
    except Exception as e:
        print(f"RAG search error: {e}")
        return ""