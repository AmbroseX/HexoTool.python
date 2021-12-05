__author__ = 'Rong_kang_Xiong'
# -*- coding: utf-8 -*-
import sys
import os
import threading
import subprocess
sys.path.append(os.path.join(os.getcwd(), "lib"))  #添加lib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject , pyqtSignal


from QtUI.SearchBlog import Ui_SearchWindow #导入生成的py文件的类 Ui_BuildWindow
from functools import partial
from openUrl import openurl
from lib.FileAction import readymldir

import requests
from bs4 import BeautifulSoup


__config__ = readymldir("lib/config.yml")  #配置文件导入

blog_position = __config__["BlogInfo"]["blog_position"]
cmd_gotoblogfolder = 'cd '+blog_position
blog_disk = blog_position.split("\\")[0]  #获取博客所在盘符


class SearchButton(QMainWindow, Ui_SearchWindow):
    signal_search = pyqtSignal(str)  #子界面类创建信号用来绑定主界面类的函数方法

    def __init__(self, parent = None):
        super(SearchButton, self).__init__(parent)
        self.setupUi(self)

        #最小化打开Everything确保能搜索正确
        cmd = 'cmd /c start /min "" ' + __config__["ToolsPath"]["Everything"]  # 'F:\Everything\Everything.exe'
        os.system(cmd)

        self.pushButton_OpenChooseContent.clicked.connect(self.button_press_OpenChooseContent)
        self.listWidget_SearchContent.itemClicked.connect(self.SearchitemClicked)


    def SearchitemClicked(self,item):
        self.Chooseitem = item.text()
        self.emit_signal("你选择了文件:"+self.Chooseitem)

    def get_signal(self,signal):
        self.signal_search_from_main = signal
        self.searchContent = self.ShowSearchContent(self.signal_search_from_main)
        self.listWidget_SearchContent.clear()
        self.listWidget_SearchContent.addItems(self.searchContent)
        # 子界面通过signal_2 向主界面传递数据

    def emit_signal(self,signal):
        #signal = "BuilWindow signal:\n"+signal
        self.signal_search.emit(signal)

    def ShowSearchContent(self,keyword):
        blogpost = os.path.join(blog_position, 'source')
        urlpath = SpecialPathContent2Url(blogpost)
        print(urlpath)
        content = findit(urlpath,keyword)
        return content

    def button_press_OpenChooseContent(self):
        self.chooseContent = self.Chooseitem
        cmd = 'cmd /c start '+ self.chooseContent
        os.system(cmd)

        #print(self.chooseContent)

    # 检测键盘回车按键
    def keyPressEvent(self, QkeyEvent):
        print("按下：" + str(QkeyEvent.key()))
        if(QkeyEvent.key() == 16777220):  #敲击回车
            self.button_press_OpenChooseContent()



def findit(path,text):
    request = requests.get("http://"+path+text)
    content = request.text
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    items = soup.find_all("tr", {'class': 'trdata1'})
    title = []
    source = []
    if items:

        for i in range(len(items)):
            filename = str(items[i].find("a").text)
            title.append(filename)
            source.append(items[i].find_all("nobr")[2].text + "/" + filename)
    items = soup.find_all("tr", {'class': 'trdata2'})
    #print(source)
    return source


def SpecialPathContent2Url(path):
    disk = path.split("\\")[0]  #获取路径所在盘符
    disk0 = disk.split(":")[0]
    urlpath = "localhost/"+"?search="+disk0+"%3A"
    for item in path.split("\\"):
        if item != path.split("\\")[0]:
            urlpath = urlpath+"%5C"+item
    urlpath = urlpath+"+content%3A"
    return urlpath

