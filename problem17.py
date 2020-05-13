if __name__ == '__main__':
    num_to_words_dict = {}

    for num in range(1, 1001, 1):
        if num in {1, 2, 6, 10}:
            num_to_words_dict[num] = 3
        if num in {4, 5, 9}:
            num_to_words_dict[num] = 4
        if num in {3, 7, 8, 40, 50, 60}:
            num_to_words_dict[num] = 5
        if num in {11, 12, 20, 30, 80, 90}:
            num_to_words_dict[num] = 6
        if num in {15, 16, 70}:
            num_to_words_dict[num] = 7
        if num in {13, 14, 18, 19}:
            num_to_words_dict[num] = 8
        if num in {17}:
            num_to_words_dict[num] = 9
        if num in set(range(21, 100)) and num % 10 != 0:
            num_to_words_dict[num] = num_to_words_dict[(num // 10) * 10] + num_to_words_dict[num % 10]
        if num in {100, 200, 300, 400, 500, 600, 700, 800, 900}:
            num_to_words_dict[num] = num_to_words_dict[num // 100] + 7
            continue
        if num in set(range(101, 1000)):
            hundredths = (num // 100) * 100
            # correct = num_to_words_dict[hundredths] + 3 + num_to_words_dict[num % 100]
            # print(num % 100)
            num_to_words_dict[num] = num_to_words_dict[hundredths] + 3 + num_to_words_dict[num % 100]
        if num == 1000:
            num_to_words_dict[num] = 11

    sum = 0
    for item in num_to_words_dict.values():
        sum += item
    print(sum)
