from dotenv import load_dotenv
import os
from utils.neo4j_helper import Neo4jHelper
from utils.gemini_api_helper import GeminiAPIHelper
from nlp.query_parser import QueryParser
from query_translator import QueryTranslator

# Load environment variables from .env
load_dotenv()

# Get values from environment variables
uri = os.getenv("NEO4J_URI")
user = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

# Ensure that the environment variables are loaded correctly
if not uri or not user or not password:
    raise ValueError("Neo4j credentials are not set correctly in the .env file.")

# Initialize components
query_parser = QueryParser()
neo4j_helper = Neo4jHelper(uri=uri, user=user, password=password)
translator = QueryTranslator(neo4j_helper)
gemini_helper = GeminiAPIHelper()  # Initialize Gemini API helper

# Example usage: Get a natural language query from the user and process it
user_query = "5 nodes from the graph that are labeled as gene"
parsed_query = query_parser.parse(user_query)
cypher_query = translator.translate(parsed_query)

# Running the query to fetch relevant results
result = neo4j_helper.run_query(cypher_query)

# Fetch the results all at once into a list to avoid consuming it multiple times
records = list(result)  # Converting the result into a list before any iteration

# Now you can safely iterate through the results
for record in records:
    print(record)

# After querying the graph, you can process the query through Gemini for content generation
processed_query = gemini_helper.process_query(user_query)
print("Generated Content from Gemini API: ", processed_query)

# Close the Neo4j connection
neo4j_helper.close()
