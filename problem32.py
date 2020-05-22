if __name__ == '__main__':

    track = []
    for a in range(1, 10000):
        for b in range(1, 10000):
            if (a > 1000 and b > 1000) or b >= a:
                break
            string_a = str(a)
            string_b = str(b)
            string_c = str(a * b)
            sum_of_strings = string_a + string_b + string_c
            if "0" in sum_of_strings:
                continue
            if len(sum_of_strings) == len(set(sum_of_strings)) == 9:
                track.append(a * b)
                print(a, b, a * b)
    count = 0
    for num in set(track):
        count += num
    print(count)


