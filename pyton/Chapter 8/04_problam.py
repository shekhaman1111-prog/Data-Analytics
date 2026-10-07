# a file contains a word "Donkey" multiple times. you need to write a program which
# replace this word with #### by updating the same file.

word = "Doncky"

with open("file.txt","r")as f:
    contane = f.read()
    
new_contane = contane.replace(word,"****")

with open("file.txt","w") as f:
    f.write(new_contane)  