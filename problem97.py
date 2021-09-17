product = 1
for num in range(0, 7830457):
  product *= 2
  product %= 10 ** 10
product *= 28433
product %= 10 ** 10
print(product + 1)