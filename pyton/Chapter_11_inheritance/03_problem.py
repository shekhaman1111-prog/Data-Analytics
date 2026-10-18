class Employee:
    salery = 300
    increment = 20
    @property
    def saleryafterincrement(self):
        return (self.salery + self.salery * (self.increment/100) )
    
    @saleryafterincrement.setter
    def saleryafterincrement (self,salery):
        self.increment = ((salery/self.salery) -1)*100 
    
    
    
e = Employee()
# print(e.saleryafterincrement)
e.saleryafterincrement = 360.0
print(e.increment)