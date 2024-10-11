from storage import Storage

class User:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id
    
    def get_details(self):
        return {
            "name": self._name,
            "user_id": self._user_id
        }


# for user management adding or lsiting users
class UserManager:

    def __init__(self, storage_file = 'users.csv'):
        self.storage_file = storage_file
        self.storage = Storage()
        self.headers = ['name', 'user_id']
        self.users = self.load_users()

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user.get_details())
        self.storage.save_data(self.storage_file, [user.get_details()], self.headers, append=True)
        return "User added succesfully."
    
    def list_user(self):
        for user in self.users:
            print(user)

    def load_users(self):
        return self.storage.load_data(self.storage_file, self.headers)