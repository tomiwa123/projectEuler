if __name__ == '__main__':
    tally = 0
    for num in range(1, 1000):
        if num%3 == 0 or num %5 == 0:
            tally += num
    print(tally)