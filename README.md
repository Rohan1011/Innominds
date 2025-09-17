# Neo - AI Assistant with Persistent Memory

A conversational AI assistant built with the Agno framework that remembers conversations across sessions using either PostgreSQL or SQLite for persistent memory storage.

## 🌟 Features

- **Persistent Memory**: Remembers conversations across sessions
- **Flexible Database Support**: Primary PostgreSQL with SQLite fallback
- **Local LLM Integration**: Works with LM Studio hosting local models
- **Session Management**: Tracks conversation history and context
- **User-Friendly Interface**: Simple command-line chat interface
- **Error Handling**: Graceful fallbacks and error recovery

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- LM Studio running locally on port 1234
- PostgreSQL database (optional, falls back to SQLite)
- Required Python packages (see requirements.txt)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd innominds
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up LM Studio**
   - Install [LM Studio](https://lmstudio.ai/)
   - Load a model (e.g., DeepSeek R1 or Mistral 7B Instruct)
   - Start the local server on port 1234

4. **Database Setup (Optional)**
   
   **For PostgreSQL:**
   ```sql
   -- Connect to PostgreSQL and create database
   CREATE DATABASE agno_db;
   ```
   
   **For SQLite:** 
   - No setup required - database file will be created automatically

### Running the Assistant

```bash
# Run with PostgreSQL primary, SQLite fallback
python test_agno.py

# Run with SQLite only
python Manual_agno.py
```

## 📁 Project Structure

```
innominds/
├── Manual_agno.py      # SQLite-only version
├── test_agno.py        # Full version with PostgreSQL/SQLite
├── testing.py          # Database connection testing utility
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Configuration

### Database Configuration

The assistant supports two database backends:

**PostgreSQL (Primary)**
```python
db_url = "postgresql://postgres:pheo259f@localhost:5432/agno_db"
```

**SQLite (Fallback)**
```python
db_file = "agno_memories.db"
```

### LLM Configuration

```python
local_llm = OpenAIChat(
    id="deepseek/deepseek-r1-0528-qwen3-8b",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)
```

## 🎯 Usage Examples

### Basic Conversation
```
You: Hi, my name is Sarah
Neo: Hello Sarah! Nice to meet you. How can I help you today?

You: What's the weather like?
Neo: I don't have access to current weather data, but I can help you find weather information or discuss weather-related topics!
```

### Memory Persistence
The assistant remembers:
- Your name and personal details
- Previous conversation topics
- Preferences and context
- Session history (last 3 runs)

### Commands
- `exit` or `quit`: End the conversation
- `Ctrl+C`: Force quit with graceful shutdown

## 🛠️ Development

### Testing Database Connections

Use the testing utility to verify your database setup:

```bash
python testing.py
```

This will test various connection string formats and help diagnose connection issues.

### Key Components

1. **Agent Setup**: Configures the AI agent with memory and database
2. **Memory Manager**: Handles conversation persistence
3. **Database Layer**: Abstraction for PostgreSQL/SQLite
4. **LLM Integration**: Connects to local LM Studio instance

## 🐛 Troubleshooting

### Common Issues

**LM Studio Connection Failed**
- Ensure LM Studio is running on localhost:1234
- Check that a model is loaded and server is started
- Verify the model ID matches your loaded model

**Database Connection Failed**
- For PostgreSQL: Check connection string, database exists, and credentials
- For SQLite: Ensure write permissions in project directory
- Run `testing.py` to diagnose connection issues

**Memory Not Persisting**
- Verify database connection is successful
- Check that memory_manager is properly initialized
- Ensure user_id and session_id are set correctly

## 📝 Configuration Options

### Agent Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `user_id` | Unique user identifier | "rohan" |
| `session_id` | Session identifier | timestamp-based |
| `num_history_runs` | Number of previous conversations to include | 3 |
| `enable_user_memories` | Enable memory persistence | True |
| `add_memories_to_context` | Include memories in conversation context | True |

### Database Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `db_url` | PostgreSQL connection string | "postgresql://user:pass@host:port/db" |
| `db_file` | SQLite database file path | "agno_memories.db" |

## 🔒 Security Notes

- Database credentials are currently hardcoded for development
- Consider using environment variables for production deployments
- Ensure proper database permissions and access controls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source. Please check with your organization's licensing requirements.

## 🙏 Acknowledgments

- [Agno Framework](https://github.com/phidatahq/agno) for the AI agent architecture
- [LM Studio](https://lmstudio.ai/) for local LLM hosting
- PostgreSQL and SQLite for database persistence

---

**Made with ❤️ by the Innominds team**