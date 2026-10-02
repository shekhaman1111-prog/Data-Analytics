# write a python function to print first n line of the foloowing pattern:
def  patten (n):
  if n == 0:
      return 0
  print("*" *n)
  patten (n-1)
  
patten(5)
