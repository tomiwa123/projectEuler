from ProjEulerTools import *

if __name__ == "__main__":
  def check_pallindrome(digits):
    length = len(digits)
    for index in range(0, length // 2):
      if digits[index] != digits[length - index - 1]:
        return False
    return True
  
  lychrel = 0

  for num in range(1, 10000):
    count = 0
    current_sum = num
    found = False

    while count < 51:
      count += 1
      reverse_current = list(str(current_sum))
      reverse_current.reverse()
      current_sum += num_from_list(reverse_current)
      if check_pallindrome(str(current_sum)):
        print(current_sum)
        found = True
        break
    if not found:
      lychrel += 1
  
  print(lychrel)