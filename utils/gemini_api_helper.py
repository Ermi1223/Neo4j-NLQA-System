import os
import requests

class GeminiAPIHelper:
    """
    Helper class to interact with the MML Gemini API for advanced NLP.
    """
    def __init__(self):
        self.api_key = os.getenv("MML_GEMINI_API_KEY")
        self.endpoint = "https://mml.googleapis.com/v1/query"  # Placeholder endpoint

    def process_query(self, query: str) -> dict:
        """
        Sends the user query to MML Gemini API and returns the processed response.
        :param query: Natural language query string.
        :return: Processed response from the API.
        """
        if not self.api_key:
            raise ValueError("MML_GEMINI_API_KEY is not set in the environment variables.")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "query": query,
            "context": "Neo4j knowledge graph query translation"
        }

        response = requests.post(self.endpoint, json=payload, headers=headers)
        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code} - {response.text}")

        return response.json()
