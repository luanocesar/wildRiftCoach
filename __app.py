from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model_name="llama-3.1-8b-instant")

def main():
    print("-- Oraculo Groq Conectado")
    pergunta = input("Pergunta: ")
    
    try:
        resposta = llm.invoke(pergunta)
        print(f"\nGroq: {resposta.content}")
    except Exception as e:
        print(f"Falha : {e}")
    
if __name__ == "__main__":
    main()