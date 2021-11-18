def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for x in fib(10):
        print(x)


if __name__ == '__main__':
    main()
