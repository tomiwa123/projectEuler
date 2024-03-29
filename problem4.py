if __name__ == '__main__':
    found_answer = False
    factors = [0, 0]


    def palindrome(number):
        s = str(number)

        return list(s)[::-1] == list(s)


    for num in range(998001, 1, -1):
        if found_answer:
            break
        if not palindrome(num):
            continue
        for factor in range(100, min(999, int(num ** 0.5))):
            if num % factor == 0 and len(str(num / factor)) == 3:
                found_answer = True
                print(num)
                factors[0] = factor
                factors[1] = num / factor
                break

    print(factors)
