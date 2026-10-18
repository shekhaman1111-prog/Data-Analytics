
# creat a class with a class attribute a; creat an object from it set 'a'
# directly using object.a = o. does this change the class attribute 

class demo:
    a =4
    
O = demo()
print(O.a)
O.a = 0 
print(O.a)
print(demo.a)