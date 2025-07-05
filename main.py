# main.py
"""
Entry point for the EduChain MCP server assignment.
"""

import sys
import os
#from dotenv import load_dotenv  # Removed
from educhain_tools.generator import generate_mcqs, generate_lesson_plan

def main():
    # No need to load environment variables
    # load_dotenv()  # Removed
    
    # Check if API key is available (skip for now, handled in client)
    # if not os.getenv('OPENROUTER_API_KEY'):
    #     print("Error: OPENROUTER_API_KEY not found in environment variables.")
    #     print("Please make sure your .env file contains: OPENROUTER_API_KEY=your_api_key_here")
    #     return
    
    if len(sys.argv) < 3:
        print("Usage: python main.py [mcq|lesson] <topic> [num_questions]")
        return
    
    mode = sys.argv[1]
    topic = sys.argv[2]
    
    try:
        if mode == "mcq":
            num = int(sys.argv[3]) if len(sys.argv) > 3 else 5
            result = generate_mcqs(topic, num)
            print(result)
        elif mode == "lesson":
            result = generate_lesson_plan(topic)
            print(result)
        else:
            print("Unknown mode. Use 'mcq' or 'lesson'.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 