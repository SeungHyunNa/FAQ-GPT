from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from app.interfaces.embedder_interface import EmbedderInterface

class CachedEmbedder(EmbedderInterface):
  def __init__(self, embedder: EmbedderInterface, cache_dir: LocalFileStore): 
    self.embeddings = CacheBackedEmbeddings.from_bytes_store(embedder.get_embedder(), cache_dir)

  def get_embedder(self):
    return self.embeddings

  def embed_documents(self, documents):
    return self.embeddings.embed_documents(documents)
