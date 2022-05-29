class Step:
    def __init__(self,name = "name", age = 0):
        self.Username = name
        self.age = age
    def get_name(self):
        return self.Username
    def set_name(self,name):
        self.Username = name
user = Step()
print(user.get_name())
user.set_name("Tony")
print(user.get_name())
# print(user.Username)