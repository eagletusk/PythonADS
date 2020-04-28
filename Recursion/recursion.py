# Recursion

def fact(n):
  #  base classmethod
  if n ==0 :
    return 1
  else:
    return n*fact(n-1)

print(fact(54))
