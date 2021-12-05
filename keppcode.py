import threading
import subprocess
import time
import os

from git import Repo
from lib.FileAction import quotes_str

def getdesk(path:str):
    return path.split("\\")[0]  # 获取博客所在盘符

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
                repo.remote().pull()  #拉取代码
                print(self.path)
                isdiff = repo.is_dirty()
                if len(repo.untracked_files) != 0 or isdiff == True:
                    print("有文件不同")
                    cmd1 = getdesk(self.path)
                    print(cmd1)
                    cmd2 = 'cd '+self.path
                    print(cmd2)
                    cmd_gitadd = 'git add --all'
                    print(cmd_gitadd)
                    cmd_commit = 'git commit -m '+quotes_str(self.Commit)
                    self.logCommit = cmd_commit
                    print(cmd_commit)
                    git_push = 'git push'
                    cmdall1 = cmd1 + ' && '+cmd2+' && '+cmd_gitadd+' && '+cmd_commit
                    child1 = subprocess.call(cmdall1, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,close_fds=True)
                    print(cmdall1)
                    cmdall2 = cmd1 + ' && '+cmd2+' && '+cmd_gitadd+' && '+git_push
                    child12 = subprocess.call(cmdall2, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, close_fds=True)
                    print(cmdall2)
                    #os.system(cmdall2)
                    print("push success!")
                    self.setFlag(False)
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


# 多线程操作来Push到GitHub
dirfile = 'G:\Data\MyBlog\Tools\HexoTool.python'


repo = Repo(dirfile)
#repo.remote().pull()
print(repo.active_branch)

g = repo.git
g.add("--all")
g.commit("-m auto update")
g.push()
print("Successful push!")

#dirfile = 'G:\Data\MyBlog\source_blog'
#dirfile = os.path.abspath('') # code的文件位置，我默认将其存放在根目录下

#AutoPuShGihub = MyGitThread()  # 实例化多线程对象
#AutoPuShGihub.setDaemon(True)  # 保护线程，主进程结束会关闭线程
#AutoPuShGihub.setPath(dirfile)  # 设置Push的博客本地
#print(AutoPuShGihub.is_alive())
#AutoPuShGihub.start()

#AutoPuShGihub.setFlag(False)
#time.sleep(2)
#print(AutoPuShGihub.is_alive())

