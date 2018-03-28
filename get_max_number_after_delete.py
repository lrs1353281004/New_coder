# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:33:02 2018
给定一个十进制的正整数number，选择从里面去掉一部分数字，希望保留下来的数字组成的正整数最大。
输入为两行内容，第一行是正整数number，1 ≤ length(number) ≤ 50000。第二行是希望去掉的数字数量cnt 1 ≤ cnt < length(number)。
@author: Li Ruosong
"""
n='7654321'
k=3
def get_max_after_del(n,k):
    str_n=[i for i in n]
    for j in range(0,k):
        for i in range(0,len(str_n)):
            if i==len(str_n)-1 or str_n[i]<str_n[i+1]  :
                del str_n[i]
                break
    return ''.join(str_n)

print(get_max_after_del(n,k))          
            
        
        
    
