class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.age}"

name = input("Enter your name: ")
age = input("Enter your age: ")
person = Person(name, age)

for i in range(10):
    print(person)