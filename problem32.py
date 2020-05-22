if __name__ == '__main__':

    track = []
    for a in range(1, 10000):
        for b in range(1, 10000):
            if a == b:
                continue
            string_a = str(a)
            string_b = str(b)
            string_c = str(a * b)
            sum_of_strings = string_a + string_b + string_c
            if len(sum_of_strings) == len(set(sum_of_strings)) == 9:
                track.append(a * b)
    count = 0
    for num in set(track):
        count += num
    print(count)


