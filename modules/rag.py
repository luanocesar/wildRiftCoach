from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

class setup:
    def __init__(self,model_name:str, documents):
        self.model_name = model_name
        self.documents = documents
        
        self.embeddings = GoogleGenerativeAIEmbeddings(model_name="models/text-embedding-004")
        
        self.vectorstore = FAISS.from_documents(documents, self.embeddings)
        
    def run(self):
        return self.vectorstore.as_retriever()