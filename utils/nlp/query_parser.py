from utils.gemini_api_helper import GeminiAPIHelper

class QueryParser:
    """
    Class to parse natural language queries into Cypher queries using Gemini API.
    """
    def __init__(self):
        self.gemini_helper = GeminiAPIHelper()

    def parse_to_cypher(self, natural_language_query: str) -> str:
        """
        Translate a natural language query into a Cypher query using Gemini API.
        :param natural_language_query: The user's query in natural language.
        :return: A Cypher query string.
        """
        print("Processing query with Gemini API...")
        response = self.gemini_helper.process_query(natural_language_query)

        # Assume the API returns a field "cypher_query" in the response
        cypher_query = response.get("cypher_query")
        if not cypher_query:
            raise ValueError("Gemini API failed to return a Cypher query.")
        
        return cypher_query
