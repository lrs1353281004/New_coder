# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:13:34 2018
优雅的点
小易有一个圆心在坐标原点的圆，小易知道圆的半径的平方。
小易认为在圆上的点而且横纵坐标都是整数的点是优雅的，小易现在想寻找一个算法计算出优雅的点的个数，请你来帮帮他。
例如：半径的平方如果为25
优雅的点就有：(+/-3, +/-4), (+/-4, +/-3), (0, +/-5) (+/-5, 0)，一共12个点。
@author: Li Ruosong
"""

import math
n=input()
def Get_elegant_point_numbers(r2):
    r2 = float(r2)
    if r2 == 0 :
        return 0
    r = int(math.sqrt(r2))
    count=0
    if r == math.sqrt(r2) :
        count += 4
    res=[]
    for i in range(1,r):
        flag = math.sqrt(r2 - i**2)
        if int(flag) == flag :
            res.append(int(flag))
            res.append(i)
    return count+len(set(res))*4
print(Get_elegant_point_numbers(n))
        
    
