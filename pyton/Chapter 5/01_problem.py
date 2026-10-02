# write a program to find the gretest of foure numbers entered by the user.
a1 = int(input("enter a number 1: "))
a2= int(input("enter b number 2: "))
a3 = int(input("enter c number 3: "))
a4 = int(input("enter d number 4: "))

if (a1>a2 and a1>a3 and a1>a4):
    print("gratest number is a1:",a1)
    
elif (a2>a1 and a2>a3 and a2>a4):
    print("gratest number is a2:",a2)
    
elif (a3>a1 and a3>a2 and a3>a4):
    print("gratest number is a3:",a3 )
    
elif (a4>a1 and a4>a2 and a4>a3):
    print("gratest number is a4:",a4 )

