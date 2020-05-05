if __name__ == '__main__':
    num_sum = 0
    tally = 0
    for num in range(1, 101):
        num_sum += num
        tally += num**2
    print(num_sum ** 2 - tally)