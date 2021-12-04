__author__ = 'Rong_kang_Xiong'
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "lib"))  #添加lib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject , pyqtSignal


from QtUI.Build_new import Ui_BuildWindow #导入生成的py文件的类 Ui_BuildWindow
from functools import partial
from openUrl import openurl
from lib.FileAction import readymldir
from lib.SearchFile import search_files,from_list_get_filename


__config__ = readymldir("lib/config.yml")  #配置文件导入
blog_position = __config__["BlogInfo"]["blog_position"]
cmd_gotoblogfolder = 'cd '+blog_position
blog_disk = blog_position.split("\\")[0]  #获取博客所在盘符


class BuildButton(QMainWindow, Ui_BuildWindow):
    signal_build = pyqtSignal(str)  #子界面类创建信号用来绑定主界面类的函数方法

    def __init__(self, parent = None):
        super(BuildButton, self).__init__(parent)
        self.setupUi(self)

        #初始化信号传递
        self.signal_from_main = 'None'
        #初始化下拉菜单
        self.essay_type.addItems(get_blog_type(os.path.join(__config__["BlogInfo"]["blog_position"], "scaffolds")))
        self.essay_type.currentIndexChanged.connect(self.selectionchange)  #下拉菜单改变时触发绑定事件
        self.essay_type.setCurrentIndex(3) #设置为最后一项为默认值

        #选择缩略图
        self.choose_img.clicked.connect(self.Button_press_choose_img)
        #
        self.open_essay.clicked.connect(self.Button_press_open_essay)



    def executeCommand(self,cmd):
        try:
            os.system(command=cmd)
        except Exception as e:
            self.show_msg(cmd+" 命令错误")


    def titleOnChanged(self,text):
        self.lineEdit_filename.setText(text)


#建立新文章
    def Button_press_open_essay(self):
        title = self.lineEdit_title.text()
        cmd1 = blog_disk # 切换到对应的盘路径
        cmd2 = cmd_gotoblogfolder  # 切换对应路径
        cmd3 = 'hexo new '+self.essay_type.currentText()+' '+title # 执行hexo new
        cmdall = cmd1 + " && " + cmd2+" && "+cmd3
        os.system(cmdall)

    def selectionchange(self,i):
        # 标签用来显示选中的文本
        # currentText()：返回选中选项的文本
        emitsignal = "新建文章类型为："+self.essay_type.currentText()
        self.emit_signal(emitsignal)
        #print(self.essay_type.currentText())


    def Button_press_choose_img(self):
        self.emit_signal(self.signal_from_main)
        #self.signal_from_main = self.signal_build
        print(self.signal_from_main+"ceshi")
        #self.signal_build.emit("ceshi")

    def get_signal(self,signal):
        self.signal_from_main = signal
        # 子界面通过signal_2 向主界面传递数据

    def emit_signal(self,signal):
        #signal = "BuilWindow signal:\n"+signal
        self.signal_build.emit(signal)

    # 检测键盘回车按键
    def keyPressEvent(self, QkeyEvent):
        print("按下：" + str(QkeyEvent.key()))
        if(QkeyEvent.key() == 16777220):  #敲击回车
            title = self.lineEdit_title.text()
            if len(title) == 0:
                self.emit_signal("文章标题为空")
            else:
                if title.isspace() == True:
                    self.emit_signal("文章标题不能全为空格")
                else:
                    self.Button_press_open_essay()






def get_blog_type(path):
    template_file_list = search_files(path)
    #print(template_file_list)
    template_file_name = from_list_get_filename(template_file_list)
    return template_file_name
    #print(template_file_name)




