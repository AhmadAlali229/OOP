from mongo_connection import MongoDBConnection
from user_repository import UserRepository


if __name__ == "__main__":
    mongo_db = MongoDBConnection(
        uri="mongodb://localhost:27017",
        db_name="training_db"
    )

    mongo_db.connect()

    user_repo = UserRepository(mongo_db.database)

    # CREATE
    user_repo.add_user("Manal", 22, "Manal@test.com")

    # READ
    users = user_repo.get_all_users()
    for user in users:
        print(user)

    # UPDATE
    #user_repo.update_user_age("Ahmad", 26)

    # DELETE
    #user_repo.delete_user("Ahmad")

    mongo_db.close()
