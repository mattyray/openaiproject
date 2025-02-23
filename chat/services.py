# chat/services.py
import openai
from environs import Env

# Load environment variables
env = Env()
env.read_env()

# Initialize OpenAI client
client = openai.Client(api_key=env("OPENAI_API_KEY"))

def get_motivational_response(prompt):
    """Generate a motivational response using OpenAI."""
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a motivational coach who provides supportive and inspiring responses, drawing from real-life resilience stories."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, an error occurred: {str(e)}"
