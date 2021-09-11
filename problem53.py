if __name__ == "__main__":
  pascal = [1, 2, 1]
  b = 100
  def update_pascal(b):
    new_pascal = [1]
    global pascal
    for index in range(0, min(b, len(pascal) - 1)):
      new_pascal.append(pascal[index] + pascal[index + 1])
    new_pascal.append(1)
    pascal = new_pascal
  
  def get_current_pascal_number():
    return len(pascal) - 1
  
  def calculate_x(n, b):
    return n + 1 - (2 * b)
  
  while get_current_pascal_number() < 23:
    update_pascal(23)
  
  count = 0
  for n in range(23, 101):
    for index in range(n):
      if pascal[index] > 1000 ** 2:
        # print(n, index, pascal[index])
        # print(n, index, calculate_x(n, index))
        count += calculate_x(n, index)
        b = index
        break
    update_pascal(b)

  print(count)