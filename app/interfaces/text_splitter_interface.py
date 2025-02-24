from abc import ABC, abstractmethod

class TextSplitterInterface(ABC):
  @abstractmethod
  def split_documents(self, documents): pass