from google.adk.agents import Agent
from typing import Optional, Dict, Any # For type hints

from .sophia_tools import get_library_books_list, get_book_by_isbn, get_authors_list, get_books_by_author_id


MODEL_GEMINI_2_0_FLASH = "gemini-2.0-flash"

def say_hello(name: Optional[str] = None) -> str:
    if name:
        greeting = f'Hello, {name}!'
    else:
        greeting = "Hello there!" # Default greeting if name is None or not explicitly passed
    
    sophia_description = " My name is Sophia, I'm your personal library agent. I will help you in all matters books!"
    return greeting + sophia_description

# --- Redefine Sub-Agents (Ensures they exist in this context) ---
greeting_agent = None
try:
    # Use a defined model constant
    greeting_agent = Agent(
        model=MODEL_GEMINI_2_0_FLASH,
        name="greeting_agent", # Keep original name for consistency
        instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting using the 'say_hello' tool. Do nothing else.",
        description="Handles simple greetings and hellos using the 'say_hello' tool.",
        tools=[say_hello],
    )
    print(f"✅ Sub-Agent '{greeting_agent.name}' redefined.")
except Exception as e:
    print(f"❌ Could not redefine Greeting agent. Check Model/API Key ({greeting_agent.model}). Error: {e}")


root_agent = Agent(
    name='sophia_library_agent',
    model=MODEL_GEMINI_2_0_FLASH,
    description='Main agent: tasked to help find and list books in a library',
    instruction='Your name is Sophia, you are the main agent.'
                'Your task is to help find and list books in a library.'
                'You can find an author id in the get_authors_list'
                'Auhtors and Books have id numbers that can be used to fetch futher information with other tools. Ex: get_books_by_author_id may use an author id to fetch a list of books by the author',
    tools=[get_library_books_list, get_book_by_isbn, get_books_by_author_id, get_authors_list],
    sub_agents=[greeting_agent]
)