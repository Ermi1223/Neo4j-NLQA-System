import os
import google.generativeai as genai

class GeminiAPIHelper:
    """
    Helper class to interact with the MML Gemini API for advanced NLP.
    """
    def __init__(self):
        # Ensure that the API key is loaded from the environment variables
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
        
        # Configure the API with the provided API key
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    def process_query(self, query: str) -> str:
        """
        Sends the user query to the Gemini API to generate content.
        :param query: The natural language query string.
        :return: Processed response text from the API.
        """
        response = self.model.generate_content(query)
        return response.text
