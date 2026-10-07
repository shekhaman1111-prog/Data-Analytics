# write a program to make a copy a text file "this.txt"
with open("six.txt","r") as f:
    contane =  f.read()
    
with open("copy_six.txt","w") as f:
    contane =  f.write()
    