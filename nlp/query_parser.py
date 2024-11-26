# nlp/query_parser.py

class QueryParser:
    def __init__(self):
        pass

    def parse(self, query):
        # Implement logic to parse the natural language query
        # For simplicity, let's assume it's just extracting the main keyword for now
        return query.lower().split(" ")[-1]  # Example: 'super_enhancer' from 'Find all nodes with super_enhancer label'
