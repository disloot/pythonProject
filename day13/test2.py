# #!usr/bin/python3
# # author lyle
# f = open('The_Holy_Bible.txt')
# f1 = open('Bible', mode='w', encoding='utf8')
# while True:
#     text = f.readline()
#     if text != '':
#         a = text.split(' ')
#         a.pop(0)
#         text = " ".join(a)
#         f1.write(text)
#     else:
#         break
# import re
#
#
# punctuation = '!,.;:?'
#
#
# def remove_punctuation(text):
#     text = re.sub('[{}]+'.format(punctuation), '', text)
#     return text
# sentence = "+今天=是！2021!   年/8月?1,7日★.---《七夕节@》：让我*们出门（#@）去“感受”夏天的荷尔蒙！"
# string4 = re.sub('', '', sentence)
# string = remove_punctuation(sentence)
# print(string)
b ={'a': 11, 'b': 15, 'c': 18, 'd': 15, 'e': 11}
sorted(b)