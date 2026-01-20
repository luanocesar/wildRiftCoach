from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

class fileIngestion:
    def __init__(self,file_name):
        loader = UnstructuredMarkdownLoader(f"./{file_name}")
        data = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=100
        )
        self.documents = text_splitter.split_documents(data)
    
    def getData(self):
        return self.documents