# write a pythone program to rename a file is to "rename _by_python.txt".

with open ("five.txt","r") as f:
    contant1 = f.read()
    
with open ("rename_by_five.txt","w") as f:
    f.write(contant1)
    