if __name__ == '__main__':
  def check_pallindrome(digits):
    length = len(digits)
    for index in range(0, length // 2):
      if digits[index] != digits[length - index - 1]:
        return False
    return True

  def check_bin_pallindrome(num):
    digits = num[2:]
    return check_pallindrome(digits)

  answer = 0
  for num in range(1, 1000000):
    if check_pallindrome(list(str(num))) and check_bin_pallindrome(bin(num)):
      answer += num

  print(answer)