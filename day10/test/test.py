#!usr/bin/python3
# author lyle
import os


class Player:
    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__()
        return cls.instance


class NotSymmetry(Exception):
    def __init__(self, msg):
        self.msg = msg


def is_symmetry(num):
    num = str(num)
    length = len(num)
    for i in range(length // 2):
        if num[i] != num[length - i - 1]:
            return False
    return True


def demo1():
    result = int(input('输入：'))
    if not is_symmetry(result):
        raise NotSymmetry('输入对称数')
    result = 8 / result
    return result


def demo2():
    return demo1()


def use_os():
    file = open("file.txt", mode='w+', encoding='utf8')
    file.write("人生苦短\n我用Python")
    file.seek(0, 0)
    print(file.read())
    file.seek(0, 0)
    file1 = open("file1.txt", mode='w+', encoding='utf8')
    while True:
        text = file.readline()
        if text == '':
            break
        file1.write(text)
    file1.close()
    file.close()


def use_try_except():
    try:
        num = demo2()
    except ValueError:
        print('请输入数字')
    except ZeroDivisionError:
        print('请勿输入0')
    except NotSymmetry as ex:
        print(ex)
    except Exception as ex:
        print('未知错误:{}'.format(ex))
    finally:
        print(num)


def use_mode_rb():
    use_os()
    file = open("file.txt", mode='r', encoding='utf8')
    file1 = open("file1.txt", mode='rb')
    print(file.read())
    print(file1.read())


def dep_search_dir(path, depth=0):
    for i in os.listdir(path):
        print(" " * 4 * depth + i)
        if os.path.isdir(path + '/' + i):
            dep_search_dir(path + '/' + i, depth + 1)


if __name__ == '__main__':
    dep_search_dir("./")
