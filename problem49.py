from itertools import permutations

if __name__ == '__main__':

  def num_from_list(my_list):
    result = 0
    length = len(my_list)
    for index, letter in enumerate(my_list):
      result += int(letter) * pow(10, length - index - 1)
    return result

  def is_prime(num):
    if num % 2 == 0 or num <= 1:
      return False
    for x in range(3, int(num ** 0.5) + 1):
      if num % x == 0:
          return False
    return True

  primes = list()
  for num in range(1000, 10000):
    if not is_prime(num):
      continue
    primes.append(num)
  
  primes.sort()
  prime_dict = dict()

  for prime in primes:
    found = False
    for perm in prime_dict.keys():
      if set(str(prime)) == set(str(perm)):
        prime_dict[perm].append(prime)
        found = True
    if not found:
      prime_dict[prime] = [prime]
  
  for prime_key in prime_dict.keys():
    perm_primes = prime_dict[prime_key]
    if len(perm_primes) < 3:
      continue

    for val_1 in range(0, len(perm_primes) - 2):
      for val_2 in range(val_1 + 1, len(perm_primes) - 1):
        diff = perm_primes[val_2] - perm_primes[val_1]
        if perm_primes[val_2] + diff in perm_primes:
          print(perm_primes[val_1], perm_primes[val_2], perm_primes[val_2] + diff)
