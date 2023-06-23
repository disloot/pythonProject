# 作者: 王道 龙哥
# 2022年03月22日10时57分54秒

class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, "description...")


def use_foo():
    obj = Foo()

    obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
    obj.BAR = "alex"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
    desc = Foo.BAR.__doc__  # 自动获取第四个参数中设置的值：description...
    print(desc)
    del obj.BAR


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value


    def del_price(self):
        del self.original_price


    PRICE = property(get_price, set_price,del_price,"description")

def use_goods():
    obj = Goods()
    print(obj.PRICE)         # 获取商品价格\
    print(Goods.PRICE.__doc__)  #打印描述,要用类名.property属性
    obj.PRICE = 200   # 修改商品原价
    print(obj.PRICE)
    del obj.PRICE     # 删除商品原价

if __name__ == '__main__':
    # use_foo()
    use_goods()