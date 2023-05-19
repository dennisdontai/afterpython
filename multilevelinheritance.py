class employee:
    def task(self):#object
        print("Employs")

class Manager(employee):
    def role(self):
        print("Manages")

class Chef(Manager):
    def  info(self):
        print("Works at a hotel" )

c = Chef()
c.info()


