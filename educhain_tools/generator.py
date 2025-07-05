import os
import json
#from dotenv import load_dotenv  # Removed
from .openrouter_client import OpenRouterClient

# No need to load environment variables here

# Initialize the OpenRouter client
try:
    client = OpenRouterClient()
except ValueError as e:
    print(f"Error: {e}")
    client = None

def generate_mcqs(topic: str, num: int = 5):
    """
    Generate multiple-choice questions (MCQs) for a given topic.
    Returns the result as a string.
    """
    if not client:
        return json.dumps({"error": "OpenRouter client not initialized"})
    prompt = f"""Generate {num} multiple-choice questions about {topic}. 
Return the response in this exact JSON format:
{{
  \"questions\": [
    {{
      \"question\": \"Question text here?\",
      \"options\": [\"A\", \"B\", \"C\", \"D\"],
      \"correct_answer\": \"A\",
      \"explanation\": \"Explanation of why this is correct\"
    }}
  ]
}}
Make sure the response is valid JSON only."""
    try:
        result = client.simple_chat(prompt)
        return result
    except Exception as e:
        return json.dumps({"error": f"Failed to generate MCQs: {str(e)}"})

def generate_lesson_plan(topic: str):
    """
    Generate a lesson plan for a given topic.
    Returns the result as a string.
    """
    if not client:
        return json.dumps({"error": "OpenRouter client not initialized"})
    prompt = f"""Create a comprehensive lesson plan for {topic}. 
Return the response in this exact JSON format:
{{
  \"title\": \"Lesson Title\",
  \"subject\": \"{topic}\",
  \"learning_objectives\": [\"Objective 1\", \"Objective 2\", \"Objective 3\"],
  \"main_topics\": [\"Topic 1\", \"Topic 2\", \"Topic 3\"],
  \"activities\": [
    {{
      \"name\": \"Activity Name\",
      \"description\": \"Activity description\",
      \"duration\": \"10 minutes\"
    }}
  ],
  \"assessment\": \"How to assess student understanding\",
  \"materials_needed\": [\"Material 1\", \"Material 2\"]
}}
Make sure the response is valid JSON only."""
    try:
        result = client.simple_chat(prompt)
        return result
    except Exception as e:
        return json.dumps({"error": f"Failed to generate lesson plan: {str(e)}"}) 