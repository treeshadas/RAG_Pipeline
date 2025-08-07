from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS

# Step 1: Load PDF
loader = PyPDFLoader("data/banglaBook.pdf")
pages = loader.load()

# Step 2: Chunking
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(pages)

# Step 3: Embedding Model
embedding = SentenceTransformerEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")

# Step 4: Create FAISS vectorstore
db = FAISS.from_documents(docs, embedding)
db.save_local("vectorstore/bangla_faiss")

print("✅ FAISS Vectorstore তৈরি হয়েছে!")
