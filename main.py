from nlp.query_parser import QueryParser

def main():
    print("Welcome to the Neo4j Natural Language Query System with Gemini API!")
    parser = QueryParser()

    try:
        while True:
            user_query = input("\nEnter your query (or type 'exit' to quit): ")
            if user_query.lower() == 'exit':
                print("Goodbye!")
                break

            try:
                cypher_query = parser.parse_to_cypher(user_query)
                print(f"\nExecuting Cypher query:\n{cypher_query}\n")
                records = db.run_query(cypher_query)
                for record in records:
                    print(record)
            except Exception as e:
                print(f"Error: {e}")

    finally:
        db.close()
        print("Neo4j connection closed.")
