# replace program 4 for a list of such word to be censored.


word = ["shivansh", "aman", "nabeel"]

with open("five.txt","r")as f:
    contane = f.read()
    
new_contane = contane

for w in word:
    new_contane = new_contane.replace(w,"****")

with open("five.txt","w") as f:
    f.write(new_contane)  