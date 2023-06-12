# author luke
# 2022年02月25日

from collections import deque
#增删查改
queue = deque(["Eric", "John", "Michael"])
queue.append('luke')
print(queue)
print(queue.popleft())
print(queue)

queue[0] ='xiongda'
print(queue[0])

