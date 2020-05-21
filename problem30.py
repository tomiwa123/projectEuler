if __name__ == '__main__':

    sum_of_powers = 0

    for num in range(1000, 1000000):
        string = str(num)
        fifth_power_sum = 0
        for index in range(0, 6):
            if index < len(string):
                fifth_power_sum += (int(string[index]) ** 5)
        # print(num, fifth_power_sum)
        if fifth_power_sum == num:
            print(num, fifth_power_sum)
            sum_of_powers += fifth_power_sum

    print(sum_of_powers)
