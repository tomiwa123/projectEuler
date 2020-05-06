if __name__ == '__main__':
    def check_if_answer(first, second):
        return 2000 * (first + second) == 10 ** 6 + 2 * first * second

    found_answer = False

    for a in range(1, 1000):
        for b in range (1, 1000):
            if check_if_answer(a, b):
                print(a*b*(1000 - a - b))
                print(a)
                print(b)
                print(1000 - a - b)
                found_answer = True
                break
        if found_answer:
            break
