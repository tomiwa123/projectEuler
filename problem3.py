if __name__ == '__main__':

    def isprime(num):
        for x in range(2, int(num ** 0.5)):
            if num%x == 0:
                return False
        return True

    largest = 1
    for num in range(1, int(600851475143 ** 0.5)):
        if 600851475143%num == 0 and isprime(num):
            largest = num
    print(largest)