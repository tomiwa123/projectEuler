from ProjEulerTools import *

current = 1
step = 2

a = 0
b = 1

while b < 10 * a or current < 30:
# while current <  49:
  for _ in range(4):
    current += step
    b += 1
    if is_prime(current):
      # print(current)
      a += 1
  step += 2
print(step-1, a, b)