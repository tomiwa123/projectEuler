if __name__ == '__main__':
  def is_prime(num):
    if num % 2 == 0 or num <= 1:
        return False
    for x in range(3, int(num ** 0.5) + 1):
        if num % x == 0:
            return False
    return True
  
  def num_from_list(my_list):
    result = 0
    length = len(my_list)
    for index, letter in enumerate(my_list):
      result += int(letter) * pow(10, length - index - 1)
    return result

  def get_versions(num):
    versions = []
    num_list = list(str(num))
    length = len(num_list)
    
    versions.append(num)
    for iter in range(1, length):
      versions.append(num_from_list(num_list[iter:]))
    for iter in range(1, length):
      versions.append(num_from_list(num_list[: (-iter)]))
    
    return list(set(versions))
  
  truncatable_primes = []
  for num in range(11, 100000):
    if not is_prime(num):
      continue
    versions = get_versions(num)

    validating = True
    while(validating):
      if len(versions) == 0:
        break
      if not is_prime(versions[0]):
        validating = False
        break
      versions.pop(0)
    
    if validating:
      truncatable_primes.append(num)
  
  print("The truncatable primes are:")
  print(truncatable_primes)
  print(len(truncatable_primes))

  