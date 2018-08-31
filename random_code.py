# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 01:11:19 2018

@author: wei
"""

import random
list = []
#生成26个大写字母
for i in range(65,91):
    a = str(chr(i)) #ASXII码对应
    list.append(a)
#生成26个小写字母
for i in range(97,123):
    a = str(chr(i))
    list.append(a)
#生成10个数字
for i in range(10):
    list.append(str(i))
#生成16位激活码 的两种方式
def random_code():
    s = ''
    for i in range(16):
        a = random.choice(list)
        s = s + a
    print(s)
def code_random():
    
    a = random.sample(list,16)
    a = '-'.join(a)
    print(a)
# 生成200个激活码
for i in range(200):
    random_code()
    code_random()
