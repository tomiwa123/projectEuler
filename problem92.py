ones = set()
ones.add(1)
eighty_nines = set()
eighty_nines.add(89)

def transform(num):
  sum = 0
  for let in str(num):
    sum += int(let) ** 2
  return sum

for num in range(1, 10000000):
  temp = num
  track = {num}
  while (temp != 1) and (temp != 89):
  # while (temp != 1) and (temp != 89) and (temp not in ones) and (temp not in eighty_nines):
    # print(temp)
    temp = transform(temp)
    track.add(temp)
  # print(track)
  # print(temp)
  if temp == 1 or temp in ones:
    ones.union(track)
  elif temp == 89 or temp in eighty_nines:
    eighty_nines = eighty_nines.union(track)
  
# print(eighty_nines)
print(len(eighty_nines))