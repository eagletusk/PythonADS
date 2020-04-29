# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    
    pass

def fib_iter(n):
  a,b = 0,1

  for i in range(n):
    a,b = b,a+b
    # print(a)
  return a


def fib_rec(n):
    
    pass

print(fib_rec(10))
print(fib_dyn(10))
print(fib_iter(10))