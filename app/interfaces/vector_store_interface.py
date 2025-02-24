from abc import ABC, abstractmethod

class VectorStoreInterface(ABC):
  @abstractmethod
  def add_documents(self, documents): pass

  @abstractmethod
  def as_retriever(self): pass

  @abstractmethod
  def similarity_search(self, query: str, k: int = 4): pass
  