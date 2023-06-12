# 作者: 王道 龙哥
# 2022年03月04日16时38分09秒
import struct
import os
import time

train_content = '我很帅你很牛'.encode('utf-8')
train_head=len(train_content)
print(train_head)
print(type(train_head))
print('-'*50)
train_head_bytes=struct.pack('I',train_head)
print(train_head_bytes)

b=struct.unpack('I',train_head_bytes)
print(b[0])
print('-'*50)
c=train_head_bytes+train_head_bytes
print(c)