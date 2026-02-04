from PostgresProject.DataBase.Connection import DatabaseConnection
from PostgresProject.DataBase.User_Repo import UserRepository
import os

if __name__ == "__main__":
    db = DatabaseConnection(
        host="localhost",
        port=5432,
        db_name="training_db",
        user="postgres",
        password= os.getenv("PASSWORD")
    )

    db.connect()

    user_repo = UserRepository(db)

    user_repo.add_user("Khalid", "Khalid@test.com", 19)

    users = user_repo.get_all_users()
    for user in users:
        print(user)

    db.close()
