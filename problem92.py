def transform(num):
  sum = 0
  for let in str(num):
    sum += int(let) ** 2
  return sum

values = [0]*10000001
for num in range(1, 10000000):
  values[num] = num
for num in range(1, 10000000):
  # print(num)
  temp = values[num]
  if temp in {1, 89}:
    continue
  track = {temp}
  while (temp != 1) and (temp != 89):
    new_index = transform(temp)
    temp = values[new_index]
    track.add(temp)
  
  update = 89
  if temp == 1:
    update = 1
  for index in track:
    values[index] = update

count = 0
for num in range(1, 10000000):
  if values[num] == 89:
    count += 1
print(count)