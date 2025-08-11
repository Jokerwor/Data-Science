class Programmer:
    company = "Outlook"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("Jonas",150000,4561)
print(p.name,p.salary,p.pin)
p = Programmer("Martha",120000,3454)
print(p.name,p.salary,p.pin)
p = Programmer("Eva",90000,2754)
print(p.name,p.salary,p.pin)
p = Programmer("Adam",100000,6844)
print(p.name,p.salary,p.pin)