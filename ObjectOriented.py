
class Dog(object):      # Parrent Class
    race = "Pitbull"    # Class Attribute
    def __init__(self, name, childs=0): # Constructor / Instantiator
        """ Variables inside this is called instance attributes """
        self.name = name
        # self.__childs = childs # Private attribute
    
    def sit(self):
        """ Class Method for both parrent and child class """
        print(self.name + " is sitting.")
    
    def bark(self):
        print(self.name + " is barking!! ")

    def __str__(self):  # String representation of the class
        return str(f"Name: {self.name}"
                   f"Race: {Dog.race}"
                   f"{self.sit()}"
                   f"{self.bark()}")


# Inheritance.
class Puppy(Dog):
    """ Child Class """
    def __init__(self, name):
        """ Constructor based on parrent class """
        super().__init__(name)
        # Dog().__childs += 1
    
    def bark(self):
        """ Polymorphism makes you able to customize a inherrited method"""
        print(self.name + " can't bark!.")


if __name__ == "__main__":
    snoopy = Dog("Snoopy")    # Instance of the Dog class.
    sniffy = Puppy("Sniffy")  # Instance of the Puppy class.

    print(snoopy)