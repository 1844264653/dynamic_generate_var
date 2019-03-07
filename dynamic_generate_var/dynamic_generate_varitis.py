#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 22:56
# @Author  : 海心
# @Site    : 
# @File    : dynamic_generate_varitis.py
# @Software: PyCharm
# @descri  :  比较简单

cr = locals()
l = range(1,10)
for i,s in enumerate(l):
    cr['a'+str(i)] = s
print(a1,a2,a3, type(a1))