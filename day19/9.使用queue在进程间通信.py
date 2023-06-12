# 作者: 王道 龙哥
# 2022年03月07日16时11分02秒
from multiprocessing import Process, Queue
import time
def writer(q):
    for value in ['A', 'B', 'C']:
        print(f'Put {value} to queue...')
        q.put(value)
        time.sleep(1)

def reader(q:Queue):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(2)
        else:
            break

if __name__ == '__main__':
    q=Queue(10)
    pw=Process(target=writer,args=(q,)) #一个元素必须加逗号，才是元组
    pr=Process(target=reader,args=(q,))
    pw.start()
    time.sleep(1)
    pr.start()
    pw.join()
    pr.join()