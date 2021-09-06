import cmath

if __name__ == "__main__":
  
  def solve_quadratic(c, a = 3, b = -1):  
    # calculating  the discriminant
    dis = (b**2) - (4 * a*c)
      
    # find two results
    ans1 = (-b - cmath.sqrt(dis))/(2 * a)
    ans2 = (-b + cmath.sqrt(dis))/(2 * a)

    return (ans1, ans2)
  
  def get_c_versions(j, k):
    pos_c = 3 * ((j ** 2) + (k ** 2)) - (j + k)
    neg_c = 3 * ((j ** 2) - (k ** 2)) - (j - k)
    return pos_c, neg_c
  
  def test_c_value(c):
    opt_1, opt_2 = solve_quadratic(-c)
    if opt_1.imag == 0:
      if opt_1.real.is_integer() and opt_1.real > 0:
        return int(opt_1.real)
    if opt_2.imag == 0:
      if opt_2.real.is_integer() and opt_2.real > 0:
        return int(opt_2.real)
    return False

  for j in range(4, 300):
    for k in range(j-3, j):
      pos_c, neg_c = get_c_versions(j, k)
      
      # Calculate addition
      pos_sol = test_c_value(pos_c)
      if not pos_sol:
        continue
      print(j, k, pos_sol)      
      
      # Calculate subtraction
      neg_sol = test_c_value(neg_c)
      if not neg_sol:
        continue
      print(j, k, neg_sol)      

    