if __name__ == '__main__':
    def factorial(number):
        if number in {0, 1}:
            return 1
        return number * factorial(number - 1)

    current = 1000000
    answer = ["S"]*10

    for num in range(0, 10):
        index = 1
        step = factorial(9 - num)
        while current > step:
            index += 1
            current -= step
        answer[num] = index
    print(answer)

    num_ber = 2783915460