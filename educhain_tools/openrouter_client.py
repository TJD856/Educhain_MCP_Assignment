import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class OpenRouterClient:
    def __init__(self):
        # Get API key from environment variables only
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables. Please set it in your .env file or environment.")
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key,
        )

    def simple_chat(self, prompt: str, model: str = "openai/gpt-3.5-turbo-0613"):
        completion = self.client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://github.com/your-username/educhain-mcp",  # Optional
                "X-Title": "EduChain MCP Server",  # Optional
            },
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    def generate_mcqs(self, topic: str, num: int = 5) -> dict:
        """Generate multiple-choice questions for a given topic"""
        prompt = f"""Generate {num} multiple-choice questions about {topic}. 
        Return the response in this exact JSON format:
        {{
            "questions": [
                {{
                    "question": "Question text here?",
                    "options": ["A", "B", "C", "D"],
                    "correct_answer": "A",
                    "explanation": "Explanation of why this is correct"
                }}
            ]
        }}
        
        Make sure the response is valid JSON only."""
        
        response = self.simple_chat(prompt)
        
        if "error" in response:
            return response
        
        try:
            # Extract the content from the response
            content = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # Try to parse as JSON
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                # If not valid JSON, return the raw content
                return {"raw_response": content, "parsed_response": response}
                
        except Exception as e:
            return {"error": f"Failed to parse response: {str(e)}", "raw_response": response}
    
    def generate_lesson_plan(self, topic: str) -> dict:
        """Generate a lesson plan for a given topic"""
        prompt = f"""Create a comprehensive lesson plan for {topic}. 
        Return the response in this exact JSON format:
        {{
            "title": "Lesson Title",
            "subject": "{topic}",
            "learning_objectives": ["Objective 1", "Objective 2", "Objective 3"],
            "main_topics": ["Topic 1", "Topic 2", "Topic 3"],
            "activities": [
                {{
                    "name": "Activity Name",
                    "description": "Activity description",
                    "duration": "10 minutes"
                }}
            ],
            "assessment": "How to assess student understanding",
            "materials_needed": ["Material 1", "Material 2"]
        }}
        
        Make sure the response is valid JSON only."""
        
        response = self.simple_chat(prompt)
        
        if "error" in response:
            return response
        
        try:
            # Extract the content from the response
            content = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # Try to parse as JSON
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                # If not valid JSON, return the raw content
                return {"raw_response": content, "parsed_response": response}
                
        except Exception as e:
            return {"error": f"Failed to parse response: {str(e)}", "raw_response": response} 