class Employee:
    def __init__(self,first,last,email,pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay

class Developer(Employee):
    pass

e2 = Developer("kumar","saw","ks@gmail.com",50000)
print(help(Developer))