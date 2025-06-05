from ..Entities.User import User


class UserRepository:

    def __init__(self):
        self.file_path = "Model/users.txt"
        try:
            file = open(self.file_path, "r")
        except FileNotFoundError:
            print("Info Archivo: No se encontro el archivo de usuarios, se creara uno nuevo")
            file = open(self.file_path, "x")
        finally:
            file.close()

    def get_users(self):
        users = []
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for row in lines:
                user_data = row.strip().split(",")
                if len(user_data) == 6 and int(user_data[5]) == 1:
                    user = User()
                    user.username = user_data[0]
                    user.password = user_data[1]
                    user.email = user_data[2]
                    user.name = user_data[3]
                    user.surname = user_data[4]
                    user.state = int(user_data[5])
                    users.append(user)
        return users

    def get_user(self, user):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
            for row in lines:
                user_data = row.strip().split(",")
                if (len(user_data) == 6 and user_data[0] == user.username and int(user_data[5]) == 1):
                    user = User()
                    user.username = user_data[0]
                    user.password = user_data[1]
                    user.email = user_data[2]
                    user.name = user_data[3]
                    user.surname = user_data[4]
                    user.state = int(user_data[5])
                    return user
        return None

    def add_user(self, user):
        with open(self.file_path, "a") as file:
            file.write(f"{user.username},{user.password},{user.email},{user.name},{user.surname},1\n")
    ########################################################################################################
    def update_user(self, user, new_state=1):
        
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        with open(self.file_path, "w") as file:
            for line in lines:
                user_data = line.strip().split(",")
                if (len(user_data) == 6 and user_data[0] == user.username and user_data[1] == user.password):
                    if new_state == 0:
                        line = f"{user.username},{user_data[1]},{user_data[2]},{user_data[3]},{user_data[4]},{new_state}\n"
                        #{contact_data[1]},{contact_data[2]},{contact_data[3]},{contact_data[4]},{new_state}\n"
                    else:
                        line = f"{user.username},{user.password},{user.email},{user.name},{user.surname},{new_state}\n"
                file.write(line)

    def delete_user(self, user):
        user.update_user(user, 0)
        
    
