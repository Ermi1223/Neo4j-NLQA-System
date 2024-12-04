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

# User input loop
while True:
    user_query = input("\nEnter your query (or type 'exit' to quit): ").strip()
    
    # Exit condition
    if user_query.lower() == 'exit':
        print("Exiting the application. Goodbye!")
        break
    
    try:
        # Parse the user's query
        parsed_query = query_parser.parse(user_query)
        
        # Translate the parsed query into Cypher
        cypher_query = translator.translate(parsed_query)
        
        # Run the Cypher query to fetch results
        result = neo4j_helper.run_query(cypher_query)
        records = list(result)  # Convert the results into a list

        # Display results
        if records:
            print("\nQuery Results:")
            for record in records:
                print(record)
        else:
            print("\nNo results found for your query.")

        # Process the query through Gemini for content generation
        processed_query = gemini_helper.process_query(user_query)
        if processed_query:
            print("\nGenerated Content from Gemini API:", processed_query)
    
    except Exception as e:
        print("\nAn error occurred while processing your query:", str(e))

# Close the Neo4j connection
neo4j_helper.close()
