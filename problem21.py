if __name__ == '__main__':
    def sum_divisors(number):
        divisor_sum = 0
        for poss_factor in range(1, int(number ** 0.5) + 1):
            if number % poss_factor == 0:
                divisor_sum += poss_factor
                if poss_factor not in {number / poss_factor, 1}:
                    divisor_sum += number // poss_factor
        return divisor_sum

    amicable_sum = 0
    store = ["Placeholder"]
    for num in range(1, 10001):
        store.append(sum_divisors(num))
    for num in range(1, 10001):
        potential_pair = store[num]
        if 1 <= potential_pair <= 10000:
            if num == store[potential_pair] and num != potential_pair:
                amicable_sum += num

    print(amicable_sum)
