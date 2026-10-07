# write a program to find out the line number where python is present from 
# ques 6. 
with open("six.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if "python" in line:
        print(f"word 'python' is present{lineno}. ")
        break
    lineno +=1
else:
    print("the word is not print in the python") 