# Instantiate Cache information
n = 10
cache = [None] * (n+1 )


def fib_dyn(n):
  # base
  if n == 0 or n ==1:
    return n
  # check cache
  if cache[n] != None:
    return cache[n]
  # keep seeting cache
  cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
  
  return cache[n]


def fib_iter(n):
  a,b = 0,1

  for i in range(n):
    a,b = b,a+b
    # print(a)
  return a


def fib_rec(n):
    # base case:
    if n == 0 or n ==1:
      return n

    else: 
      # print(n)
      return fib_rec(n-1) +fib_rec(n-2)
    # recursive case:
    

print(fib_rec(10))
print(fib_dyn(10))
print(cache)
print(fib_iter(10))