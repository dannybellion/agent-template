import os
import snowflake.connector
import logging
from typing import List, Dict, Any


# ------------------------------
# Snowflake Connection Details
# ------------------------------
ACCOUNT = "capitalontap.eu-west-1"
DATABASE = "COT_DATABASE"
WAREHOUSE = "KUBERNETES_WAREHOUSE"
SCHEMA = "ANALYTICS"
ROLE = "KUBERNETES"
AUTHENTICATOR = "externalbrowser"

logger = logging.getLogger(__name__)


class SnowflakeConnection:
    _instance = None
    _connection = None

    def __new__(cls, database: str = DATABASE):
        if cls._instance is None:
            logger.info("Creating new SnowflakeConnection instance")
            cls._instance = super(SnowflakeConnection, cls).__new__(cls)
            cls._instance._initialize_connection(database)
        return cls._instance

    def _initialize_connection(self, database: str = DATABASE):
        """
        Initialize connection parameters for Snowflake.
        The actual connection will be created on first use.
        """
        logger.info("Initializing Snowflake connection parameters...")
        self.conn_params = {
            "user": os.getenv("SNOWFLAKE_USER_SHARED"),
            "account": ACCOUNT,
            "database": database,
            "schema": SCHEMA,
            "warehouse": WAREHOUSE,
            "role": ROLE,
            "authenticator": AUTHENTICATOR,
        }
        # Don't connect immediately, wait until needed
        self._connection = None

    def _create_connection(self):
        """Create and return a new Snowflake connection"""
        logger.info("Creating new Snowflake connection")
        return snowflake.connector.connect(**self.conn_params)

    def _is_connection_valid(self):
        """Check if the connection is still valid"""
        if self._connection is None:
            return False

        try:
            # Try a simple query to test the connection
            cursor = self._connection.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
            return True
        except Exception as e:
            logger.warning(f"Connection validation failed: {e}")
            return False

    @property
    def conn(self):
        """Return the existing connection or create a new one if needed"""
        if self._connection is None or not self._is_connection_valid():
            self._connection = self._create_connection()
        return self._connection

    def fetch_query(
        self,
        query: str,
    ) -> List[Dict[str, Any]]:
        """
        Execute a SQL query and return results.

        Args:
            query: The SQL query to execute

        Returns:
            List of dictionaries representing the query results
            dict if single_row=True
        """
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            if cursor.description:
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                data = [dict(zip(columns, row)) for row in rows]

            return data
        finally:
            cursor.close()
