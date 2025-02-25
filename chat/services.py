# chat/services.py
from openai import OpenAI
import markdown
from environs import Env

# ✅ Load environment variables
env = Env()
env.read_env()

# ✅ Initialize OpenAI client
client = OpenAI(api_key=env.str("OPENAI_API_KEY"))  # <-- Use env.str to ensure it's a string

def get_motivational_response(prompt):
    """Generate a motivational response using OpenAI with Markdown formatting."""
    try:
        # ✅ Generate motivational response using OpenAI
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a motivational coach who provides supportive and inspiring responses using rich formatting such as headings, bullet points, and bold text."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=300
        )

        # ✅ Convert Markdown to HTML (safe for rendering)
        formatted_response = markdown.markdown(response.choices[0].message.content.strip())
        return formatted_response

    except Exception as e:
        return f"<p style='color: red;'>Sorry, an error occurred: {str(e)}</p>"


# ✅ Set OpenAI API key correctly


def get_motivational_response(prompt):
    """Generate a motivational response using OpenAI with Markdown formatting."""
    try:
        # ✅ Correct OpenAI Chat Completion call (1.0.0+)
        response = client.chat.completions.create(model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a motivational coach who provides supportive and inspiring responses using rich formatting such as headings, bullet points, and bold text."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=300)

        # ✅ Convert Markdown to HTML (safe for rendering)
        formatted_response = markdown.markdown(response.choices[0].message.content.strip())
        return formatted_response

    except Exception as e:
        return f"<p style='color: red;'>Sorry, an error occurred: {str(e)}</p>"
