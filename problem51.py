from ProjEulerTools import *
from collections import Counter

if __name__ == "__main__":
  non_valid_primes = dict()
  longest_count = 0
  longest_primes = []

  def count_other_primes(num, duplicate):
    str_num = str(num)
    generic = str_num.replace(str(duplicate), "*")
    if generic in non_valid_primes.keys():
      return non_valid_primes[generic]
    options = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    options.remove(duplicate)
    count = 1
    primes = [num]
    for variant in options:
      variant = str(variant)
      mod_str_num = str_num.replace(str(duplicate), variant)
      duplicate_variant = int(mod_str_num)
      if is_prime(int(mod_str_num)) and len(str(int(mod_str_num))) == len(str_num):
        # TODO: Implement handling 1**45 *=1
        count += 1
        primes.append(int(mod_str_num))
    
    
    non_valid_primes[generic] = (count, primes)
    return count, primes

  for num in range(100000, 1000000):
    if not is_prime(num) or num in non_valid_primes:
      continue

    for num_stars in range(2, 5):

      counter_list = Counter(str(num)).most_common()
      for duplicate, count in counter_list:
        if count != num_stars:
          continue
        count, primes = count_other_primes(num, int(duplicate)) # Re think total logic thus far
        if count > longest_count:
          longest_count = count
          longest_primes = primes

  print(longest_count, longest_primes)