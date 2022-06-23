# types of class

class student :

    # static variable
    school = 'MIPS'
   

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)


s1 = student(23,23,24)
s2 = student(21,24,45)

print(s1.avg())
