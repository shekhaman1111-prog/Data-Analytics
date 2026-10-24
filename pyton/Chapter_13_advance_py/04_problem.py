def devisable(n):
    if (n%5 == 0):
        return True
    return False
a = [ 10, 15, 20 , 55, 2365 ,654 ,24545]
f = list(filter(devisable, a))
print (f)