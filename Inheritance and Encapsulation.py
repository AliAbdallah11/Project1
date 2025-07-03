class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        print(f"name is {self.name}, email:{self.email}")
    def set_email(self, email):
        self.email = email