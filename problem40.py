# d1 = 1
# d10 = 1
# d100 = 8 - 85
# d1000 = 

if __name__ == '__main__':
  count = 0

  for num in range(1, 1000000):
    # print(count, num)
    
    length = len(str(num))
    new_count = count + length

    if count <= 100 <= new_count:
      print(count, num)
    if count <= 1000 <= new_count:
      print(count, num)
    if count <= 10000 <= new_count:
      print(count, num)
    if count <= 100000 <= new_count:
      print(count, num)
    if count <= 1000000 <= new_count:
      print(count, num)
    
    count = new_count
    
    