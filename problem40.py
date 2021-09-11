# d1 = 1
# d10 = 1
from operator import mul
from functools import reduce

if __name__ == '__main__':
  count = 0
  numbers = []

  for num in range(1, 1000000):
    
    length = len(str(num))
    new_count = count + length

    if count <= 100 <= new_count:
      digit = str(num)[100 - count - 1]
      numbers.append(int(digit))

    if count <= 1000 <= new_count:
      digit = str(num)[1000 - count - 1]
      numbers.append(int(digit))

    if count <= 10000 <= new_count:
      digit = str(num)[10000 - count - 1]
      numbers.append(int(digit))

    if count <= 100000 <= new_count:
      digit = str(num)[100000 - count - 1]
      numbers.append(int(digit))
      
    if count <= 1000000 <= new_count:
      digit = str(num)[1000000 - count - 1]
      numbers.append(int(digit))
    
    count = new_count
  # print(numbers)
  answer = reduce(mul, numbers)
  print(answer)
    