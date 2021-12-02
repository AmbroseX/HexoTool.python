__author__ = 'Rong_kang_Xiong'
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "lib"))  #添加lib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime
from PyQt5 import QtWidgets, QtCore
from QtUI.HexoTools import Ui_MainWindow  #导入生成的py文件的类 Ui_MainWindow
from lib import config


class mainButton(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mainButton, self).__init__(parent)
        self.setupUi(self)

        #将相应函数绑定到Button
        self.show_comand.clicked.connect()



    def show_msg(self, msg):   #在消息框中输出消息
        if not isinstance(msg, str):
            self.Show_message.append("参数非字符串")
        else:
            # msg = '\n'+msg +'\n'+str(self.getCurrentDateTime())  #空一行再写入消息
            msg = '\n'+msg + '\n'+'消息时间:'+self.DateTime2str(self.getCurrentDateTime(), 6)
            self.Show_message.append(msg)

    def show_Date(self, date):   #显示日期
        self.show_msg("日期:"+date.toString("yyyy-MM-dd"))
        # return date.toString("yyyy-MM-dd")

    #时间改变时显示信息
    def onTimeChanged(self, time):
        self.time = time.toString('hh:mm')
        self.show_msg(time.toString('hh:mm'))

    #日期改变时显示信息
    def onDateChanged(self, date):
        # 年:月:日 [星期]
        self.date = date.toString('yyyy/MM/dd')
        self.show_msg(self.date)
        self.show_msg(date.toString('yyyy/MM/dd [ddd]'))

    #时间日期改变时显示信息
    def onDateTimeChanged(self, dateTime):
        self.datetime = dateTime.toString('yyyy/MM/dd, hh:mm:ss')
        self.show_msg(dateTime.toString('yyyy:MM:dd [ddd] hh:mm:ss'))

    def getCurrentDateTime(self):   #返回当前时间(0,1,2,3)
        #获得当前时间
        timestr = str(QDateTime.currentDateTime())
        timestr = timestr.replace('PyQt5.QtCore.QDateTime(', '')  #去掉左边括号和字符串
        timestr = timestr.replace(')', '')   #去掉右边括号和字符串
        timestr = timestr.split(',', maxsplit=-1)
        for i in range(len(timestr)):
            timestr[i] = timestr[i].rstrip()
            timestr[i] = timestr[i].lstrip()
        return timestr

    def QtDate2str(self, arg):   #返回PyQt5.QtCore.QDate(2021, 7, 31)形式日期的字符串list
        timestr = str(arg)
        timestr = timestr.replace('PyQt5.QtCore.QDate(', '')  # 去掉左边括号和字符串
        timestr = timestr.replace(')', '')  # 去掉右边括号和字符串
        timestr = timestr.split(',', maxsplit=-1)
        for i in range(len(timestr)):
            timestr[i] = timestr[i].rstrip()
            timestr[i] = timestr[i].lstrip()
        return timestr

    def QtTime2ampm(self, arg):  #10:00:00
        time = str(arg)
        time = time.split(':', maxsplit=-1)
        if int(time[0])<12:
            ampm = 'am'
        else:
            ampm = 'pm'
        return time[0]+':'+time[1]+ampm

    def DateTime2str(self, DateTime, dtlen = 7):  #将时间转换为字符串 例如2021/7/23/19/20/05/345
        dtstr = ''
        if dtlen > len(DateTime):
            dtlen = len(DateTime)
        else:
            for i in range(dtlen):
                if i == 0:
                    dtstr = dtstr + DateTime[i]
                else:
                    dtstr = dtstr + r'/' + DateTime[i]
        return dtstr


    def default_config(self, arg):
        return config.get(arg)

    def open_file(self, arg):
        '''
        fileName = 'G:/Data/WenLab/JC_Update/SD.pdf'
        fileType = '*.pdf'
        '''
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "All Files(*.pdf)")
        self.rawPDF = fileName
        #复制文件到目录
        self.show_msg("选择文件："+self.rawPDF)
        self.show_msg("坚果云路径：" + config.get(arg))

        return fileName

    def button_press_show_comand(self):
        '''
        显示常用hexo命令
        '''
        self.show_msg(default_config("常用命令"))







    #清空消息日志
    def btnpress_clear_log_1(self):
        self.text_paper_Browser_1.setPlainText('')

    def btnpress_clear_log_2(self):
        self.text_paper_Browser_2.setPlainText('')

    def btnpress_clear_log_3(self):
        self.text_paper_Browser_2.setPlainText('')
    # def update_JC(self):

    def clearAllInfo(self):
        #清除窗口
        self.DOI_1.setPlainText('')
        self.title_1.setPlainText('')
        self.Presenter_1.setPlainText('')
        self.URL_link_1.setPlainText('')
        self.PDF_link_1.setPlainText('')
        self.text_JC_Browser_1.setPlainText('')
        self.text_paper_Browser_1.setPlainText('')

        self.DOI_2.setPlainText('')
        self.title_2.setPlainText('')
        self.Presenter_2.setPlainText('')
        self.URL_link_2.setPlainText('')
        self.PDF_link_2.setPlainText('')
        self.text_JC_Browser_2.setPlainText('')
        self.text_paper_Browser_2.setPlainText('')

        self.workreport_3.setPlainText('')
        self.Presenter_3.setPlainText('')
        self.text_paper_Browser_3.setPlainText('')
        #清除变量
        self.Presenter = ''
        self.title = ''
        self.authors = ''
        self.URLLink = ''
        self.rawPDF = ''
        self.PDFLink = ''
        self.date = ''
        self.time = ''
        self.datetime = ''
        self.location = ''
        self.doidic = []  # Bibtex
        self.ymlall = []
        self.ymlnew = {}
