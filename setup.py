# setup_rag.py
import os
import subprocess

def setup_environment():
    """Set up the environment for the RAG agent"""
    # Create directories
    os.makedirs("marketing_docs", exist_ok=True)
    
    # Install required packages
    packages = [
        "langchain",
        "openai",
        "chromadb",
        "tiktoken",
        "pypdf",
        "python-dotenv"
    ]
    
    print("Installing required packages...")
    for package in packages:
        subprocess.run(["pip", "install", package])
    
    print("Creating .env file for API key...")
    with open(".env", "w") as f:
        f.write("OPENAI_API_KEY=your_api_key_here\n")
    
    print("\nSetup complete!")
    print("1. Place your marketing documents in the 'marketing_docs' folder")
    print("2. Update the OPENAI_API_KEY in the .env file")
    print("3. Run 'python rag_agent.py' to start the agent")

if __name__ == "__main__":
    setup_environment()