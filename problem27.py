if __name__ == '__main__':
    def is_prime(num):
        if num % 2 == 0 or num <= 1:
            return False
        for x in range(3, int(num ** 0.5) + 1):
            if num % x == 0:
                return False
        return True

    pair = 0
    max_primes = 0

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            count = 0
            terminated = False
            while not terminated:
                if is_prime(count ** 2 + a * count + b):
                    count += 1
                else:
                    terminated = True
            if count > max_primes:
                max_primes = count
                pair = a, b
    print(pair[0] * pair[1])
