__author__ = 'Rong_kang_Xiong'
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "lib"))  #添加lib
sys.path.append(os.path.join(os.getcwd(), "QtUI"))  #添加UI的路径

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from lib.mainButton import mainButton



if __name__== '__main__':
    pwd = os.getcwd()  #获取当前路径
    print("当前路径 = "+pwd)
    app = QApplication(sys.argv)
    MainWindow = mainButton()
    MainWindow.setWindowIcon(QIcon(os.path.join(pwd, "img","logo.svg")))  #添加窗口图标

    MainWindow.show()
    sys.exit(app.exec_())
