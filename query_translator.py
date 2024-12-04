class QueryTranslator:
    def __init__(self, neo4j_helper):
        self.neo4j_helper = neo4j_helper

    def translate(self, parsed_query):
        # Extracting entity and action type from parsed query
        action = parsed_query.get("action", "MATCH")
        entity = parsed_query.get("entity", None)
        properties = parsed_query.get("properties", None)

        # Example of more complex handling
        if action == "MATCH" and entity:
            if properties:
                # Add filter for properties if available
                conditions = " AND ".join([f"n.{key} = '{value}'" for key, value in properties.items()])
                return f"MATCH (n:{entity}) WHERE {conditions} RETURN n"
            return f"MATCH (n:{entity}) RETURN n"
        
        elif action == "CREATE" and entity and properties:
            properties_str = ", ".join([f"{key}: '{value}'" for key, value in properties.items()])
            return f"CREATE (n:{entity} {{ {properties_str} }}) RETURN n"
        
        elif action == "DELETE" and entity:
            return f"MATCH (n:{entity}) DELETE n"
        
        elif action == "UPDATE" and entity and properties:
            set_clause = ", ".join([f"n.{key} = '{value}'" for key, value in properties.items()])
            return f"MATCH (n:{entity}) SET {set_clause} RETURN n"

        else:
            return "Invalid query format"
