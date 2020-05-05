if __name__ == '__main__':
    def is_prime(num):
        if num % 2 == 0:
            return False
        for x in range(3, int(num ** 0.5) + 1):
            if num % x == 0:
                return False
        return True

    count = 1
    current = 3
    while count <= 10000:
        if is_prime(current):
            count += 1
        current += 2
    print(current - 2)
