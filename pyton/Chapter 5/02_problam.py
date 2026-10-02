'''write program out whether a student has passed or failed
if it requires a total of 40% and at least 33% in each subject has passed of failed if it 
requires atotal of 40% and at least 33% in each subject to pass. assume 3 subject and
take marks as an input for the user.'''

marks1 = int(input("enter the maks1"))
marks2 = int(input("enter the maks2"))
marks3 = int(input("enter the maks3"))

total_precentage = (100*(marks1 + marks2 + marks3)/300)
 
if(total_precentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("your are pass",total_precentage)
    
else:
    print("your failed",total_precentage)

