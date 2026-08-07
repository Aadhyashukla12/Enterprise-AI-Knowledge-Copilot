from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


# ======================================
# Embedding Model
# ======================================

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)


# ======================================
# Create FAISS Vector Database
# ======================================

def create_vector_store(chunks, filename):

    metadatas = []

    for i in range(len(chunks)):
        metadatas.append({
            "source": filename,
            "chunk": i + 1
        })

    vector_db = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model,
        metadatas=metadatas
    )

    vector_db.save_local("faiss_index")

    return vector_db


# ======================================
# Load Existing FAISS Database
# ======================================

def load_vector_store():

    vector_db = FAISS.load_local(

        "faiss_index",

        embedding_model,

        allow_dangerous_deserialization=True

    )

    return vector_db