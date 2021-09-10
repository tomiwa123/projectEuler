if __name__ == '__main__':
    num_sum = 0
    sum_of_squares = 0
    for num in range(1, 101):
        num_sum += num
        sum_of_squares += num**2
    print(num_sum ** 2 - sum_of_squares)