# 作者: 王道 龙哥
# 2022年03月07日15时25分11秒
from multiprocessing import Queue
q=Queue(3) #初始化一个Queue对象，最多可接收三条put消息
q.put(1)
q.put(2)
print(q.full())  #False
q.put(3)
print(q.full())  #True
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# q.put(4)  # 队列满了后，再放会阻塞
try:
    q.put("消息4",False)
except:
    print("消息列队已满，现有消息数量:%s"%q.qsize())

try:
    q.put_nowait("消息4")
except:
    print("消息列队已满，现有消息数量:%s"%q.qsize())