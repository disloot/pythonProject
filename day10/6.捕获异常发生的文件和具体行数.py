
try:
    print(a)
except Exception as e:
    print(e)
    print(e.__traceback__.tb_frame.f_globals["__file__"])   # 发生异常所在的文件
    print(e.__traceback__.tb_lineno)  #打印异常发生的代码 行