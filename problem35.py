import itertools

if __name__ == '__main__':
  def is_prime(num):
        if num % 2 == 0 or num <= 1:
            return False
        for x in range(3, int(num ** 0.5) + 1):
            if num % x == 0:
                return False
        return True
  
  def is_circular_prime(num):
    # Currently validates only permutable primes
    # circular prime cannot contain digits 2, 4, 6, 8, 5, 0
    string_num = str(num)
    for test_num in ['0', '2', '4', '5', '6', '8']:
      if test_num in string_num:
        return False

    if num in answers:
      return False

    list_of_permutations = list(itertools.permutations(list(string_num)))
    length = len(string_num)
    new_coprimes = []

    for permutation in list_of_permutations:
      number = 0
      for index, digit in enumerate(permutation):
        number += int(digit) * pow(10, length - index - 1)
      if not is_prime(number):
        return False
      new_coprimes.append(number)
    
    return new_coprimes
    # number contains only 1, 3, 7, 9

  # print(list(itertools.permutations([1, 2, 3])))
  answers = list()
  for num in range(1, 1000000):
    result = is_circular_prime(num)
    if result:
      answers = answers + result
  
  print(list(set(answers)))
