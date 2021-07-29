if __name__ == '__main__':
  def is_prime(num):
        if num % 2 == 0 or num <= 1:
            return False
        for x in range(3, int(num ** 0.5) + 1):
            if num % x == 0:
                return False
        return True
    
  def is_circular_prime(num):
    # circular prime cannot contain digits 2, 4, 6, 8, 5, 0
    for test_num in ['0', '2', '4', '5', '6', '8']:
      if test_num in str(num):
        return False
    print(num)
    
    # number contains only 1, 3, 7, 9
  
  for num in range(1, 100):
    is_circular_prime(num)
