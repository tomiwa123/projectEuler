import cmath

if __name__ == "__main__":
  
  def solve_quadratic(a, b, c):  
    # calculating  the discriminant
    dis = (b**2) - (4 * a*c)
      
    # find two results
    ans1 = (-b - cmath.sqrt(dis))/(2 * a)
    ans2 = (-b + cmath.sqrt(dis))/(2 * a)

    return (ans1, ans2)
  
  def solve_quadratic_tri(c, a=1, b=1):
    return solve_quadratic(a, b, -2 * c)
  
  def solve_quadratic_pent(c, a=3, b=-1):
    return solve_quadratic(a, b, -2 * c)

  def solve_quadratic_hex(c, a=2, b=-1):
    return solve_quadratic(a, b, -c)
  
  def test_roots(root_1, root_2):
    # Account for the possibility that both roots are valid
    if root_1.imag == 0:
      if root_1.real.is_integer() and root_1.real > 0:
        return int(root_1.real)
    if root_2.imag == 0:
      if root_2.real.is_integer() and root_2.real > 0:
        return int(root_2.real)
    return False

  for num in range(20000000, 40000000):
    # Check if num is triangle
    solution = [num]
    tri_sol = solve_quadratic_tri(num)
    
    if not test_roots(*tri_sol):
      continue
    # print(test_roots(*tri_sol))
    solution.append(test_roots(*tri_sol))

    pent_sol = solve_quadratic_pent(num)
    
    if not test_roots(*pent_sol):
      continue
    # print(test_roots(*pent_sol))
    solution.append(test_roots(*pent_sol))
    
    hex_sol = solve_quadratic_hex(num)
    
    if not test_roots(*hex_sol):
      continue
    # print(test_roots(*hex_sol))
    solution.append(test_roots(*hex_sol))

    print(solution)

  # print(test_roots(*solve_quadratic_hex(2 * 40755)))

