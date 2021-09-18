def count_variations(a, b, x, y):
  if a > x or b > y:
    return 0
  if a == x and b == y:
    return 1
  return (x - a + 1) * (y - b + 1)

max_count = 0
max_x_y = (0, 0)

for x in range(2, 100):
  for y in range(2, 100):
    count = 0
    for a in range(1, x + 1):
      for b in range(1, y + 1):
        count += count_variations(a, b, x, y)
    print(x, y, count)
    if abs(2000000 - count) < abs(2000000 - max_count):
      max_count = count
      max_x_y = (x, y)

print(max_x_y, max_count)
