class computer():
    pass



# every time you create an object it is allocated to new space

# c1 = computer()
# c2 = computer()
# print(id(c1))
# print(id(c2))
#

# USE OF SELF --------

    def __init__(self):
        self.name = "piyush"
        self.age = 28

    def update(self):
        self.age = 27
    
    def comparing_the_objects(self, other):
        if self.age == other.age:
            return True
        else:
            return False
    

c1 = computer()
c2 = computer()

print(c1.name)
c1.name = "piyu"
print(c1.name)

c1.update()
print(c1.age)

if c2.comparing_the_objects(c1):
    print("thery are same")
else:
    print("they are not same")

