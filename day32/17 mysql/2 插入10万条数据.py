
from pymysql import connect

def main():
    # 创建Connection连接
    conn = connect(host='192.168.19.130',port=3306,user='root',password='123',database='jing_dong',charset='utf8')
    # 获得Cursor对象
    cursor = conn.cursor()
    # 插入10万次数据
    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)
    # 提交数据，不提交是插入不进去的
    conn.commit()

if __name__ == "__main__":
    main()