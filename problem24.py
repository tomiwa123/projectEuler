if __name__ == '__main__':
    def factorial(number):
        if number in {0, 1}:
            return 1
        return number * factorial(number - 1)

    current = 1000000
    # filler elements in string to make double checking easy
    answer = ["S"]*10

    for num in range(0, 10):
        index = 1
        step = factorial(9 - num)
        while current > step:
            index += 1
            current -= step
        answer[num] = index
    # Each index value corresponds to the lexicographic position of the
    # element that is supposed to be in that index
    # Note that numbers may not be repeated
    print(answer)

    # The actual correct final string using iterative calculator process
    num_ber = 2783915460