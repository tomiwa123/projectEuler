if __name__ == '__main__':
  def check_pallindrome(num):
    # print(list(str(num)))
    digits = list(str(num))
    length = len(digits)
    for index in range(0, length // 2):
      if digits[index] != digits[length - index - 1]:
        return False
    return True

  def check_bin_pallindrome(num):
    digits = num[2:]
    length = len(digits)
    for index in range(0, length // 2):
      if digits[index] != digits[length - index - 1]:
        return False
    return True

  answer = []
  for num in range(11, 586):
    if check_pallindrome(num) and check_bin_pallindrome(bin(num)):
      answer.append(num)

  print(answer)