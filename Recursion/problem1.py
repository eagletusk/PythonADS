def rec_sum(n):
  # cumlutive sum
  if n == 0:
    return 1
  else:
    print(n)
    return n + rec_sum(n-1)

print(rec_sum(11))