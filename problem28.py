if __name__ == '__main__':
    current = 1
    step = 2
    numbers = [1]
    while current <= 1001 * 1001:
        for _ in range(4):
            current += step
            numbers.append(current)
        step += 2
    num_sum = 1
    for num in range(1, len(numbers), 2):
        num_sum += num
    print(num_sum)