import cmath

if __name__ == "__main__":

  triangles = set()
  for t in range(1, 100000):
    triangles.add((t * (t + 1))/2)
  pentagonals = set()
  for p in range(1, 100000):
    pentagonals.add((p * ((3 * p) - 1)) / 2)
  for h in range(1, 100000):
    p_h = h * ((2 * h) - 1)
    if p_h in triangles and p_h in pentagonals:
      print(h, p_h)
