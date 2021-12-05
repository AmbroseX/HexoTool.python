__author__ = 'Rong_kang_Xiong'
# -*- coding: utf-8 -*-
import sys
import os
from time import ctime
import threading
import subprocess
from git import Repo
sys.path.append(os.path.join(os.getcwd(), "lib"))  #添加lib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject , pyqtSignal

from QtUI.HexoTools import Ui_MainWindow  #导入生成的py文件的类 Ui_MainWindow
from lib.BuildButton import BuildButton
from lib.PortAction import killPortAllPID

from functools import partial
from lib.openUrl import openurl
from lib.FileAction import readymldir,open_file_path,quotes_str



__config__ = readymldir("lib/config.yml")  #配置文件导入

blog_position = __config__["BlogInfo"]["blog_position"]
cmd_gotoblogfolder = 'cd '+blog_position
blog_disk = blog_position.split("\\")[0]  #获取博客所在盘符
print(blog_disk)


class mainButton(QMainWindow, Ui_MainWindow):
    signal_main = pyqtSignal(str) #主界面的信号用来绑定子界面类的函数方法

    def __init__(self, parent = None,):
        super(mainButton, self).__init__(parent)
        self.setupUi(self)


        #初始化参数
        self.pwd = os.getcwd()  # 获取当前路径

        #将相应函数绑定到Button
        self.show_comand.clicked.connect(self.button_press_show_comand)  #显示常用命令
        self.open_gitee.clicked.connect(partial(self.openlink,__config__["BlogInfo"]["gitee"]))  #绑定点击打开gitee
        self.open_github.clicked.connect(partial(self.openlink,__config__["BlogInfo"]["github"]))  #绑定点击打开github
        self.choose_blog_position.clicked.connect(self.button_press_choose_blog_position)  #点击选择博客路径
        self.open_blog_position.clicked.connect(self.button_press_open_blog_path)  #打开博客路径

        self.clear_log.clicked.connect(self.button_press_clear_log)  # 清空消息日志

        #多线程操作来打开本地Server
        self.OpenServer = MyThread()  #实例化多线程对象
        self.OpenServer.setDaemon(True) #保护线程，主进程结束会关闭线程
        self.open_local_debug.clicked.connect(self.button_press_open_local_debug)  #打开本地调试
        self.close_local_debug.clicked.connect(self.button_press_close_local_debug)  #关闭本地调试

        #多线程操作来Push到GitHub
        self.AutoPuShGihub = MyGitThread() #实例化多线程对象
        self.AutoPuShGihub.setDaemon(True) #保护线程，主进程结束会关闭线程
        self.AutoPuShGihub.setPath(blog_position)  #设置Push的博客本地
        self.Push_Github.clicked.connect(self.button_press_Push_Github)  # Push到github上面键绑定
        self.lineEdit_Add_Commit.setText(__config__["Other"]["CommitInfo"])

        #新建文章Button绑定
        self.buildWindow = BuildButton()  #实例化新建文章子界面类
        self.build_new.clicked.connect(self.button_press_build_new)  #绑定打开新建文章界面类
       #初始化信号
        self.signal_from_subwindow = 'None'
        self.signal_to_build = 'None' #发送给子界面的数据
        # 信号连接
        self.signal_main.connect(self.buildWindow.get_signal)  # 将主界面的信号和buildWindow的接受函数绑定
        self.buildWindow.signal_build.connect(self.get_signal)  # 将buildWindow的信号signal_build和主界面的get_signal连接

        #发送信号
        self.signal_main.emit(self.signal_to_build)  # 通过自己的信号向子界面传递数据。要想多传递几个值，就在emit(值1，值2） 对应到子界面get_data接受就是2个参数，即get_data(值1，值2）


    def show_msg(self, msg):  # 在消息框中输出消息
        if not isinstance(msg, str):
            self.Show_message.append("参数非字符串")
        else:
            msg = '\n' + '消息时间:' + DateTime2str(self.getCurrentDateTime(), 6) + '\n' + msg
            self.Show_message.append(msg)

    def getCurrentDateTime(self):  # 返回当前时间(0,1,2,3)
        # 获得当前时间
        timestr = str(QDateTime.currentDateTime())
        timestr = timestr.replace('PyQt5.QtCore.QDateTime(', '')  # 去掉左边括号和字符串
        timestr = timestr.replace(')', '')  # 去掉右边括号和字符串
        timestr = timestr.split(',', maxsplit=-1)
        for i in range(len(timestr)):
            timestr[i] = timestr[i].rstrip()
            timestr[i] = timestr[i].lstrip()
        return timestr




    def openlink(self,url):
        print(type(url))
        print(url)
        #self.show_msg(url)
        #self.show_msg("Oprn link:" + url)
        openurl(url)

    def button_press_choose_blog_position(self):
        blog_path=QFileDialog.getExistingDirectory(self,"选择你的博客的目录","C:")
        self.show_msg("你选择的博客路径为:\n"+blog_path)
        print(blog_path)

    def button_press_open_blog_path(self):
        path = open_file_path(__config__["BlogInfo"]["blog_position"])
        self.show_msg("打开路径"+path)

    def button_press_show_comand(self):
        '''
        打开另一个窗口，显示常用hexo命令
        '''

    # 打开git bash执行命令然后打开，本地http://localhost:4000/调试

    def localurl(self):
        local_server = "http://localhost:" + self.OpenServer.getPort() + "/"
        return local_server

    def button_press_open_local_debug(self):
        import subprocess
        # 先检查当前端口是否被占用了
        from lib.PortAction import CheckPort
        result = CheckPort(self.lineEdit_port.text())
        if result == False:
            self.show_msg("端口"+self.lineEdit_port.text()+"没有部署")
        else:
            self.show_msg(result)
        #print(result)
        if result == False:
            self.show_msg("尝试打开端口:"+self.lineEdit_port.text())
            try:
                self.OpenServer.setPort(self.lineEdit_port.text())    #传入端口值
                self.OpenServer.setTurnOnOff(1)  #修改线程内部值
                self.OpenServer.start() #开始线程
                self.show_msg("Open"+self.localurl())
                self.show_msg("localhost open success")
            except KeyboardInterrupt:
                self.show_msg(__config__["CompleteTip"]["server_done_text"])
        else:
            self.show_msg("当前端口:"+ self.lineEdit_port.text()+" 已打开")
            openurl(self.localurl())
            self.show_msg("open " + self.localurl() + " success")


    def button_press_close_local_debug(self):
        result = killPortAllPID(self.OpenServer.port)
        self.OpenServer.setFlag(False)
        print(self.OpenServer.is_alive())
        if result == False:
            self.show_msg("当前端口:"+self.lineEdit_port.text()+" 没有运行")
        self.show_msg("kill port \n" + result + '\n kill success!')

    # 显示第二个窗口来创建文章
    def button_press_build_new(self):
        # 点击按钮后会打开新的窗口
        self.buildWindow.setWindowIcon(QIcon(os.path.join(self.pwd, "img", "logo.svg")))  # 添加窗口图标
        self.buildWindow.show()
        self.show_msg("Open Build New Essay")

    #从子界面传递来的信号
    def get_signal(self,signal):
        self.signal_from_subwindow = signal
        self.show_msg(self.signal_from_subwindow)

    def emit_signal_to_build(self,signal):
        #signal = "来自Main:"+signal
        self.signal_main.emit(signal)


    # 清空消息日志
    def button_press_clear_log(self):
        #self.show_msg("ceshi")
        self.Show_message.setPlainText('')
        #self.signal_main.emit(self.signal_from_subwindow+'从main来')

    def button_press_Push_Github(self):
        pwd = os.getcwd()  # 获取当前路径
        print("当前路径 = " + pwd)
        AutoGitPath = os.path.join(pwd, 'lib', 'autogit.py')
        print(AutoGitPath)
        cmd = 'python ' + AutoGitPath
        os.system(cmd)

        # commitrepo = self.lineEdit_Add_Commit.text()
        # print(commitrepo)
        # if commitrepo == __config__["Other"]["CommitInfo"]: #没有Commit 改变
        #     print("自动添加Commit")
        #     print(self.AutoPuShGihub.path)
        #     self.PushGihubThread.setCommit(ctime())  #添加此时的时间
        # else:
        #     self.PushGihubThread.setCommit(commitrepo)
        # self.AutoPuShGihub.start()
        # self.show_msg("Begin Push to Github")
        # self.AutoPuShGihub.setFlag(False)  # 修改线程运行状态，关闭线程
        # self.show_msg("Push success")
        # #self.show_msg("线程是否还在运行:"+self.AutoPuShGihub.is_alive())  # 查看线程运行状态
        # self.show_msg(self.AutoPuShGihub.Commit)



