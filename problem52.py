from collections import Counter

if __name__ == "__main__":
  for num in range(1, 200000):
    set_num = set(str(num))
    dict_num = Counter(str(num)).most_common()
    factors = []

    for factor in range(1, 7):
      # if len(str(num * factor)) != len(str(num)) or set(str(num * factor)) != set(str(num)):
      #   break
      dict_num_fact = Counter(str(num * factor)).most_common()
      if cmp(dict_num, dict_num_fact):
        break
      else:
        factors.append(num * factor)
    if len(factors) == 6:
      print(factors)