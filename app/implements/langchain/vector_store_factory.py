from app.interfaces.embedder_interface import EmbedderInterface
from app.interfaces.vector_store_interface import VectorStoreInterface
from app.implements.langchain.vector_store_type import VectorStoreType
from app.implements.langchain.faiss_vector_store import FAISSVectorStore
from app.implements.langchain.chroma_vector_store import ChromaVectorStore
from app.implements.langchain.supabase_vector_store import SupabaseVectorStore

class VectorStoreFactory:
  @staticmethod
  def create_vector_store(vector_store_type: VectorStoreType, embedder: EmbedderInterface, documents) -> VectorStoreInterface:
    if vector_store_type == VectorStoreType.FAISS:
      return FAISSVectorStore(embedder, documents)
    elif vector_store_type == VectorStoreType.CHROMA:
      return ChromaVectorStore(embedder, documents)
    elif vector_store_type == VectorStoreType.SUPABASE:
      return SupabaseVectorStore(embedder, documents)
    else:
      raise ValueError(f"Unsupported vector store type: {vector_store_type}")