def executeCommand(self, cmd:str):
    try:
        print(cmd)
        os.system(command=cmd)
    except Exception as e:
        print(e)
        return False
        #self.show_msg(cmd + " 命令错误")

def getdesk(path:str):
    return path.split("\\")[0]  # 获取博客所在盘符

def DateTime2str(DateTime, dtlen=7):  # 将时间转换为字符串 例如2021/7/23/19/20/05/345
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


def serverWithAnotherPort(port):
    port = __config__["HexoCommand"]["Server"] + ' -p ' + port
    return port

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.Flag = True  # 停止标志位
        self.TurnOnOff = 0  # 用来被外部访问的,0是关闭,1是开启线程
        self.port = "4000"
        self.ThreadName = "Thread-1"
        self.localport = "http://localhost:"+self.port
        # 自行添加参数

    #线程的函数
    def run(self):
        while (True):
            if (not self.Flag):
                result = killPortAllPID(self.port)
                print(self.is_alive())
                if result == False:
                    print("当前端口:", self.port, " 没有运行")
                    print("kill port \n" + result + '\n kill success!')
                break
            else:
                # 此处写你的函数操作
                cmd1 = blog_disk  # 切换到对应的盘路径
                cmd2 = cmd_gotoblogfolder
                # print(self.lineEdit_port.text())
                cmd3 = serverWithAnotherPort(self.port)  # 执行hexo s -p port
                cmdall = cmd1 + ' && ' + cmd2 + ' && ' + cmd3
                print("%s: %s" % (self.ThreadName, self.port))
                openurl("http://localhost:" + self.port + "/")
                child = subprocess.call(cmdall, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        close_fds=True)
    def setFlag(self, parm):  # 外部停止线程的操作函数
        self.Flag = parm  # boolean

    def setTurnOnOff(self, parm):  # 外部修改内部信息函数
        self.TurnOnOff = parm

    def getTurnOnOff(self):  # 外部获得内部信息函数
        return self.TurnOnOff

    def getPort(self):
        return self.port

    def setPort(self,parm):
        self.port = parm
        self.localport = self.localport = "http://localhost:"+self.port

class MyGitThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.Flag = True  # 停止标志位
        # 自行添加参数
        self.path = 'C:'
        self.ThreadName = "Thread-aoto-git"
        self.Commit = "auto update"
        self.logCommit = 'None'

    #线程的函数
    def run(self):
        while (True):
            if (not self.Flag): #关闭的话
                break
            else:
                repo = Repo(self.path)
                g = repo.git
                print(self.path)
                isdiff = repo.is_dirty()
                if len(repo.untracked_files) != 0 or isdiff == True:
                    print("有文件不同")
                    g.add("--all")
                    print('add success')
                    g.commit("-m " + self.Commit)
                    print("Successful Commit!")
                    g.push()
                    print("Successful push!")

                    # cmd1 = getdesk(self.path)
                    # print(cmd1)
                    # cmd2 = 'cd '+self.path
                    # print(cmd2)
                    # cmd_gitadd = 'git add --all'
                    # print(cmd_gitadd)
                    # cmd_commit = 'git commit -m '+quotes_str(self.Commit)
                    # self.logCommit = cmd_commit
                    # print(cmd_commit)
                    # git_push = 'git push'
                    # cmdall = cmd1 + ' && '+cmd2+' && '+cmd_gitadd+' && '+cmd_commit+' && '+git_push
                    # subprocess.call(cmdall, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
                    # #os.system(cmdall)
                    # print("push success!")
                    # self.setFlag(False)
                else:
                    print("代码未改变")
                    self.setFlag(False)  #关闭线程
    def setFlag(self, parm:bool):  # 外部停止线程的操作函数 True开始执行，False关闭进程
        self.Flag = parm  # boolean

    def setPath(self,parm:str):
        self.path = parm  #设置路径

    def setCommit(self,parm:str):
        #设置Commit内容
        self.Commit = parm

    def getCommit(self):
        return self.Commit