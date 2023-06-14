
from operator import itemgetter, attrgetter
def sort_str():
    l = "This is a test string from Andrew".split()
    print(l)
    print(sorted(l, key=str.lower))


def sort_list_tuple():
    # Pycharm中竖选是shift+alt+鼠标左键
    student_tuples = [
        ('john', 'A', 15),
        ('dave', 'B', 12),
        ('jane', 'B', 10),
    ]

    # lambda 就是匿名函数
    print(sorted(student_tuples, key=lambda i: i[0], reverse=True))


class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):  #相对于str更加灵活
        return repr((self.name, self.grade, self.age))


# 排序的列表里是自定义的object
def sort_list_object():
    student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]
    print(sorted(student_objects, key=lambda s: s.age))





def use_operator():
    student_tuples = [
        ('dave', 'B', 12),
        ('john', 'A', 15),
        ('jane', 'B', 10),
    ]
    print(sorted(student_tuples, key=itemgetter(2), reverse=True))
    student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]
    print(sorted(student_objects, key=attrgetter('age')))
    print(sorted(student_tuples, key=itemgetter(1, 2)))
    print(sorted(student_objects, key=attrgetter('grade', 'age')))


def use_stability():
    l = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
    l.sort(key=itemgetter(0))
    print(l)


def dict_list():
    mydict = {'Li': ['M', 7],
              'Zhang': ['E', 2],
              'Wang': ['P', 3],
              'Du': ['C', 2],
              'Ma': ['C', 9],
              'Zhe': ['H', 7]}
    # 字典的key value是组合为一个元组
    print(sorted(mydict.items(), key=lambda v: v[1][1]))


# 列表中含有字典
def list_dist():
    gameresult = [
        {"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
        {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
        {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
        {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]
    print(sorted(gameresult, key=itemgetter('rating', 'wins')))


if __name__ == '__main__':
    #sort_list_object()
    # use_operator()
    # use_stability()
    # dict_list()
    sort_str()