from abc import ABC, abstractmethod

class ChatAIInteface(ABC):
    @abstractmethod
    def chat(self, message: str) -> str:
        pass
