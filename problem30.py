if __name__ == '__main__':

    sum_of_powers = 0

    for num in range(1000, 10000):
        string = str(num)
        fifth_power_sum = 0
        for index in range(0, 4):
            fifth_power_sum += (int(string[index]) ** 5)
        # print(num, fifth_power_sum)
        if fifth_power_sum == num:
            print(num, fifth_power_sum)
            sum_of_powers += fifth_power_sum

    for num in range(10000, 100000):
        string = str(num)
        fifth_power_sum = 0
        for index in range(0, 5):
            fifth_power_sum += (int(string[index]) ** 5)
        # print(num, fifth_power_sum)
        if fifth_power_sum == num:
            print(num, fifth_power_sum)
            sum_of_powers += fifth_power_sum

    for num in range(100000, 1000000):
        string = str(num)
        fifth_power_sum = 0
        for index in range(0, 6):
            fifth_power_sum += (int(string[index]) ** 5)
        # print(num, fifth_power_sum)
        if fifth_power_sum == num:
            print(num, fifth_power_sum)
            sum_of_powers += fifth_power_sum

    for num in range(1000000, 10000000):
        string = str(num)
        fifth_power_sum = 0
        for index in range(0, 7):
            fifth_power_sum += (int(string[index]) ** 5)
        # print(num, fifth_power_sum)
        if fifth_power_sum == num:
            print(num, fifth_power_sum)
            sum_of_powers += fifth_power_sum

    print(sum_of_powers)