if __name__ == '__main__':

    num_list = list(range(1, 10))
    used_set = set([])
    for a in num_list:
        used_set.add(a)
        list_a = list(filter(lambda num: num not in used_set, num_list))
        for b in list_a:
            used_set.add(b)
            list_b = list(filter(lambda num: num not in used_set, num_list))
            for c in list_b:
                use
            used_set.remove(b)
        used_set.remove(a)