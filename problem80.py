import math

def get_next_digit_sqrt(divisor, dividend):
  str_divisor = str(divisor)
  new_dividend = dividend
  for num in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
    new_divisor = int(str_divisor + str(num))
    if new_divisor * num < new_dividend:
      new_dividend = int(str(new_dividend - (new_divisor * num)) + "00")
      return num, new_divisor + num, new_dividend
      
  return 0, divisor, int(str(new_dividend) + "0") 
  # new_dividend = int(str(new_dividend) + "0")

digits = []

def hundred_digits_sqrt(num):
  if math.sqrt(num) == int(math.sqrt(num)):
    return 0
  sum = 0

  div = math.floor(math.sqrt(num))
  divisor, dividend = int(div * 2), int(str(int(num - (div ** 2))) + "00")
  for _ in range(100):
    next_digit, divisor, dividend = get_next_digit_sqrt(divisor, dividend)
    # print(next_digit)
    digits.append(next_digit)
    sum += next_digit
  return sum

sum = 0
for num in range(1, 100):
  sum += hundred_digits_sqrt(num)
  # print(num, len(digits), sum)
  digits = []
print (sum)