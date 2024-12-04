import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("MML_GEMINI_API_KEY")

def translate_to_cypher(natural_language_query):
    response = openai.Completion.create(
        model="text-davinci-003",  # Use OpenAI's GPT model
        prompt=f"Convert this natural language query to a Cypher query: {natural_language_query}",
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

# Example usage
natural_query = "Find all movies directed by Christopher Nolan released after 2010."
cypher_query = translate_to_cypher(natural_query)
print(cypher_query)
