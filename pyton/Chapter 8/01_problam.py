'''write a program to read the text from a given file 'poem.txt' and find out whether it 
contains the word 'twinkle'. '''

f = open("poem.txt","r")
contain = f.read()

if "twinkle" in contain:
    print("the word is twinkle in a present in the poem ")

else:
    print("the word is twinkle is not  present in the poem ")

f.close()
