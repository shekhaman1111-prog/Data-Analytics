# write a program using function to find gretest of three number.

def gretest_no(a, b, c):
    if a>=b and a>=c:
        return a
    elif  b>=a and b>=c:
        return b
    elif  c>=a and c>=b:
        return c
    
a = 5
b = 6
c = 10
 
print(gretest_no(a, b ,c))    
    