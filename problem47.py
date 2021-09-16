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

  current_factors = list()

  def check_list(x):
    length = len(current_factors) - 1
    for num in range(length, length - x, -1):
      if current_factors[num] != x:
        return False
    return True

  def count_prime_factors(num):
    if is_prime(num):
      current_factors.append(1)
      return 1
    count = 0
    for divisor in range(2, num + 1):
      if is_prime(divisor) and num % divisor == 0:
        factor_count = current_factors[num / divisor]
        if (num / divisor) % divisor == 0:
          current_factors.append(factor_count)
          count = factor_count
        else:
          current_factors.append(factor_count + 1)
          count = factor_count + 1
        break
    return count

  current_factors.append(0)
  current_factors.append(1)
  current_factors.append(1)
  current_factors.append(1)

  for num in range(4, 1000000):
    count_prime_factors(num)
    if check_list(4):
      print(num-3)
      break

