from langchain.vectorstores import Chroma
from app.interfaces.vector_store_interface import VectorStoreInterface
from app.interfaces.embedder_interface import EmbedderInterface

class ChromaVectorStore(VectorStoreInterface):
  def __init__(self, embedder: EmbedderInterface, documents):
    self.vector_store = Chroma.from_documents(documents, embedder.get_embedder())

  def add_documents(self, documents):
    self.vector_store.add_documents(documents)
    return self

  def as_retriever(self):
    return self.vector_store.as_retriever()

  def similarity_search(self, query: str, k: int = 4):
    return self.vector_store.similarity_search(query, k)
