from langchain.document_loaders import PDFPlumberLoader, TextLoader,BSHTMLLoader, UnstructuredWordDocumentLoader, UnstructuredMarkdownLoader
from app.interfaces.doc_loader_interface import DocLoaderInterface

class LangchainLoader(DocLoaderInterface):
  
  def load(self, file_path: str):
    if file_path.endswith(".pdf"):
      return PDFPlumberLoader(file_path).load()
    elif file_path.endswith(".txt"):
      return TextLoader(file_path).load()
    elif file_path.endswith(".html"):
      return BSHTMLLoader(file_path).load()
    elif file_path.endswith(".docx"):
      return UnstructuredWordDocumentLoader(file_path).load()
    elif file_path.endswith(".md"):
      return UnstructuredMarkdownLoader(file_path).load()
    else:
      raise ValueError(f"Unsupported file type: {file_path}")



