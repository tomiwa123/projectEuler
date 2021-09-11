if __name__ == '__main__':
    def get_first_digit(number):
        return number // 10

    def get_second_digit(number):
        return number % 10

    top = 1
    bottom = 1

    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            frac_1 = float(numerator) / denominator
            if get_first_digit(numerator) == 0 or \
                    get_second_digit(denominator) == 0 or \
                    (numerator % 11 == 0 and denominator % 11 == 0):
                continue
            frac_2 = float(get_first_digit(numerator)) / get_second_digit(denominator)

            if frac_1 == frac_2 and get_second_digit(numerator) == get_first_digit(denominator):
                print(numerator, denominator)
                top *= numerator
                bottom *= denominator

    def simplify_frac(a, b):
        above = a
        below = b
        for divisor in range(a-1, 1):
            if above % divisor == 0 and below % divisor == 0:
                print(above, below, divisor)
                above /= divisor
                below /= divisor
        return above, below

    print(simplify_frac(top, bottom))
