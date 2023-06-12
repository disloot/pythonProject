import my_module


def test1():
    print("*" * 50)
    print("test 1")
    print("*" * 50)


def test2():
    print("-" * 50)
    print("test 2")

    test1()

    print("-" * 50)


if __name__ == '__main__':
    # test2()
    my_module.print_line('*')
    print(my_module.name)
