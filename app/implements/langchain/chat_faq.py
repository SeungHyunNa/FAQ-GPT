from app.interfaces.chat_ai_interface import ChatAIInteface
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain_core.vectorstores.base import VectorStoreRetriever

class ChatFAQ(ChatAIInteface):
    def __init__(self):
      self.prompt = ChatPromptTemplate.from_messages(
        [
          (
            "system",
            """
            Answer the question using ONLY the following context. If you don't know the answer just say you don't know. DON'T make anything up.
            And Please answer according to the language of the human question, not the context
            
            Context: {context}
            """,
          ),
          ("human", "{question}"),
        ]
      )
      self.llm = ChatOpenAI(temperature=0.1)

    def format_docs(self, docs):
      return "\n\n".join(document.page_content for document in docs)

    def chat(self, retriever: VectorStoreRetriever, message: str) -> str:
      chain = ({"context": retriever | RunnableLambda(self.format_docs), "question": RunnablePassthrough()} | self.prompt | self.llm)        
      response = chain.invoke(message)
      return response.content
