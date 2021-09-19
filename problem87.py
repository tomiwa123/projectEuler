from ProjEulerTools import is_prime

primes = []
for num in range(2, 10000):
  if is_prime(num):
    primes.append(num)

triples = [False] * 50000000

for a in primes:
  for b in primes:
    for c in primes:
      power_triple = a ** 2 + b ** 3 + c ** 4
      if power_triple < 50000000:
        triples[power_triple] = True
      else:
        break

found_count = 0
for term in triples:
  if term:
    found_count += 1

print(found_count)