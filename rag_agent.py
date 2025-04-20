# rag_agent.py
import os
from dotenv import load_dotenv
from rag_actions import load_documents, split_documents, create_vector_store, search_documents, generate_response
from rag_prompts import rag_system_prompt

# Load environment variables
load_dotenv()

def initialize_knowledge_base(docs_directory="./marketing_docs"):
    """Initialize the knowledge base from documents"""
    print("Loading documents...")
    documents = load_documents(docs_directory)
    
    print(f"Splitting {len(documents)} documents into chunks...")
    chunks = split_documents(documents)
    
    print(f"Creating vector store with {len(chunks)} chunks...")
    vector_store = create_vector_store(chunks)
    
    print("Knowledge base initialized successfully!")
    return vector_store

def run_rag_agent():
    """Run the RAG agent"""
    # Initialize the knowledge base
    vector_store = initialize_knowledge_base()
    
    print("\nB2B Marketing RAG Agent")
    print("Ask questions about SynWrite AI's marketing, strategy, competitors, and more.")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("\nYour question: ")
        if query.lower() == 'exit':
            break
        
        # Search for relevant documents
        print("Searching knowledge base...")
        results = search_documents(query, vector_store, top_k=3)
        
        # Generate response
        print("Generating response...")
        response = generate_response(query, results, rag_system_prompt)
        
        # Print response
        print("\nResponse:")
        print(response)

if __name__ == "__main__":
    run_rag_agent()