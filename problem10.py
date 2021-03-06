if __name__ == '__main__':
    def is_prime(num):
        if num % 2 == 0:
            return False
        for x in range(3, int(num ** 0.5) + 1):
            if num % x == 0:
                return False
        return True
    tally = 2
    for num in range(3, 2000000, 2):
        if is_prime(num):
            tally += num
    print(tally)