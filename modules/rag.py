import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""  # Disable CUDA

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

class setup:
    def __init__(self,model_name:str, documents):
        self.model_name = model_name
        self.documents = documents
        
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        self.vectorstore = FAISS.from_documents(documents, self.embeddings)
        
    def run(self):
        return self.vectorstore.as_retriever()