# RAG Marketing Agent

A Retrieval-Augmented Generation (RAG) agent built to provide intelligent marketing insights and recommendations based on your marketing documents and industry best practices.

## Overview

The RAG Marketing Agent combines the knowledge from your marketing materials with advanced language models to:

- Answer questions about marketing strategies and campaigns
- Provide insights based on your marketing documentation
- Ensure consistent and accurate messaging
- Support data-driven marketing decisions

## Features

- 📚 **Document Processing**: Automatically processes PDF and text files
- 🔍 **Semantic Search**: Finds the most relevant information for any query
- 🧠 **Context-Aware Responses**: Generates responses grounded in your marketing materials
- 🔄 **Easy Integration**: Can be integrated into larger agent orchestration systems

## Installation

### Prerequisites

- Python 3.8+
- OpenAI API key

### Setup

1. Clone this repository:
```bash
git clone https://github.com/GauravVarma-web/RAG-Marketing-Agent.git
cd RAG-Marketing-Agent
```

2. Run the setup script:
```bash
python setup.py
```

3. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

4. Add your marketing documents to the `marketing_docs` folder:
   - PDF files (.pdf)
   - Text files (.txt)

## Usage

1. Start the agent:
```bash
python rag_agent.py
```

2. Ask marketing-related questions:
```
Your question: What are our key marketing differentiators?
```

## Project Structure

```
RAG-Marketing-Agent/
├── marketing_docs/     # Your marketing document files
├── chroma_db/          # Vector database (created automatically)
├── .env                # Environment file for API keys
├── rag_actions.py      # Document processing and retrieval functions
├── rag_prompts.py      # System prompt for the RAG agent
├── rag_agent.py        # Main execution file
└── setup.py            # Setup script
```

## How It Works

1. **Document Processing**: The agent loads and processes documents from the `marketing_docs` folder.
2. **Chunking**: Documents are split into manageable chunks for embedding.
3. **Embedding**: Text chunks are converted into vector embeddings.
4. **Retrieval**: When a question is asked, the agent finds the most relevant chunks.
5. **Response Generation**: The agent uses the retrieved context to generate an accurate response.

## Integration

This RAG Marketing Agent can be integrated into a broader AI agent orchestration system, working alongside other specialized agents like:

- Travel planning agents
- Content workflow agents
- Analytics agents

See the `integration_example.py` file for integration guidelines.

## Customization

- Modify the system prompt in `rag_prompts.py` to specialize the agent for your needs
- Adjust chunking parameters in `rag_actions.py` for different document types
- Change the model used in `generate_response()` function for different capabilities

## License

MIT

## Author

Gaurav Varma - AI-First Marketer & Self-Taught Agent Builder
