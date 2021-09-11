import math

if __name__ == '__main__':

  def is_prime(num):
    if num % 2 == 0 or num <= 1:
      return False
    for x in range(3, int(num ** 0.5) + 1):
      if num % x == 0:
          return False
    return True

  current_factors = dict()
  def update_dict():
    current_factors[0] = current_factors[1]
    current_factors[1] = current_factors[2]
    current_factors[2] = current_factors[3]
    current_factors[3] = current_factors[3] + 1
  
  def get_prime_factors(num):
    factors = []
    for divisor in range(1, int(math.floor(num ** 0.5)) + 1):
      if not is_prime(divisor):
        continue
      if num % divisor == 0:
          factors.append(divisor)
    return factors
  

