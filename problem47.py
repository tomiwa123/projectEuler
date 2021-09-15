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

  # current_factors = dict()
  current_factors = list()

  # def update_dict(factors):
  #   current_factors[0] = current_factors[1]
  #   current_factors[1] = current_factors[2]
  #   current_factors[2] = current_factors[3]
  #   current_factors[3] = factors
    # print(current_factors)
  
  # def check_dict(x):
  #   first = current_factors[0]
  #   second = current_factors[1]
  #   third = current_factors[2]
  #   fourth = current_factors[3]
    
  #   return len(set(first)) == x and len(set(second)) == x and len(set(third)) == x and len(set(fourth)) == x
  #   # return len(set(second)) == x and len(set(third)) == x and len(set(fourth)) == x
  
  def check_list(x):
    length = len(current_factors) - 1
    for num in range(length, length - x):
      if current_factors[num] != x:
        return False
    return True

  # def get_prime_factors(num):
  #   number = num
  #   factors = []

  #   while number > 1:
  #     for divisor in range(2, number + 1):
  #       if is_prime(divisor) and number % divisor == 0:
  #         number /= divisor
  #         factors.append(divisor)
  #         break
  #   # print(num, factors)
  #   return factors

  def count_prime_factors(num):
    count = 0
    for divisor in range(2, num + 1):
      if is_prime(divisor) and num % divisor == 0:
        if num == divisor:
          current_factors.append(1)
          return 1
        factor_count = current_factors[num / divisor]
        if (num / divisor) % divisor == 0:
          current_factors.append(factor_count)
          count = factor_count
        else:
          current_factors.append(factor_count + 1)
          count = factor_count + 1
        break
    return count

  # current_factors[0] = get_prime_factors(210)
  # current_factors[1] = get_prime_factors(211)
  # current_factors[2] = get_prime_factors(212)
  # current_factors[3] = get_prime_factors(213)
  current_factors.append(0)
  current_factors.append(1)

  for num in range(2, 1000):
    count_prime_factors(num)
    if check_list(3):
      # print(current_factors)
      print(num-2)
      break

