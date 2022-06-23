# === creating a class
# Classes are used to create user-defined data structures. Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.


# A class is a blueprint for how something should be defined. It doesn’t actually contain any data. The Dog class specifies that a name and an age are necessary for defining a dog, but it doesn’t contain the name or age of any specific dog.

# class dog :

#     def bark(self):
#         print("Dog is barking")
#     def running(self):
#         print("Dog  is running")


# While the class is the blueprint, an instance is an object that is built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old.


# === INSTANCE IN AN OBJECT

# dog1 = dog()
# dog1.bark()

# dog2 = dog()
# dog2.running()

# ======= The __init__() Function

# class computer():
# ///// basic idea of concept ////

#     def __init__(self):
#         print("init")
        

#     def config(Self):
#         print("i5 16GB  1TB")

# com1 = computer()
# com2 = computer()

# com1.config()
# com2.config()

#==== EXAMPLE OF INIT METHOD   

class computer:

    def __init__(Self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu, self.ram)

com1 = computer('i5', 16)
com2 = computer('ryzen5', 16)

com1.comfig()
com2.config()