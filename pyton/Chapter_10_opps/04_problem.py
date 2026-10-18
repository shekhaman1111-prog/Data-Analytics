# add a staric method in problem 2, to greet the user with hello.


class calcularor:
    def __init__(self,n):
        self.n = n
    
    def squre(self):
        print(f"the squre of {self.n*self.n}")
    
    def cube(self):
        print(f"the cube of {self.n*self.n*self.n}")
            
    def squreroot(self):
        print(f"the squreroot of {self.n**1/2}")
        
        
    @staticmethod
    def hello ():
          print ("hello world")    
         
a= calcularor(4)
a.squre()
a.cube()
a.squreroot()
a. hello ()
