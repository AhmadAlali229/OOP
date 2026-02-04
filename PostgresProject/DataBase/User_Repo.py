class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_users(self):
        cursor = self.db_connection.connection.cursor()
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        cursor.close()
        return users

    def add_user(self, name, email, age):
        cursor = self.db_connection.connection.cursor()
        cursor.execute(
            """
            INSERT INTO users (name, email, age)
            VALUES (%s, %s, %s)
            """,
            (name, email, age)
        )
        self.db_connection.connection.commit()
        cursor.close()
