if __name__ == '__main__':

  sum = 0
  for num in range(1, 1000):
    sum += num ** num
    sum = sum % (10 ** 10)
  print(sum)
