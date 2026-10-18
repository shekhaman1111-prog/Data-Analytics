# can you change the self - parameter inside a class to something else (say "harry")
# .try changeing self to "slf" or "harry" and see he effects.


class calcularor:
    def __init__(aman,n):
        aman.n = n
    
    def squre(aman):
        print(f"the squre of {aman.n*aman.n}")
    
    def cube(aman):
        print(f"the cube of {aman.n*aman.n*aman.n}")
            
    def squreroot(aman):
        print(f"the squreroot of {aman.n**1/2}")
        
        
    @staticmethod
    def hello ():
          print ("hello world")    
         
a= calcularor(4)
a.squre()
a.cube()
a.squreroot()
a. hello ()