if __name__ == '__main__':
    file = open('p022_names.txt', 'r')
    desired_list = file.read().split('\",\"')
    desired_list[0] = 'MARY'
    desired_list[-1] = 'ALONSO'
    desired_list.sort()
    print(desired_list)
    desired_list.insert(0, 0)
    length = len(desired_list)
    name_score = 0

    for index in range(1, length):
        this_sum = 0
        for let in desired_list[index]:
            this_sum += (ord(let) - 64)
        name_score += (this_sum * index)
        print(desired_list[index], name_score)

    print(name_score)
    file.close()
