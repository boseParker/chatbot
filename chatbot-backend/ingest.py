import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


all_chunks= []

for filename in os.listdir("docs"):
    if filename.endswith(".pdf"):
        print(f"Loading: {filename}")
        loader = PyPDFLoader(f"docs/{filename}")
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(docs)
        all_chunks.extend(chunks)

        print(f" {len(chunks)} chunks from {filename}")

if not all_chunks:
    print("no chunks available")

else:
    print(f"\nTotal chunks: {len(all_chunks)}")
    print("Creating embeddings... (first time is slow)")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )    

    vectordb = Chroma.from_documents(
        documents = all_chunks,
        embedding = embeddings,
        persist_directory="chroma_db"
    )

    vectordb.persist()
    print("Done")    