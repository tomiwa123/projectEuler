if __name__ == '__main__':
    current = 1
    step = 2
    sum = 1
    while current <= 1000 * 1000:
        for _ in range(4):
            current += step
            sum += current
        step += 2
    print(sum)