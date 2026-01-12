import json

# from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings



embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


class RAGEngine:
    def __init__(self):
        self.db=self._load_knowledge()

    def _load_knowledge(self):
        with open("data/knowledge_base.json") as f:
            data=json.load(f)

        docs=[]

        for plan,details in data["plans"].items():
            docs.append(Document(page_content=f"{plan.upper()} PLAN:{details}"))

        for policy,value in data["policies"].items():
            docs.append(Document(page_content = f"{policy.upper()}: {value}"))
            
        return FAISS.from_documents(docs, embeddings)
    def query(self,question:str)->str:
        results=self.db.similarity_search(question,k=2)
        return "\n".join([doc.page_content for doc in results])
    
