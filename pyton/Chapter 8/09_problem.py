# write a program to find out whether a file is identical & matchs the contant of 
# another file.

with open ("five.txt","r") as f:
    contant1 = f.read()
    

with open ("six.txt","r") as f:
    contant6 = f.read()
    
    if contant1 == contant6 :
        print("the contant file are same")
        
    else:
        print("the contant file are 'Not' same")
        