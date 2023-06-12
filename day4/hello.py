name = "小明"
student_no = 1
price = 9.00
weight = 5.01
money = 45.0
scale = 0.1
print(f"我的名字叫 {name}, 请多多关照")
print("我的学号是 %06d" % student_no)
print("苹果单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (price, weight, money))
print("数据比例是%.02f%%" % (scale * 100))
