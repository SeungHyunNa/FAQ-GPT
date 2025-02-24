from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.interfaces.text_splitter_interface import TextSplitterInterface

class LangchainSplitter(TextSplitterInterface):
  def __init__(self, chunk_size=500, chunk_overlap=50):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

  def split_documents(self, documents):  
    return self.splitter.split_documents(documents)
