class Dog:
    # initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # attributes unique to each dog class instance
    def bark(self):
        return f"{self.name} can bark"


dog1 = Dog("AX1", 4)
dog2 = Dog("AY2", 3)

print(dog1.bark())