class Robot:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Robot. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("I am brilliant and loayl. I do whatever my boss says")

class Robot:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Robot. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("I am brilliant and loayl. I do whatever my boss says")

bot1 = Robot("Cypher", 1)
bot2 = Robot("Nova", 2)

for toy in (bot1, bot2):
    toy.make_sound()
    toy.info()
