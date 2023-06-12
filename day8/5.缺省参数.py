#!/usr/bin/python
# author luke
# 2022年02月22日

# 缺省参数指传参时可以不传对应参数
def print_info(name, gender=True):

    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name, gender_text))

# 缺省参数放最后
def print_info1(name, title='', gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s%s 是 %s" % (title, name, gender_text))

if __name__ == '__main__':
    # print_info('xiongda')
    print_info1('xiongda')
    print_info1("老王", "班长")
    print_info1("小美", gender=False)
