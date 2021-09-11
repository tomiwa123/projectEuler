import math

if __name__ == '__main__':

  def is_prime(num):
    if num in {2, 3}:
      return True
    if num <= 1:
      return False
    for x in range(2, int(num ** 0.5) + 1):
      if num % x == 0:
          return False
    return True

  current_factors = dict()
  def update_dict(factors):
    current_factors[0] = current_factors[1]
    current_factors[1] = current_factors[2]
    current_factors[2] = current_factors[3]
    current_factors[3] = factors
    # print(current_factors)
  
  def check_dict():
    factors = current_factors[0] + current_factors[1]
    factors = factors + current_factors[2]
    factors = factors + current_factors[3]
    print(factors, set(factors))
    return len(factors) == len(set(factors))
  
  def get_prime_factors(num):
    factors = []
    for divisor in range(1, num):
      if not is_prime(divisor):
        continue
      if num % divisor == 0:
          factors.append(divisor)
          if is_prime(num / divisor):
            factors.append(num / divisor)
    print(num, factors)
    return factors

  current_factors[0] = get_prime_factors(644)
  current_factors[1] = get_prime_factors(645)
  current_factors[2] = get_prime_factors(646)
  current_factors[3] = get_prime_factors(647)
  if check_dict():
      print("check_dict works")

  # for num in range(648, 10000):
  #   update_dict(get_prime_factors(num))
  #   if check_dict():
  #     print(num-4)
  #     break

