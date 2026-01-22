# Wild Rift Coach 🎮

An intelligent AI-powered coaching assistant for League of Legends: Wild Rift, leveraging **Retrieval-Augmented Generation (RAG)** and conversational memory to provide expert champion build recommendations and strategic advice through a modern web interface.

## 🌟 Features

- **AI-Powered Web Interface** - Interactive React-based chat for real-time coaching
- **FastAPI Backend** - High-performance RESTful API with automatic reload support
- **RAG (Retrieval-Augmented Generation)** - Intelligent document retrieval for accurate, context-aware champion recommendations
- **Conversation Memory** - Maintains chat history for coherent, multi-turn conversations
- **Champion Build Recommendations** - AI-generated builds, runes, and strategies
- **Groq LLM Integration** - Fast, accurate responses using LLaMA 3.1 models
- **FAISS Vector Store** - Efficient similarity search over game knowledge
- **Error Handling & Validation** - Robust input validation with helpful error messages
- **Multi-LLM Support** - Easily switch between different language models via configuration
- **Production Ready** - Pre-built frontend served directly by FastAPI

<div style="background-color: #f8f9fa; border-left: 4px solid #28a745; padding: 16px; margin: 20px 0; border-radius: 4px;">

### ✅ Project Status: Active Development

**This project is actively maintained.** The core RAG pipeline is stable and production-ready. The web interface is fully functional with both backend and frontend components.

</div>

## 🏗️ Project Structure

```
wildRiftCoach/
├── app.py                                  # FastAPI application
├── llm.py                                  # LLM chain with RAG & memory
├── conhecimento.md                         # Game knowledge base (Portuguese)
├── template.md                             # Custom RAG prompt template
├── modules/
│   ├── __init__.py
│   ├── config.py                          # Pydantic configuration management
│   ├── ingestion.py                       # Document ingestion & chunking
│   └── rag.py                             # FAISS vector store setup
├── frontend/
│   └── wildriftcoach_fe/                  # React + TypeScript web interface
│       ├── src/
│       │   ├── App.tsx                   # Main React component
│       │   ├── main.tsx
│       │   └── index.css
│       ├── package.json
│       ├── vite.config.ts
│       └── dist/                         # Built frontend (served by FastAPI)
└── assets/                                # Champion images and builds
```

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (async Python web framework)
- **LLM Framework**: LangChain with ConversationalRetrievalChain
- **Language Model**: Groq (LLaMA 3.1 70B versatile)
- **Vector Store**: FAISS with GPU/CPU support
- **Embeddings**: HuggingFace Sentence Transformers
- **Config**: Pydantic Settings with .env support
- **Server**: Uvicorn ASGI server

### Frontend
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite (next-generation bundler)
- **UI Library**: Ant Design components
- **Package Manager**: npm

## 📋 Prerequisites

