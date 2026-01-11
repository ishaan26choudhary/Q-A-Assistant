def get_relevant_chunks(vectordb, query):
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    return retriever.invoke(query)

