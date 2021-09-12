
a = 1
b = 2
count = 0

for iter in range(1, 1000):
  if len(str(a + b)) > len(str(b)):
    count += 1
  new_a = b
  new_b = 2*b + a
  a = new_a
  b = new_b
print(count)