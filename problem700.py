if __name__ == '__main__':

    def somme(a, b):
        s = a
        while a != 0:
            b %= a
            while a >= b:
                a -= b
                s += a
        return s


    print(somme(1504170715041707, 4503599627370517))


