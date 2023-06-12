#!usr/bin/python3
# author lyle

def change(list_: list, dict_: dict):
    list_.pop()
    dict_.update({'ne': 2})


def change_1(*args, **kwargs):
    print(args)
    print(kwargs)
    change(list(args), kwargs)
    print(args)
    print(*kwargs)


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = {'name': 1}
    change_1(a, b)
    pass
