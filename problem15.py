if __name__ == '__main__':
    total_product = 1
    for num in range(21, 41):
        total_product *= num
    for num in range(1, 21):
        total_product /= num

    print(total_product)
    # The answer is 40 choose 20