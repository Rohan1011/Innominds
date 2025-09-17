# agno_sqlite_simple.py
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.memory import MemoryManager
from agno.db.sqlite import SqliteDb
import time

def create_agent():
    print("🚀 Setting up Agno Agent with SQLite...")
    
    # Connect to local LM Studio which hosts Mistral 7B Instruct and other models
    local_llm = OpenAIChat(
        id="deepseek/deepseek-r1-0528-qwen3-8b",
        base_url="http://localhost:1234/v1",
        api_key="lm-studio"
    )

    # using SQLite for memory storage
    db = SqliteDb(db_file="agno_memories.db")
    print("✅ SQLite database ready: agno_memories.db")

    
    memory_manager = MemoryManager(db=db)

    # Create agent
    agent = Agent(
        model=local_llm,
        instructions="You are a friendly AI assistant that remembers context across conversations. Your name is Neo. Be helpful and engaging.",
        memory_manager=memory_manager,
        enable_user_memories=True,
        add_memories_to_context=True,
        db=db,
        user_id="rohan",
        session_id=f"session_{int(time.time())}",
        add_history_to_context=True,
        num_history_runs=3
    )

    return agent

def main():
    print("🤖 Neo - Your AI Assistant with Memory")
    print("======================================")
    print("💾 Powered by SQLite Database")
    print("🎯 Remembers conversations across sessions")
    print("⏹️  Type 'exit' or 'quit' to end")
    print("======================================\n")
    agent = create_agent()
    print("Hello Rohan! I'm ready to help you. What would you like to talk about?\n")

    # Conversation loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ["exit", "quit"]:
                print("\nNeo: Goodbye! I'll remember our conversation. 👋")
                break
                
            if not user_input:
                continue
            
            # Process the input
            result = agent.run(user_input)
            print(f"Neo: {result.content}\n")
            
        except KeyboardInterrupt:
            print("\nNeo: Session ended. Conversation saved.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()