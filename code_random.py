# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:06:58 2018

@author: wei
"""

import random,string
#取值范围
field = string.ascii_letters + string.digits
#生成激活码
def random_code():
    return '-'.join(''.join(random.sample(field,4)) for i in range(4))

for i in range(200):
     print(random_code())