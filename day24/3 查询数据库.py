
from pymysql import *

def main1():
    # 创建Connection连接
    conn = connect(host='192.168.10.129', port=3306, database='pythonProject',
                   user='root', password='123', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count = cs1.execute('select * from goods where id>=4')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)

    for _ in range(count):
        # 获取查询的结果，fetchone像迭代器
        result = cs1.fetchone()
        # 打印查询的结果
        print(result)
    # 关闭Cursor对象 
    
    cs1.close()
    conn.close()

def main2():
    # 创建Connection连接
    conn = connect(host='192.168.10.129', port=3306, database='pythonProject',
                   user='root', password='123', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count = cs1.execute('select id,name from goods where id>=4')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)

    result = cs1.fetchall()
    print(result)

    # 关闭Cursor对象
    cs1.close()
    conn.close()



if __name__ == '__main__':
    # main1()
    main2()