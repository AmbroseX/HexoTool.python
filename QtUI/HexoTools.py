# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HexoTools.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choose_blog_position = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_blog_position.sizePolicy().hasHeightForWidth())
        self.choose_blog_position.setSizePolicy(sizePolicy)
        self.choose_blog_position.setObjectName("choose_blog_position")
        self.horizontalLayout.addWidget(self.choose_blog_position)
        self.open_blog_position = QtWidgets.QPushButton(self.centralwidget)
        self.open_blog_position.setObjectName("open_blog_position")
        self.horizontalLayout.addWidget(self.open_blog_position)
        self.show_comand = QtWidgets.QPushButton(self.centralwidget)
        self.show_comand.setObjectName("show_comand")
        self.horizontalLayout.addWidget(self.show_comand)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.open_github = QtWidgets.QPushButton(self.centralwidget)
        self.open_github.setObjectName("open_github")
        self.horizontalLayout_3.addWidget(self.open_github)
        self.open_gitee = QtWidgets.QPushButton(self.centralwidget)
        self.open_gitee.setObjectName("open_gitee")
        self.horizontalLayout_3.addWidget(self.open_gitee)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.build_new = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.build_new.sizePolicy().hasHeightForWidth())
        self.build_new.setSizePolicy(sizePolicy)
        self.build_new.setMaximumSize(QtCore.QSize(16777215, 50))
        self.build_new.setObjectName("build_new")
        self.verticalLayout.addWidget(self.build_new)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_search_blog = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_search_blog.setEnabled(True)
        self.lineEdit_search_blog.setMouseTracking(True)
        self.lineEdit_search_blog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_search_blog.setAcceptDrops(True)
        self.lineEdit_search_blog.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_search_blog.setInputMask("")
        self.lineEdit_search_blog.setText("")
        self.lineEdit_search_blog.setFrame(True)
        self.lineEdit_search_blog.setDragEnabled(True)
        self.lineEdit_search_blog.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_search_blog.setClearButtonEnabled(True)
        self.lineEdit_search_blog.setObjectName("lineEdit_search_blog")
        self.horizontalLayout_4.addWidget(self.lineEdit_search_blog)
        self.search_blog = QtWidgets.QPushButton(self.centralwidget)
        self.search_blog.setObjectName("search_blog")
        self.horizontalLayout_4.addWidget(self.search_blog)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.Show_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.Show_message.setEnabled(True)
        self.Show_message.setMouseTracking(True)
        self.Show_message.setObjectName("Show_message")
        self.verticalLayout.addWidget(self.Show_message)
        self.clear_log = QtWidgets.QPushButton(self.centralwidget)
        self.clear_log.setObjectName("clear_log")
        self.verticalLayout.addWidget(self.clear_log)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_port = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_port.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.verticalLayout.addWidget(self.lineEdit_port)
        self.open_local_debug = QtWidgets.QPushButton(self.centralwidget)
        self.open_local_debug.setObjectName("open_local_debug")
        self.verticalLayout.addWidget(self.open_local_debug)
        self.close_local_debug = QtWidgets.QPushButton(self.centralwidget)
        self.close_local_debug.setObjectName("close_local_debug")
        self.verticalLayout.addWidget(self.close_local_debug)
        self.lineEdit_Add_Commit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Add_Commit.setText("")
        self.lineEdit_Add_Commit.setObjectName("lineEdit_Add_Commit")
        self.verticalLayout.addWidget(self.lineEdit_Add_Commit)
        self.Push_Github = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Push_Github.sizePolicy().hasHeightForWidth())
        self.Push_Github.setSizePolicy(sizePolicy)
        self.Push_Github.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.Push_Github.setObjectName("Push_Github")
        self.verticalLayout.addWidget(self.Push_Github)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HexoBlogTool"))
        self.choose_blog_position.setText(_translate("MainWindow", "选择博客位置"))
        self.open_blog_position.setText(_translate("MainWindow", "打开博客目录"))
        self.show_comand.setText(_translate("MainWindow", "常用命令显示"))
        self.open_github.setText(_translate("MainWindow", "打开GtHub"))
        self.open_gitee.setText(_translate("MainWindow", "打开Gitee"))
        self.build_new.setText(_translate("MainWindow", "新建文章"))
        self.search_blog.setText(_translate("MainWindow", "搜索博客"))
        self.clear_log.setText(_translate("MainWindow", "清空日志"))
        self.label.setText(_translate("MainWindow", "本地调试Port"))
        self.lineEdit_port.setText(_translate("MainWindow", "4000"))
        self.open_local_debug.setText(_translate("MainWindow", "打开本地调试"))
        self.close_local_debug.setText(_translate("MainWindow", "关闭本地调试"))
        self.Push_Github.setText(_translate("MainWindow", "打开GitHubDesktop进行上传"))

