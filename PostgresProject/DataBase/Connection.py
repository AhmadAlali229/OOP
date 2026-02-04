import psycopg2


class DatabaseConnection:
    def __init__(self, host, port, db_name, user, password):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        """Establish connection to PostgreSQL"""
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.db_name,
            user=self.user,
            password=self.password
        )
        print("Database connected successfully")

    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("Database connection closed")
