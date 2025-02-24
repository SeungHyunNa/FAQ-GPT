from abc import ABC, abstractmethod

class EmbedderInterface(ABC):
  @abstractmethod
  def get_embedder(self): pass

  @abstractmethod
  def embed_documents(self, documents) : pass
  