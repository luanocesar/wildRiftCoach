import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.prompts import PromptTemplate
# App Modules
from modules import ingestion, rag
from modules import config

settings = config.Config()

fileIngestion = ingestion.fileIngestion('conhecimento.md')
documents = fileIngestion.getData()

def load_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
prompt_content = load_prompt("template.md")

PROMPT = PromptTemplate(
    template=prompt_content,
    input_variables=["context", "question"]
)

rag_setup = rag.setup(settings.MODEL_RAG, documents)

llm = ChatGroq(
    temperature=0,
    model_name=settings.MODEL_CHAT,
    groq_api_key=settings.GROQ_API_KEY
    )

memory = ConversationBufferMemory(
    memory_key="chat_history", 
    return_messages=True
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=rag_setup.run(),
    memory=memory,
    combine_docs_chain_kwargs={"prompt" : PROMPT}
)

def chat():
    print("--- Agente com Memória e RAG Ativo ---")
    while True:
        pergunta = input("\nVocê: ")
        if pergunta.lower() in ["sair", "exit"]: break
        
        resposta = qa_chain.invoke({"question": pergunta})
        print(f"IA: {resposta['answer']}")

if __name__ == "__main__":
    chat()