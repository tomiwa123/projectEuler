import math
from collections import Counter

if __name__ == '__main__':
  
  perimeters = dict()

  for a in range(1, 1000):
    for b in range(a, 1000):
      c = math.sqrt(pow(a, 2) + pow(b, 2))
      
      if int(c) != c:
        continue
      
      p = a + b + int(c)

      if p > 1000:
        continue
      
      if not perimeters.get(p):
        perimeters[p] = 1
      else:
        perimeters[p] += 1
  
  counter = Counter(perimeters)
  print(counter.most_common()[0])
