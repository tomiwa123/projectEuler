from math import floor, ceil

if __name__ == "__main__":

  smallest_diff = 1000
  best_d = 0
  best_n = 1000
  three_seven = 3.0/7

  for d in range(25, 1000 * 1000):
    floor_value = floor(d / 7) * 3
    # ceil_value = ceil(d / 7)
    while (floor_value / d) < three_seven:
      test_value = floor_value / d
      if (3/7 - test_value) < smallest_diff:
        smallest_diff = 3/7 - test_value
        best_d = d
        best_n = floor_value
      floor_value += 1
  print(best_d, best_n, smallest_diff)