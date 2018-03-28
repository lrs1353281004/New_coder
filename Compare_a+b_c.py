# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 13:03:08 2018
A+B > or < C ?
给定区间[-2的31次方, 2的31次方]内的3个整数A、B和C，请判断A+B是否大于C。
@author: Li Ruosong
"""

import sys
if __name__ == "__main__":
    cases = int(sys.stdin.readline().strip())
    cases_num=[]
    for i in range(0,cases):
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values_num = list(map(int, line.split()))
        cases_num.append(values_num)

#cases_num=[[1,24,4],[3,5,77],[2,2,2],[2,4,6]]
for i in range(0,cases):
    if (cases_num[i][0]+cases_num[i][1])>cases_num[i][2] :
        flag = 'true'
    else:
        flag = 'false'
    print('Case #%d: %s'%(i+1,flag))
    