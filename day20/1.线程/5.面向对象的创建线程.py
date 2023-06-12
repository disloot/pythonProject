# 作者: 王道 龙哥
# 2022年03月08日10时20分32秒
import threading
import time

class MyThread(threading.Thread):
    def run(self) -> None:
        for i in range(3):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i) #name属性中保存的是当前线程的名字
            print(msg)

# 创建5个线程
def test():
    for i in range(5):
        t = MyThread()
        t.start()
if __name__ == '__main__':
    test()