# -*- coding: utf-8 -*-
def get(arg):
    config = {}
    config['blog_posion'] = r'G:\Data\MyBlog\source_blog'
    config['常用命令'] = ""
    return config[arg]


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



