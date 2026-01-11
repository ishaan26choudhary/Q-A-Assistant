import streamlit as st
from ingest import load_and_split_pdf
from embeddings import create_vector_store
from retriever import get_relevant_chunks
from qa_chain import answer_question
st.set_page_config(page_title="Document Q&A Assistant")
st.title("Document Q&A Assistant")
# Uploading PDF
uploaded_file = st.file_uploader("Uploading the PDF",type="pdf")
if uploaded_file:
    with open("Blimp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    st.success("PDF uploaded successfully")
    # Processing document
    with st.spinner("Processing document..."):
        chunks=load_and_split_pdf("Blimp.pdf")
        vectordb = create_vector_store(chunks)
    st.success("Document indexed. You can now ask questions.")
    # Asking questions
    question=st.text_input("Ask me about Airship: ")
    if question:
        docs=get_relevant_chunks(vectordb, question)
        if not docs:
            st.warning(
                "I cannot find the answer to that question in the provided document."
            )
        else:
            context="\n\n".join(d.page_content for d in docs)
            answer = answer_question(context, question)
            st.markdown("### Answer")
            st.write(answer)
