# -*- coding: utf-8 -*-

import yaml




def readtxt(filename):
    with open(filename, "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        return(data)  #返回读取内容

def time2num(time):
    time = time.split(":", maxsplit=-1)  # 0,1,2,3
    if len(time) > 2:
        s = int(time[2])
    else:
        s = 0
    h = int(time[0])
    m = int(time[1])
    return h, m, s



# print(time2num("10:00"))



