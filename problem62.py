if __name__ == "__main__":
  def get_cube_code(num):
    str_num = str(num)
    code = [0]*10
    
    for digit in str_num:
      code[int(digit)] += 1
    
    str_code = ""
    for count in code:
      str_code += str(count)
    
    return str_code
  
  store = dict()

  for num in range(100, 10000):
    cube = num ** 3
    cube_code = get_cube_code(cube)

    if cube_code in store.keys():
      store[cube_code].append(num)
    else:
      store[cube_code] = [num]

  largest_key = ""
  largest_cubes = [100000]
  largest_value = 0
  for k, v in store.items():
    if len(v) == 5 and v[0] < largest_cubes[0]:
      largest_value = len(v)
      largest_cubes = v
      largest_key = k
  print(largest_cubes, largest_value)
  print(largest_cubes[0] ** 3)
