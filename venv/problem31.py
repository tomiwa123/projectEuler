if __name__ == '__main__':
    numbers = [1, 2, 5, 10, 20, 50, 100, 200]

    def find_possible_sums(list, target):
        if list == []:
            if target == 0:
                return 1;
            else:
                return 0;
        if target == 0:
            return 1;
        count = 0
        for multiple in range(0, 201):
            this_subtraction = multiple * list[0]
            if this_subtraction > target:
                break
            count += find_possible_sums(list[1:], target - this_subtraction)
        return count

    print(find_possible_sums(numbers, 200))