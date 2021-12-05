import threading
import time
from git import Repo
from FileAction import readymldir

__config__ = readymldir('config.yml')

def getdesk(path: str):
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

    # 线程的函数
    def run(self):
        while (True):
            if (not self.Flag):  # 关闭的话
                break
            else:
                repo = Repo(self.path)
                g = repo.git
                print(self.path)
                isdiff = repo.is_dirty()
                if len(repo.untracked_files) != 0 or isdiff == True:
                    g.add("--all")
                    print('add success')
                    g.commit("-m "+self.Commit)
                    print("Successful Commit!")
                    g.push()
                    print("Successful push!")

                else:
                    print("代码未改变")
                    self.setFlag(False)  # 关闭线程

    def setFlag(self, parm: bool):  # 外部停止线程的操作函数 True开始执行，False关闭进程
        self.Flag = parm  # boolean

    def setPath(self, parm: str):
        self.path = parm  # 设置路径

    def setCommit(self, parm: str):
        # 设置Commit内容
        self.Commit = parm

    def getCommit(self):
        return self.Commit



#print(__config__)

# blog_position = __config__["BlogInfo"]["blog_position"]
#
# print(blog_position)
#
# cmd_gotoblogfolder = 'cd '+blog_position
# blog_disk = blog_position.split("\\")[0]  #获取博客所在盘符
# print(blog_disk)

# dirfile = blog_position
dirfile = 'G:\Data\MyBlog\Tools\HexoTool.python'

# repo = Repo(dirfile)
# print(repo.active_branch)

# dirfile = 'G:\Data\MyBlog\source_blog'
# # dirfile = os.path.abspath('') # code的文件位置，我默认将其存放在根目录下
#
#
# 多线程操作来Push到GitHub

AutoPuShGihub = MyGitThread()  # 实例化多线程对象
AutoPuShGihub.setDaemon(True)  # 保护线程，主进程结束会关闭线程
AutoPuShGihub.setPath(dirfile)  # 设置Push的博客本地
print(AutoPuShGihub.is_alive())
AutoPuShGihub.start()

AutoPuShGihub.setFlag(False)
time.sleep(2)
print(AutoPuShGihub.is_alive())
