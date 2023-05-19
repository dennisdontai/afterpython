class Animal:
    alive = True
    def sleep(self):
        print("It is sleeeping")

    def eat(self):
        print("It is eating")

class Fish(Animal):
    def myfish(self):
        print("This is a fish")

fish = Fish()
fish.sleep()
fish.eat()
fish.myfish()




