# chat/services.py
import openai
import markdown
from environs import Env

# Load environment variables
env = Env()
env.read_env()

# Initialize OpenAI client
client = openai.Client(api_key=env("OPENAI_API_KEY"))

def get_motivational_response(prompt):
    """Generate a motivational response using OpenAI with Markdown formatting."""
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a motivational coach who provides supportive and inspiring responses using rich formatting such as headings, bullet points, and bold text."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=300
        )

        # Convert Markdown to HTML
        formatted_response = markdown.markdown(response.choices[0].message.content.strip())
        return formatted_response

    except Exception as e:
        return f"<p style='color: red;'>Sorry, an error occurred: {str(e)}</p>"
