class UserRepository:
    def __init__(self, database):
        self.collection = database["users"]

    def add_user(self, name, age, email):
        user = {
            "name": name,
            "age": age,
            "email": email
        }
        self.collection.insert_one(user)

    def get_all_users(self):
        return list(self.collection.find())

    def update_user_age(self, name, new_age):
        self.collection.update_one(
            {"name": name},
            {"$set": {"age": new_age}}
        )

    def delete_user(self, name):
        self.collection.delete_one({"name": name})
