if __name__ == '__main__':
    current = 1
    step = 2
    numbers = [1]
    while current <= 1000 * 1000:
        for _ in range(4):
            current += step
            numbers.append(current)
        step += 2
        print(current ** 0.5)
    num_sum = 1
    for num in range(1, len(numbers)):
        num_sum += numbers[num]
    print(num_sum)