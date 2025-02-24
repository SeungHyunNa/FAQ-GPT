from langchain.embeddings import OpenAIEmbeddings
from app.interfaces.embedder_interface import EmbedderInterface
from dotenv import load_dotenv
import os

class OpenAIEmbedder(EmbedderInterface):
  def __init__(self, model_name="text-embedding-3-small"):
    self.model_name = model_name
    load_dotenv()  # .env 파일을 로드하여 환경 변수 설정
    openai_api_key = os.getenv("OPENAI_API_KEY")
    self.embedder = OpenAIEmbeddings(model=self.model_name, openai_api_key=openai_api_key)

  def get_embedder(self):
    return self.embedder

  def embed_documents(self, documents): 
    return self.embedder.embed_documents(documents)
