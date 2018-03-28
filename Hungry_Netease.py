# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:26:42 2018
小易总是感觉饥饿，所以作为章鱼的小易经常出去寻找贝壳吃。最开始小易在一个初始位置x_0。
对于小易所处的当前位置x，他只能通过神秘的力量移动到 4 * x + 3或者8 * x + 7。
因为使用神秘力量要耗费太多体力，所以它只能使用神秘力量最多100,000次。贝壳总生长在能被1,000,000,007整除的位置
(比如：位置0，位置1,000,000,007，位置2,000,000,014等)。小易需要你帮忙计算最少需要使用多少次神秘力量就能吃到贝壳。
@author: Li Ruosong
"""
def Hungry_netease_eating(x_in):
    res=0
    x1= x_in
    x2= 4*x1 + 3
    x3= 4*x2 + 3
    while res < 100000 :
        f1 = x1 % 1000000007
        f2 = x2 % 1000000007
        f3 = x3 % 1000000007
        if f1 == 0 :
            return res 
        elif f2 == 0 :
            return res+1
        elif f3 == 0 :
            return res+2
        x1 = 8*f1 +7
        x2 = 8*f2 +7
        x3 = 8*f3 +7
        res += 1
    return -1
x_in = 125000000
res  = Hungry_netease_eating(x_in)
        
      
            
        

