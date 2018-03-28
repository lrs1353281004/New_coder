# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 10:26:10 2018
假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，
如果我们把该编码按字典序排序，形成一个数组如下：
 a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy
 其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 
 编写一个函数，输入是任意一个编码，输出这个编码对应的Index.
 输入一个待编码的字符串,字符串长度小于等于100.
 输出这个编码的index
@author: Li Ruosong
"""
def Get_dic_sort_number(s):
    if not s or len(s)>4 :
        return False
    res = 0
    for i in range(0,len(s)):
        temp = 0
        for j in range(0,4-i):
            temp += 25**j
        if i==0:
            res += (ord(s[i])-ord('a'))*temp
        else:
            res += (ord(s[i])-ord('a'))*temp+1
        
    return res

res = Get_dic_sort_number('aa')
        
