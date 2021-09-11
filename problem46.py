if __name__ == "__main__":
  def is_prime(num):
    if num % 2 == 0 or num <= 1:
      return False
    for x in range(3, int(num ** 0.5) + 1):
      if num % x == 0:
          return False
    return True

  primes = []

  for num in range (1, 10000):
    if num % 2 == 0:
      continue
    if is_prime(num):
      primes.append(num)
      continue

    found = False
    for prime in primes:
      leftover = num - prime
      leftover /= 2
      leftover = leftover ** 0.5
      if leftover == int(leftover):
        found = True
        break

    if not found:
      print(num)
