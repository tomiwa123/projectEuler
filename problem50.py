from ProjEulerTools import *

if __name__ == "__main__":
  primes = []
  longest_length = 0
  longest_primes = []
  longest_prime_sum = 0

  for num in range(2, 100000):
    if is_prime(num):
      primes.append(num)

  found = False
  for length in range(len(primes), 6, -1):
    if found:
      break

    for index in range(0, len(primes) - length):
      prime_sum = sum(primes[index : index+length])
      if prime_sum >= 1000 ** 2:
        break
      if is_prime(prime_sum):
        longest_length = length
        longest_primes = primes[index: index+length]
        longest_prime_sum = prime_sum
        found = True
        break
  
  print(longest_prime_sum, longest_primes[0], longest_primes[len(longest_primes) - 1], longest_length)