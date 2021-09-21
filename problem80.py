import math

def get_next_digit_sqrt(divisor, dividend):
  str_divisor = str(divisor)
  for num in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
    new_divisor = int(str_divisor + str(num))
    if new_divisor * num < dividend:
      new_dividend = int(str(dividend - (new_divisor * num)) + "00")
      return num, new_divisor, new_dividend
    else:
      print(dividend - new_divisor * num)
  print("something went wrong", divisor, dividend)

def hundred_digits_sqrt(num):
  if math.sqrt(num) == int(math.sqrt(num)):
    return 0
  sum = 0
  divisor, dividend = 0, num
  for _ in range(100):
    next_digit, divisor, dividend = get_next_digit_sqrt(divisor, dividend)
    sum += next_digit
  return sum

sum = 0
for num in range(1, 3):
  sum += hundred_digits_sqrt(num)
print (sum)