if __name__ == "__main__":
  def check_valid_solution(x, d, y):
    return (x ** 2) - d*(y ** 2) == 1
  
  max_x = 0
  unsolved = []

  for d in range(2, 1001):
    if int(d ** 0.5) == d ** 0.5:
      # print("Square:", d)
      continue
    found = False
    for x in range(2, 1000):
      if found:
        break
      for y in range(1, x):
        if check_valid_solution(x, d, y):
          # print(x, d, y)
          max_x = max(max_x, x)
          found = True
          break
    if not found:
      unsolved.append(d)
  print(max_x)
  print(unsolved)