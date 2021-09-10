if __name__ == '__main__':
    def sum_divisors(number):
        divisor_sum = 0
        for poss_factor in range(1, int(number ** 0.5) + 1):
            if number % poss_factor == 0:
                divisor_sum += poss_factor
                if poss_factor not in {number / poss_factor, 1}:
                    divisor_sum += number // poss_factor
        return divisor_sum

    def check_abundance(number):
        return sum_divisors(number) > number

    abundance_dictionary = {}

    for num in range(1, 28124):
        abundance_dictionary[num] = check_abundance(num)

    tally = (23 * 24) // 2
    for num in range(24, 28124):
        for slices in range(12, num // 2 + 1):
            if abundance_dictionary[slices] and abundance_dictionary[num - slices]:
                tally -= num
                break
        tally += num
    print(tally)
