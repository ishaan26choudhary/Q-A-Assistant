from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

PROMPT = """
You are a document-based assistant.
Answer ONLY using the provided context.

If the answer is not present in the context, say:
"I cannot find the answer to that question in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

def answer_question(context, question):
    llm = Ollama(model="mistral", temperature=0)

    prompt = PromptTemplate(
        template=PROMPT,
        input_variables=["context", "question"]
    )

    return llm.invoke(
        prompt.format(context=context, question=question)
    )

