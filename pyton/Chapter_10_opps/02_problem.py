# write a clas  "calculator" cable of finding square, cube and square root of a 
# number.

class calcularor:
    def __init__(self,n):
        self.n = n
    
    def squre(self):
        print(f"the squre of {self.n*self.n}")
    
    def cube(self):
        print(f"the cube of {self.n*self.n*self.n}")
            
    def squreroot(self):
        print(f"the squreroot of {self.n**1/2}")
         
         
a= calcularor(4)
a.squre()
a.cube()
a.squreroot()