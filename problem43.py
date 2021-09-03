from itertools import permutations

if __name__ == "__main__":

  def num_from_list(my_list):
    result = 0
    length = len(my_list)
    for index, letter in enumerate(my_list):
      result += int(letter) * pow(10, length - index - 1)
    return result
  
  def check_requirements(num):
    num_str = str(num)
    if int(num_str[1:4]) % 2 != 0:
      return False
    if int(num_str[2:5]) % 3 != 0:
      return False
    if int(num_str[3:6]) % 5 != 0:
      return False
    if int(num_str[4:7]) % 7 != 0:
      return False
    if int(num_str[5:8]) % 11 != 0:
      return False
    if int(num_str[6:9]) % 13 != 0:
      return False
    if int(num_str[7:10]) % 17 == 0:
      return True
    return False

  digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
  pandigitals = list(permutations(digits))

  sum = 0
  for pandigital in pandigitals:
    if check_requirements(num_from_list(pandigital)):
      sum += num_from_list(pandigital)

  print(sum)
  print(check_requirements(1406357289))