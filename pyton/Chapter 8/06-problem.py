# write a program to mine a log file and find out whether it contains 'python'

# with open('six.txt',"r")as f:
#     contane = f.read()
    
# if 'python' in contane :
#     print("python is present")
    
# else:
#     print("not present is python")
    
with open('six.txt', 'r') as f:
    content = f.read()

if 'python' in content:  
    print("The word 'python' is present in the file.")
  
else:
    print("The word 'python' is not present in the file.")