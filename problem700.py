if __name__ == '__main__':

    euler_coin_tally = 1504170715041707
    increment = 1504170715041707
    min_euler_coin_seen = 1504170715041707
    current = increment

    while min_euler_coin_seen > 1:
        current += increment
        current %= 4503599627370517

        if current < min_euler_coin_seen:
            euler_coin_tally += current
            min_euler_coin_seen = current
            print(euler_coin_tally)
            print(min_euler_coin_seen)

    print(euler_coin_tally)


