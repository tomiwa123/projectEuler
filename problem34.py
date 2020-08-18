if __name__ == '__main__':
    def factorial(number):
        if number <= 1:
            return 1
        return number * factorial(number - 1)

    for num in range(10, 1000000):
        string = str(num)
        sum = 0
        for digit in string:
            sum += factorial(int(digit))
        if sum == num:
            print(sum, num)
