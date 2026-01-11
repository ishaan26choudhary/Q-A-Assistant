from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def create_vector_store(chunks,persist_dir="data/chroma"):
    embeddings=OllamaEmbeddings(model="nomic-embed-text")
    vectordb=Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    vectordb.persist()
    return vectordb
