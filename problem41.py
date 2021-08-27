from itertools import permutations

if __name__ == "__main__":

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

  def find_largest_pandigital_prime():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for num in range(9, 3, -1):
      pan_digits = set(digits[:num])
      pandigitals = list(permutations(pan_digits))

      for tupl in pandigitals:
        num_from_tupl = num_from_list(tupl)
        if is_prime(num_from_tupl):
          print(num_from_tupl)
          return

  find_largest_pandigital_prime()