# 作者: 王道 龙哥
# 2022年03月09日10时17分23秒
import re

result=re.match('wangdao','wangdao.cn')
if result:
    print(result.group())