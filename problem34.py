if __name__ == '__main__':

  factorials = {
    '0': 1,
    '1': 1,
    '2': 2,
    '3': 6,
    '4': 24,
    '5': 120,
    '6': 720,
    '7': 5040,
    '8': 40320,
    '9': 362880
  }

  answer = 0
  for num in range(12, 1000000):
    string = str(num)
    sum = 0
    for letter in string:
      sum += factorials[letter]
    if sum == num:
      answer += sum

  print(answer)
