import os
from dotenv import load_dotenv
from utils.neo4j_helper import Neo4jHelper

# Load environment variables from the .env file
load_dotenv()

# Retrieve Neo4j credentials from environment variables
neo4j_uri = os.getenv("NEO4J_URI")
neo4j_user = os.getenv("NEO4J_USERNAME")
neo4j_password = os.getenv("NEO4J_PASSWORD")

# Initialize the Neo4j helper
db = Neo4jHelper(neo4j_uri, neo4j_user, neo4j_password)

# Test the connection by running a query
try:
    print("Testing Neo4j connection...")
    result = db.run_query("MATCH (n) RETURN n LIMIT 5")
    # Convert result to a list to avoid ResultConsumedError
    records = list(result)
    for record in records:
        print(record)
finally:
    # Close the connection
    db.close()
    print("Neo4j connection closed.")
