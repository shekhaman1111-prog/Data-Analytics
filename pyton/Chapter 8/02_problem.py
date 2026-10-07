# ''' write a program to generate multiplication table from 2 to 20 and write it to the 
# diffrent files. place these files in a folder for a 13 - year old.'''

# def genrateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} x {i} = {n * i}\n"

# with open (f"table/table_ {n}", "w") as f:
#     f.write(table)
    
    

# for i range(2, 21):
#     genrateTable(i)

def generateTable (n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"

        with open (f"table/table_ {n}", "w") as f:
            f.write(table)





for i in range(2, 21):
    generateTable(i)