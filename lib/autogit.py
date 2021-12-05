import threading
import time
from git import Repo
from FileAction import readymldir
import inspect
import ctypes




def getdesk(path: str):
    return path.split("\\")[0]  # 获取博客所在盘符


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


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
                    time.sleep(1.5)
                    g.push()
                    print("Successful push!")

                else:
                    print("没有新的需要上传")
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


__config__ = readymldir('config.yml')

#print(__config__)

blog_position = __config__["BlogInfo"]["blog_position"]

#print(blog_position)

cmd_gotoblogfolder = 'cd '+blog_position
blog_disk = blog_position.split("\\")[0]  #获取博客所在盘符
#print(blog_disk)

# dirfile = blog_position
dirfile = 'G:\Data\MyBlog\Tools\HexoTool.python'



# 多线程操作来Push到GitHub
AutoPuShGihub = MyGitThread()  # 实例化多线程对象
AutoPuShGihub.setDaemon(True)  # 保护线程，主进程结束会关闭线程
AutoPuShGihub.setPath(dirfile)  # 设置Push的博客本地
print(AutoPuShGihub.is_alive())
AutoPuShGihub.start()

AutoPuShGihub.setFlag(False)
time.sleep(2)
print(AutoPuShGihub.is_alive())
stop_thread(AutoPuShGihub)
time.sleep(2)
print(AutoPuShGihub.is_alive())
