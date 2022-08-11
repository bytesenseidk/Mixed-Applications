class Login(object):
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
    
    def valid_user(self):
        valid = False
        with open("users.txt", "r") as file:
            text = file.readlines()
            for line in text:
                for user in line.split("\n"):
                    if self.username == user.split(",")[0] and self.password == user.split(",")[1]:
                        valid = True
        return valid    
        