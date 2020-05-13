if __name__ == '__main__':
    string = str(2 ** 1000)

    sum = 0
    for num in string:
        sum += int(num)

    print(sum)