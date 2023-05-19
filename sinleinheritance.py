class Animal:
    age = 3
    def speak(self):
        print("speaking")
class Dog(Animal):
    def eat(self):
        print("eating")

d = Dog()
d.eat()
d.speak()

print(issubclass(Dog,Animal))
print(isinstance(d,Dog))




