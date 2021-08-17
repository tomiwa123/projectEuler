if __name__ == '__main__':

  digits_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
  digits_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  def num_from_list(my_list):
    result = 0
    length = len(my_list)
    for index, letter in enumerate(my_list):
      result += int(letter) * pow(10, length - index - 1)
    return result
  
  def is_list_pandigital(num_list):
    modified_num_list = list(map(int, num_list))
    return set(modified_num_list) == digits_set

  biggest_pandigital = 0
  number_index = (0, 0)
  for num in range(1, 1000000):
    concatenated_product = []
    index = 1
    
    while len(concatenated_product) < 9:
      product = num * index
      product_list = list(str(product))
      concatenated_product.extend(product_list)
      index += 1
    
    if not is_list_pandigital(concatenated_product[:9]):
      continue
    
    pandigital = num_from_list(concatenated_product[:9])
    biggest_pandigital = max(biggest_pandigital, pandigital)
    number_index = (num, index)

  print(biggest_pandigital)
  print(number_index)