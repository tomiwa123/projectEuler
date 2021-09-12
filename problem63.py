if __name__ == "__main__":
  count = 0
  def check_num_power(x, y):
    return len(str(x ** y)) == y

  for n in range(1, 22):
    for a in range(1, 10):
      if check_num_power(a, n):
        count += 1
  print(count)