- Python 3.12+
- Node.js 18+ (for frontend)
- GROQ API Key (free at https://console.groq.com)
- 4GB+ RAM recommended

## 🚀 Quick Start

### 1. Backend Setup

```bash
# Clone and navigate
git clone <repository-url>
cd wildRiftCoach

# Create virtual environment
python -m venv .venv_python3_12
source .venv_python3_12/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
GROQ_API_KEY=your_groq_api_key_here
PROJECT_NAME=Wild Rift Coach
MAX_TOKENS=150
MODEL_CHAT=llama-3.1-70b-versatile
MODEL_RAG=sentence-transformers/all-MiniLM-L6-v2
EOF
```

**Get your GROQ_API_KEY:**
1. Visit https://console.groq.com/keys
2. Sign up (free) or log in
3. Create an API key and paste into `.env`

### 2. Frontend Setup

```bash
cd frontend/wildriftcoach_fe

# Install dependencies
npm install

# Build for production (served by FastAPI)
npm run build
```

### 3. Run the Application

```bash
# From root directory with backend venv activated
fastapi dev app.py
```

Open browser: **http://localhost:8000/**

## 💻 Usage

### Web Interface
1. Enter a champion name (e.g., "Garen", "Ahri", "Teemo")
2. Click **Ask** button
3. Receive AI-generated build recommendations with runes, items, and strategies

### API Direct Access

```bash
curl -X POST http://localhost:8000/llm \
  -H "Content-Type: application/json" \
  -d '{"championName":"Garen"}'
```

**Response:**
```json
{
  "response": "Garen is a top lane melee fighter known for consistent damage output. Recommended build: Trinity Force, Black Cleaver, Dead Man's Plate..."
}
```

## � API Endpoints

### POST /llm
Champion build recommendation endpoint.

**Request Body:**
```json
{
  "championName": "string (required)"
}
```

**Success Response (200):**
```json
{
  "response": "Build recommendations and strategies..."
}
```

**Error Responses:**
- Empty champion name: `"Por favor, informe o nome de um campeão."`
- Processing error: `"Erro interno ao processar o conhecimento."`

## 📚 Architecture & Flow

```
┌─────────────────────────────────────────────────────────────┐
│                  Frontend (React/TypeScript)                 │
│                                                               │
│  User Input (Champion Name) → POST /llm → Display Response   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌──────────────────────────────────────────────────────────────┐
│              FastAPI Backend (app.py)                        │
│                                                               │
│  - Validates request body (Pydantic)                         │
│  - Calls llm.run_llm(championName)                           │
│  - Returns JSON response                                     │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
┌──────────────────────────────────────────────────────────────┐
│           LLM Chain Pipeline (llm.py)                        │
│                                                               │
│  1. Query Encoding                                           │
│     User query → HuggingFace embeddings                      │
│                                                               │
│  2. FAISS Retrieval                                          │
│     Vector similarity search → Top K relevant docs           │
│                                                               │
│  3. Context Assembly                                         │
│     Retrieved docs + conversation history                    │
│                                                               │
│  4. Prompt Generation                                        │
│     Custom template (template.md) + context                 │
│                                                               │
│  5. LLM Inference                                            │
│     Groq LLaMA 3.1 70B → Streaming response                  │
│                                                               │
│  6. Memory Update                                            │
│     ConversationBufferMemory stores Q&A                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ↓
                 Return Response JSON
```

### 1. Knowledge Base Processing
- **Ingestion** (`modules/ingestion.py`): Loads `conhecimento.md` with game knowledge
- **Chunking**: Splits text into 1000-char chunks with 100-char overlap
- **Embedding**: Converts to vectors using sentence-transformers
- **Storage**: Stored in FAISS vector index

### 2. Query Processing
- User prompt encoded to same vector space
- FAISS performs similarity search
- Top K (4) most relevant documents retrieved

### 3. Response Generation
- Retrieved docs + chat history assembled as context
- Custom prompt template structures instructions
- Groq LLM generates build recommendations
- Temperature=0 for focused, deterministic responses

### 4. Conversation Memory
- `ConversationBufferMemory` maintains chat history
- Enables context-aware follow-up questions
- Memory persists during server session

## 🔧 Configuration

### Environment Variables

| Variable | Description | Example | Required |
|----------|-------------|---------|----------|
| `GROQ_API_KEY` | Groq API authentication token | `gsk_xxxxx` | ✅ |
| `PROJECT_NAME` | Application display name | `Wild Rift Coach` | ❌ |
| `MAX_TOKENS` | Maximum response tokens | `150` | ❌ |
| `MODEL_CHAT` | Chat model ID | `llama-3.1-70b-versatile` | ✅ |
| `MODEL_RAG` | Embedding model | `sentence-transformers/all-MiniLM-L6-v2` | ✅ |

### Customization

**Update Game Knowledge:**
1. Edit `conhecimento.md` - add champion guides, strategies, item builds
2. Restart FastAPI - automatic re-indexing
3. Knowledge available in next query

**Modify Response Style:**
1. Edit `template.md` - change how LLM structures responses
2. Restart FastAPI
3. New template applies to next requests

**Change Models:**
- Groq models: `llama-3.1-70b-versatile`, `llama-3.1-8b-instant`, `mixtral-8x7b-32768`
- Embedding: Any HuggingFace sentence-transformer model

## 🐛 Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| 422 Validation Error | Wrong request format | Send `{"championName": "ChampionName"}` |
| GROQ API Error | Invalid or missing API key | Verify `.env` with key from console.groq.com |
| "Erro interno ao processar" | LLM chain failure | Check server logs, ensure .env vars are set |
| Slow first response | Embeddings compute on startup | Initial request takes 10-15s, subsequent faster |
| Build frontend missing | Didn't run npm build | Run `cd frontend/wildriftcoach_fe && npm run build` |

## 📦 Dependencies

### Key Python Packages
```
fastapi==0.109.0+
langchain==0.1.0+
langchain-groq==0.1.0+
langchain-community==0.0.20+
pydantic==2.0+
pydantic-settings==2.0+
python-dotenv==1.0+
faiss-cpu==1.7.0+
sentence-transformers==2.0+
```

### Frontend Packages
```
react==18.2.0+
typescript==5.0+
vite==5.0+
antd==5.0+
```

## 🚀 Production Deployment

### Backend
```bash
# Use production ASGI server
pip install gunicorn

# Run with Gunicorn
gunicorn app:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend
```bash
# Already included in dist/ folder built by Vite
# Served automatically by FastAPI StaticFiles mount
```

### Environment
- Deploy with production GROQ_API_KEY from paid tier for higher rate limits
- Consider using GPU FAISS if searching large knowledge bases: `pip install faiss-gpu`
- Monitor GROQ usage via https://console.groq.com/usage

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangChain Documentation](https://langchain.com/)
- [FAISS GitHub](https://github.com/facebookresearch/faiss)
- [Groq API Docs](https://console.groq.com/docs)
- [React Documentation](https://react.dev/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)

## 📞 Support

For issues, questions, or suggestions:
- Open a GitHub issue
- Check existing issues/discussions first

---

**Made with ❤️ for Wild Rift Players**

*Enhance your gameplay with AI-powered champion insights and build recommendations!*
