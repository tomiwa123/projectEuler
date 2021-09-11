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
  
  def check_dict(x):
    first = current_factors[0]
    second = current_factors[1]
    third = current_factors[2]
    fourth = current_factors[3]
    
    return len(set(first)) == x and len(set(second)) == x and len(set(third)) == x and len(set(fourth)) == x

    # factors = current_factors[0] + current_factors[1]
    # factors = factors + current_factors[2]
    # factors = factors + current_factors[3]
    # # print(factors, set(factors))
    # return len(factors) == len(set(factors))
  
  def get_prime_factors(num):
    number = num
    factors = []

    while number > 1:
      for divisor in range(2, number + 1):
        if is_prime(divisor) and number % divisor == 0:
          number /= divisor
          factors.append(divisor)
          break
    # print(num, factors)
    return factors


    # factors = []
    # for divisor in range(1, num):
    #   if not is_prime(divisor):
    #     continue
    #   if num % divisor == 0:
    #       factors.append(divisor)
    #       if is_prime(num / divisor):
    #         factors.append(num / divisor)
    # print(num, factors)
    # return factors

  current_factors[0] = get_prime_factors(210)
  current_factors[1] = get_prime_factors(211)
  current_factors[2] = get_prime_factors(212)
  current_factors[3] = get_prime_factors(213)
  # if check_dict(3):
  #     print("check_dict works")
    
  # print(get_prime_factors(10))
  # print(get_prime_factors(11))
  # print(get_prime_factors(12))

  for num in range(60000,70000):
    update_dict(get_prime_factors(num))
    if check_dict(4):
      print(num-3)
      break

