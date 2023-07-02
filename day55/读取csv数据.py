# ！/usr/bin/python3
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "./youtube_video_data/GB_video_data_numbers.csv"
# delimiter是分隔符
t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t2 = np.loadtxt(us_file_path,delimiter=",",dtype="int")

print(t1)
print("*"*100)
print(t2)
print("*"*100)
# b = t2[2:5,1:4]
# print(b)
t_us=t2
# 取评论的数据
t_us_comments = t_us[:,-1]
print(t_us.shape)
# 怎么知道分多少，打印最大和最小值


t_us_comments=t_us_comments[t_us_comments<=5000]
print(t_us_comments.max(),t_us_comments.min())
d=50
bin_nums = (t_us_comments.max()-t_us_comments.min())//d

# 绘图
plt.figure(figsize=(20,8),dpi=80)

plt.hist(t_us_comments,bin_nums)


plt.show()