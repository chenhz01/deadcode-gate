def used(a):
    return a + 1


def never_called(b):
    return b * 2


def main():
    return used(1)


if __name__ == '__main__':
    main()
