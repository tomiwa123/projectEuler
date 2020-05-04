if __name__ == '__main__':
    tally = 0
    first_fib = 1
    second_fib = 2
    while second_fib <= 4000000:
        if second_fib%2 == 0:
            tally += second_fib
        new_fib = first_fib + second_fib
        first_fib = second_fib
        second_fib = new_fib
    print(tally)

