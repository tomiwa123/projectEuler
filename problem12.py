import math

if __name__ == '__main__':
    def count_factors(num):
        count = 0
        perfect_square = False
        for divisor in range(1, int(math.floor(num ** 0.5)) + 1):
            if num % divisor == 0:
                count += 1
            if divisor == num ** 0.5:
                perfect_square = True

        if perfect_square:
            return (count * 2) - 1
        return count * 2

    tally = 0
    answer = 0
    current = 1
    while answer == 0:
        tally += current
        if count_factors(tally) > 500:
            answer = tally
        current += 1

    print(tally)
