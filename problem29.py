if __name__ == '__main__':
    set_of_powers = set([])
    for a in range(2, 101):
        for b in range(2, 101):
            set_of_powers.add(a ** b)
    print(len(set_of_powers))