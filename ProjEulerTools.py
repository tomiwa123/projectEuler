def is_prime(num):
  if num in {2, 3}:
    return True
  if num <= 1:
    return False
  for x in range(2, int(num ** 0.5) + 1):
    if num % x == 0:
        return False
  return True

def num_from_list(my_list):
  result = 0
  length = len(my_list)
  for index, letter in enumerate(my_list):
    result += int(letter) * pow(10, length - index - 1)
  return result