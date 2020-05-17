if __name__ == '__main__':

    def count_recurring(decimal):
        num_string = str(decimal)
        found = ""
        index = "shouldBeUpdated"
        for let in num_string:
            if let in found:
                index = found.index(let)
                break
            else:
                found += let
        return len(found) - index

    longest_length = 0
    longest_number = 1
    for num in range(2, 1000):
        dec = (10 ** 50) // num
        if dec % (10 ** 49) == 0:
            continue
        repeating = count_recurring(dec)
        if repeating > longest_length:
            longest_length = repeating
            longest_number = num
    print(longest_number, longest_length)
    print(round((10 ** 200) // 983, 20))
    print(count_recurring((10 ** 90) // 983))
     # answer  = 983 tho