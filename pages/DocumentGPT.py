import streamlit as st
from app.implements.langchain.langchain_loader import LangchainLoader
from app.implements.langchain.langchain_splitter import LangchainSplitter
from app.implements.langchain.vector_store_factory import VectorStoreFactory
from app.implements.langchain.cached_embedder import CachedEmbedder
from app.implements.langchain.local_cache_directory import LocalCacheDirectory
from app.implements.langchain.openai_embedder import OpenAIEmbedder
from app.implements.langchain.vector_store_type import VectorStoreType
from app.implements.langchain.chat_faq import ChatFAQ
st.set_page_config(
    page_title="DocumentGPT",
    page_icon="📃",
)

chat_faq = ChatFAQ()

@st.cache_resource(show_spinner="Embedding file...")
def embed_file(file):
  file_content = file.read()  
  file_path = f"./.cache/files/{file.name}"
  with open(file_path, "wb") as f:
    f.write(file_content)

  # 문서 로드
  loader = LangchainLoader()
  docs = loader.load(file_path)

  # 문서 분할
  splitter = LangchainSplitter()
  docs = splitter.split_documents(docs)

  # 캐시 디렉토리 설정
  cache_dir = LocalCacheDirectory.get_store(file.name)

  # embeddings
  embeddings = CachedEmbedder(OpenAIEmbedder(), cache_dir)

  # 벡터 스토어 생성
  vectorstore = VectorStoreFactory.create_vector_store(VectorStoreType.FAISS, embeddings, docs)
  retriever = vectorstore.as_retriever()

  return retriever

def send_message(message, role, save=True):
    with st.chat_message(role):
        st.markdown(message)
    if save:
        st.session_state["messages"].append({"message": message, "role": role})


def paint_history():
    for message in st.session_state["messages"]:
        send_message(
            message["message"],
            message["role"],
            save=False,
        )

st.title("DocumentGPT")

st.markdown("""
Welcome to DocumentGPT!

This is a tool that allows you to ask questions about your documents.

To get started, please upload a document below.
""")

with st.sidebar:
    file = st.file_uploader(
        "Upload a .txt .pdf or .docx file",
        type=["pdf", "txt", "docx"],
    )

if file:
  retriever = embed_file(file)

  send_message("I'm ready! Ask away!", "ai", save=False)
  paint_history()
  message = st.chat_input("Ask anything about your file...")
  if message:
    send_message(message, "human")

    answer = chat_faq.chat(retriever, message)
    send_message(answer, "ai")
else:
  st.session_state["messages"] = []

