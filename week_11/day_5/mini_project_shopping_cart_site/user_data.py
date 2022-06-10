import json

user_file = 'users.json'


def add_user(new_user, filename='users.json'):
    with open(filename) as file:
        data_users = json.load(file)
        data_users.append(new_user)
    with open(filename, "w") as json_file:
        json.dump(data_users, json_file, indent=2)


def check_user(user, password, filename="users.json"):
    with open(filename) as file:
        data_users = json.load(file)
        for item in data_users:
            print(item["Username"])
            if item["Username"] == user and item["Password"] == password:
                return True
        return False


# user = {"Username": "test", "Password": "1223"}
# add_user(user)

# print(check_user(user="user1", password="qwerty"))


