if __name__ == '__main__':
    records = {}
    largest_num = 0
    largest_length = -1

    for num in range(1, 1000000):
        current = num
        length = 0
        while current != 1:
            if current in records:
                length += records[current]
                break
            if current % 2 == 0:
                current /= 2
                length += 1
            else:
                current = 3 * current + 1
                length += 1
        records[num] = length
        if length > largest_length:
            largest_length = length
            largest_num = num
    print(largest_num)

