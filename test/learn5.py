def foo():
    global a
    a = 20  # 此处会被python识别为是定义了一个新的变量a并赋值为20，并不会影响外部的a
    print(a)  # 20


if __name__ == '__main__':
    a = 10
    foo()
    print(a)  # 20