library = {(2,2): 1}

def check_library(n, b):
  if n < b or n == 0:
    return 0
  if n == b:
    return 1
  return library[(n, b)]

def calculate_permutations(n, b):
  distribute = n - b
  sum = 1
  for div in range(2, b+1):
    sum += check_library(distribute, div)
  
  library[(n, b)] = sum
  return sum

for num in range(2, 101):
  sum = 0
  for buckets in range(2, num + 1):
    sum += calculate_permutations(num, buckets)
  print(num, sum)