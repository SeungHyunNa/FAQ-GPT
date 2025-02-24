from abc import ABC, abstractmethod

class DocLoaderInterface(ABC):
  @abstractmethod
  def load(self, file_path: str): 
    pass