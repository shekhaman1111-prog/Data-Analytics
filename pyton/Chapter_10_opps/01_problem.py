# creat a class "programmer" for storing information of few programmers
# working at microsoft.

# class program:
#     company = "microsoft"

#     def __init__ (self, name, salery, pin):
#         self.mane = name
#         self.salery = salery
#         self.pin = pin
     
# self = program("aman",10000, 482004)

# print (self.name)
# print (self.salery)
# print (self.pin)
# print (self.company)

class program:
    compny = "microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

self = program("shivansh", 5000, 1234)

print(self.name)
print(self.salary)
print (self.pin)
print(self.compny)