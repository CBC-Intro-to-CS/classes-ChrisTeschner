class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"Your name is {self.first_name} {self.last_name}, your age is {self.age}, and your gender is {self.gender}.")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}. I see you are {self.age} years old and you are a {self.gender}, I hope you have a great day.\n")

user1 = User("Chris", "Teschner", 16, "male")
user1.describe_user()
user1.greet_user()

user2 = User("Grace", "Everstay", 27, "female")
user2.describe_user()
user2.greet_user()

user3 = User("Stephen", "Matthews", 24, "male")
user3.describe_user()
user3.greet_user()
print("Chris")