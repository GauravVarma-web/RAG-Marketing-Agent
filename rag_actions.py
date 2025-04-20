# rag_actions.py
import os
from langchain.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def load_documents(directory_path):
    """Load documents from a directory"""
    # Setup loaders for different file types
    pdf_loader = DirectoryLoader(directory_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    text_loader = DirectoryLoader(directory_path, glob="**/*.txt", loader_cls=TextLoader)
    
    # Load documents
    pdf_docs = pdf_loader.load()
    text_docs = text_loader.load()
    all_docs = pdf_docs + text_docs
    
    return all_docs

def split_documents(documents):
    """Split documents into chunks"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    
    chunks = text_splitter.split_documents(documents)
    return chunks

def create_vector_store(chunks):
    """Create a vector store from document chunks"""
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    return vector_store

def search_documents(query, vector_store, top_k=3):
    """Search for relevant document chunks"""
    results = vector_store.similarity_search(query, k=top_k)
    return results

def generate_response(query, context, system_prompt, model="gpt-3.5-turbo"):
    """Generate a response based on the query and context"""
    from openai import OpenAI
    import os
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"{system_prompt}\n\nContext:\n"
    
    # Add context from retrieved documents
    for i, doc in enumerate(context):
        prompt += f"\nDocument {i+1}:\n{doc.page_content}\nSource: {doc.metadata.get('source', 'Unknown')}\n"
    
    prompt += f"\nQuestion: {query}\n"
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query}
        ]
    )
    
    return response.choices[0].message.content