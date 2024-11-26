from neo4j import GraphDatabase

class Neo4jHelper:
    """
    A helper class to manage the Neo4j connection and run Cypher queries.
    """

    def __init__(self, uri, user, password):
        """
        Initialize the Neo4jHelper instance and establish a connection.
        :param uri: Neo4j URI
        :param user: Username for Neo4j
        :param password: Password for Neo4j
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def run_query(self, query):
        """
        Execute a Cypher query and return the results as a list of records.
        :param query: The Cypher query string
        :return: Query results as a list
        """
        with self.driver.session() as session:
            # Materialize results as a list
            return list(session.run(query))

    def close(self):
        """
        Close the connection to the Neo4j database.
        """
        self.driver.close()
