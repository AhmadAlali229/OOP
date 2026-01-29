import self
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        print("IDK what I SAY")
class cat(Pet):
    def speak(self):
        print("Meow")

class dog(Pet):
    def speak(self):
        print("Bark")

P1= Pet("Pepper",1)
P1.show()
P1.speak()
C= cat("Cat",2)
C.speak()
d=dog("Dog",3)
d.speak()
