if __name__ == '__main__':
    product = 1
    for num in range(2, 101):
        product *= num
    sum = 0
    for let in str(product):
        sum += int(let)
    print(sum)