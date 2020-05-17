if __name__ == '__main__':
    def thousand_check(number):
        return number // (10 ** 999) >= 1

    fib_1 = 1
    fib_2 = 2
    index = 2
    while not thousand_check(fib_2):
        temp = fib_2
        fib_2 = fib_1 + fib_2
        fib_1 = temp
        index += 1
    print(index + 1, fib_2)