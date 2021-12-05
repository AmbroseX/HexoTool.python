
# #for push to github
# commitrepo = self.lineEdit_Add_Commit.text()
# #print(commitrepo)
# repo = Repo(blog_position)
# g = repo.git
# print("blog位置" + blog_position)
# isdiff = repo.is_dirty()
# if len(repo.untracked_files) != 0 or isdiff == True:
#     if commitrepo == __config__["Other"]["CommitInfo"]:  # 没有Commit 改变
#         print("自动添加Commit")
#         self.show_msg("自动添加Commit")
#         print(self.AutoPuShGihub.path)
#         self.AutoPuShGihub.setCommit(ctime())  # 添加此时的时间
#     else:
#         self.PushGihubThread.setCommit(commitrepo)
#     self.AutoPuShGihub.start()
#     print("Begin Push to Github")
#     self.show_msg("Begin Push to Github")
#     self.AutoPuShGihub.setFlag(False)  # 修改线程运行状态，关闭线程
#     print("Push success")
#     self.show_msg("Push success")
#     # self.show_msg("线程是否还在运行:"+self.AutoPuShGihub.is_alive())  # 查看线程运行状态
#     self.show_msg(self.AutoPuShGihub.Commit)
# else:
#     self.show_msg("没有新的内容需要上传")
#     print("没有新的内容需要上传")
#     # self.setFlag(False)  # 关闭线程


# pwd = os.getcwd()  # 获取当前路径
# print("当前路径 = " + pwd)
# AutoGitPath = os.path.join(pwd, 'lib', 'autogit.py')
# print(AutoGitPath)
# cmd = 'python ' + AutoGitPath
# os.system(cmd)

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
                IsDiff = repo.is_dirty()
                if len(repo.untracked_files) != 0 or IsDiff == True:
                    print("有文件不同")
                    g.add("--all")
                    print('add success')
                    g.commit("-m " + quotes_str(self.Commit))
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
                    print("没有需要上传的文件")
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