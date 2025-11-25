class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old.'
    
alice = Person("Alice", 30)
bob = Person("Bob", 25)

print(alice.introduce())
print(bob.introduce())