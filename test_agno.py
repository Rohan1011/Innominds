# agno_final_working.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory import MemoryManager
from agno.db.postgres import PostgresDb
from agno.db.sqlite import SqliteDb
import time
import logging

# Reduce verbose logging
logging.basicConfig(level=logging.ERROR)

def create_agent():
    print("🚀 Setting up Agno Agent with PostgreSQL...")
    
    # Connect to local LM Studio
    local_llm = OpenAIChat(
        id="deepseek/deepseek-r1-0528-qwen3-8b",
        base_url="http://localhost:1234/v1",
        api_key="lm-studio"
    )

    # Try PostgreSQL with the correct database name
    print("🔌 Connecting to PostgreSQL database 'agno_db'...")
    try:
        db_url = "postgresql://postgres:pheo259f@localhost:5432/agno_db"
        db = PostgresDb(db_url=db_url)
        print("✅ Connected to PostgreSQL database 'agno_db'!")
        db_type = "PostgreSQL"
        
    except Exception as e:
        print(f"❌ PostgreSQL connection failed: {e}")
        print("🔄 Falling back to SQLite...")
        
        try:
            db = SqliteDb(db_file="agno_backup.db")
            print("✅ Using SQLite database as backup")
            db_type = "SQLite"
        except Exception as e2:
            print(f"❌ SQLite failed: {e2}")
            print("⚠️  Running without database persistence")
            db = None
            db_type = "None"

    # Setup memory management
    if db:
        memory_manager = MemoryManager(db=db)
        print("💾 Memory persistence: ENABLED")
    else:
        memory_manager = None
        print("💾 Memory persistence: DISABLED")

    # Create agent
    agent = Agent(
        model=local_llm,
        instructions="You are a friendly AI assistant that remembers context across conversations. Your name is Neo. Be helpful and engaging.",
        memory_manager=memory_manager,
        enable_user_memories=True if memory_manager else False,
        add_memories_to_context=True if memory_manager else False,
        db=db,
        user_id="rohan",  # Using your name as user ID
        session_id=f"session_{int(time.time())}",
        add_history_to_context=True,
        num_history_runs=3
    )

    return agent, db_type

def main():
    print("🤖 Neo - Your AI Assistant with Memory")
    print("======================================")
    print("💾 Powered by PostgreSQL Database")
    print("🎯 Remembers conversations across sessions")
    print("⏹️  Type 'exit' or 'quit' to end")
    print("======================================\n")
    
    agent, db_type = create_agent()
    
    print(f"Database: {db_type}")
    print("Neo: Hello! I'm ready to help you. What would you like to talk about?\n")

    # Conversation loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ["exit", "quit"]:
                print("\nNeo: Goodbye Rohan! I'll remember our conversation for next time. 👋")
                break
                
            if not user_input:
                continue
            
            # Process the input
            result = agent.run(user_input)
            print(f"Neo: {result.content}\n")
            
        except KeyboardInterrupt:
            print("\nNeo: Session ended. Our conversation has been saved.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again or rephrase your question.")

if __name__ == "__main__":
    main()