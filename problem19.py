if __name__ == '__main__':

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    pointer = 2
    regular_year = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    leap_year = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    special_year = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2]
    count = 0

    for year in range(1901, 2001):
        if year % 4 != 0:
            year_to_be_used = regular_year
        elif year != 2000:
            year_to_be_used = leap_year
        else:
            year_to_be_used = special_year

        for index in year_to_be_used:
            pointer += index
            pointer %= 7
            if days_of_week[pointer] == "Sunday":
                count += 1
    print(count)