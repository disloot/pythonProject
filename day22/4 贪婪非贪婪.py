                                                                                    

import re
s="This is a number 234-235-22-423"
r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
print(r.group())
print(r.group(1))

test_str='''
<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">
'''
print(re.search(r"https://.*?\.jpg", test_str).group())