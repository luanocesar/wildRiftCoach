# Wild Rift Coach 🎮

An intelligent AI-powered coaching assistant for gaming players, leveraging **Retrieval-Augmented Generation (RAG)** and conversational memory to provide expert game knowledge and strategic advice.

## 🌟 Features

- **AI-Powered Chat Interface** - Interactive conversations with an intelligent AI coach
- **RAG (Retrieval-Augmented Generation)** - Intelligent document retrieval to provide context-aware responses
- **Conversation Memory** - Maintains chat history for coherent, context-aware conversations
- **Game Knowledge Base** - Built-in knowledge about champion characters and game mechanics
- **Multi-LLM Support** - Easily switch between different language models via configuration
- **Modular Architecture** - Clean separation of concerns for easy maintenance and extension

<div style="background-color: #ffffff; border-left: 4px solid #d63031; padding: 16px; margin: 20px 0; border-radius: 4px; color: #2d3436;">

### ⚠️ Project Status: In Development

**This project is currently in development and not yet at beta stage.** Features, APIs, and documentation may change. Please use it for experimental purposes and be prepared for breaking changes.

</div>

## 🏗️ Project Structure

```
wildRiftCoach/
├── app.py                      # Main application entry point
├── rag_memory.py               # RAG setup with conversation memory
├── conhecimento.md             # Game knowledge base (Portuguese)
├── template.md                 # Prompt template for RAG
├── modules/
│   ├── __init__.py
│   ├── config.py              # Configuration management (Pydantic)
│   ├── ingestion.py           # Document ingestion and chunking
│   └── rag.py                 # RAG vector store setup (FAISS)
└── assets/                    # Game character images and builds
```

## 🛠️ Tech Stack

- **LLM Framework**: LangChain
- **Language Models**: Groq (llama-3.1-8b-instant)
- **Vector Store**: FAISS (Facebook AI Similarity Search)
- **Embeddings**: HuggingFace Embeddings
- **Config Management**: Pydantic Settings
- **Environment**: Python 3.x, dotenv

## 📋 Prerequisites

- Python 3.8+
- GROQ API Key
- HuggingFace library support

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd wildRiftCoach
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   PROJECT_NAME=Wild Rift Coach
   MAX_TOKENS=100
   MODEL_CHAT=llama-3.1-8b-instant
   MODEL_RAG=sentence-transformers/all-MiniLM-L6-v2
   ```

## 💻 Usage

### Basic Chat (No RAG)
```bash
python app.py
```
Start a simple conversation with the AI coach.

### Chat with RAG & Memory
```bash
python rag_memory.py
```
Launch the intelligent coach with game knowledge retrieval and conversation memory.

## 📚 How It Works

### 1. **Knowledge Ingestion**
The system reads `conhecimento.md` and splits it into manageable chunks using `RecursiveCharacterTextSplitter`.

### 2. **Vector Embedding**
Documents are converted to vector embeddings using HuggingFace embeddings and stored in FAISS for fast similarity search.

### 3. **Retrieval-Augmented Generation**
When you ask a question:
- The system retrieves relevant game knowledge from the vector store
- This context is combined with your question
- The LLM generates a response using the custom prompt template

### 4. **Conversation Memory**
`ConversationBufferMemory` maintains chat history, enabling the AI to reference previous messages for contextual responses.

## 🎯 Key Components

### `modules/config.py`
Manages application configuration using Pydantic for type-safe environment variable loading.

### `modules/ingestion.py`
Handles document loading from Markdown files and text chunking for optimal RAG performance.

### `modules/rag.py`
Sets up the FAISS vector store and retriever for document similarity search.

### `rag_memory.py`
Orchestrates the complete RAG pipeline with memory and LangChain's `ConversationalRetrievalChain`.

## 🎮 Knowledge Base

The `conhecimento.md` file contains game information about:
- **Jinx** - ADC champion with early-game critical damage
- **Olaf** - Jungle champion with temporary invulnerability ultimate
- **Reyna** - Valorant duelist with life-steal and invisibility mechanics

Feel free to expand this knowledge base with more champion details and game strategies!

## 🔧 Customization

### Add New Game Knowledge
Edit or expand `conhecimento.md` with additional champion information, strategies, and game tips.

### Modify Response Behavior
Update `template.md` to change how the AI formats its responses and uses the retrieved context.

### Change Language Models
Modify `MODEL_CHAT` and `MODEL_RAG` in your `.env` file to use different LLMs or embedding models.

## 📝 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GROQ_API_KEY` | Your Groq API authentication key | `gsk_...` |
| `PROJECT_NAME` | Application display name | `Wild Rift Coach` |
| `MAX_TOKENS` | Maximum tokens for model responses | `100` |
| `MODEL_CHAT` | Chat/conversation model | `llama-3.1-8b-instant` |
| `MODEL_RAG` | Embedding model for RAG | `sentence-transformers/all-MiniLM-L6-v2` |

## 🤝 Contributing

Feel free to submit issues and enhancement requests! Contributions are welcome.

## 📄 License

This project is open source and available under the MIT License.

## 🎓 Learning Resources

- [LangChain Documentation](https://langchain.com/)
- [FAISS Index](https://github.com/facebookresearch/faiss)
- [Groq API Documentation](https://groq.com/)

---

**Happy Coaching! 🚀** Enhance your gaming skills with AI-powered strategic insights.
