# Types of Methods

#      Variables ( which depicts certain properties of an object ) and
    #    Methods ( represents a set of behaviour of an object ).

    
# ===============1. Instance methods =================
#   The purpose of instance methods is to set or get details about instances (objects), and that is why they’re known as instance methods. They are the most common type of methods used in a Python class.

                # they are of two types : 1. Accessor methods ==> also known as GETTERS(getters only fetch the value)
                 #                        2. Mutator methods ===> also known as SETTERs (Setters only set the value)




class student:
    school = 'MIPS'
   

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)
        # accssor method
    def get_m1(self):
        return self.m1
        # mutator method
    def set_m1(self,value):
        self.m1 = value

s1 = student(23,23,24)
s2 = student(21,24,45)


print(s1.avg())

# 2. ================= CLASS METHODS===========
# The purpose of the class methods is to set or get the details (status) of the class. That is why they are known as class methods. They can’t access or modify specific instance data. 
# 
# They are bound to the class instead of their objects. Two important things about class methods:

    #1. In order to define a class method, you have to specify that it is a class method with the help of the @classmethod decorator
    # 2. Class methods also take one default parameter- cls, which points to the class. Again, this not mandatory to name the default parameter “cls”. But it is always better to go with the conventions



class student:
    school = 'MIPS'
    area = 'GZB'
   

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)
        # accssor method
    def get_m1(self):
        return self.m1
        # mutator method
    def set_m1(self,value):
        self.m1 = value

    # class method
    @classmethod

    def info(cls):
        print(cls.school)
        print(cls.area)

print(student.info())


# ============== STATIC CLASS METHODS==================

# Static methods cannot access the class data. In other words, they do not need to access the class data. They are self-sufficient and can work on their own.  Since they are not attached to any class attribute, they cannot get or set the instance state or class state.

class student:
    school = 'MIPS'
    area = 'GZB'
   

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)
        # accssor method
    def get_m1(self):
        return self.m1
        # mutator method
    def set_m1(self,value):
        self.m1 = value

    # class method
    @classmethod

    def info(cls):
        print(cls.school)
        print(cls.area)
    
    # static method

    @staticmethod
    def info():
        print("This is a student class.. and static method")

print(student.info())
