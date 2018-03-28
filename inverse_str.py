# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:04:59 2018
倒置字符串
将一句话的单词进行倒置，标点不倒置。比如 I like beijing. 经过函数后变为：beijing. like I
@author: Li Ruosong
"""
or_str=input().strip()
str_list=or_str.split(' ')
res=''
for i in range(0,len(str_list)):
    if i == 0:
        res += str_list[-i-1]
    else:
        res +=' '+ str_list[-i-1]
print(res)
