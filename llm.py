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

chat_llm = ChatGroq(
    temperature=0,
    model_name=settings.MODEL_CHAT,
    groq_api_key=settings.GROQ_API_KEY
    )

memory = ConversationBufferMemory(
    memory_key="chat_history", 
    return_messages=True
)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=chat_llm,
    retriever=rag_setup.run(),
    memory=memory,
    combine_docs_chain_kwargs={"prompt" : PROMPT}
)

async def run_llm(promptFromUser: str):
    try:
        resposta = qa_chain.invoke({"question": promptFromUser})
        answer = resposta.get('answer', "Não foi possível processar a resposta.")
        
        # Log para seu terminal de dev
        print(f"User: {promptFromUser} | Bot: {answer[:50]}...")
        
        return answer
    except Exception as e:
        print(f"Erro na Chain: {e}")
        return "Erro interno ao processar o conhecimento."