import os
from langchain.storage import LocalFileStore

class LocalCacheDirectory:
    @staticmethod
    def get_store(file_name: str, base_path: str = "./.cache/embeddings"):
        return LocalFileStore(f"{base_path}/{file_name}")