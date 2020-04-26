def gen():
  for x in range(3):
    yield x

g = gen()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))

s = 'Hello'
for let in s:
  print(let)

# print(next(s))

s_iter = iter(s)
print(next(s_iter))
