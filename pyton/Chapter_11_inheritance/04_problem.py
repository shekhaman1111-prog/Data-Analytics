# write a program to takeout the length of vactor 
class vactor:
    
    
    def __init__(self,l):
        self.l = l
        
    def __len__(self):
        return len(self.l)
v1 = vactor({1,2,3,4,5})
print(len(v1))        