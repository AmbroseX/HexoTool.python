# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Common_Commands.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CommondCommands(object):
    def setupUi(self, CommondCommands):
        CommondCommands.setObjectName("CommondCommands")
        CommondCommands.resize(467, 609)
        self.centralwidget = QtWidgets.QWidget(CommondCommands)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser_Show_Command = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_Show_Command.setObjectName("textBrowser_Show_Command")
        self.gridLayout.addWidget(self.textBrowser_Show_Command, 0, 0, 1, 1)
        CommondCommands.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CommondCommands)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 23))
        self.menubar.setObjectName("menubar")
        CommondCommands.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CommondCommands)
        self.statusbar.setObjectName("statusbar")
        CommondCommands.setStatusBar(self.statusbar)

        self.retranslateUi(CommondCommands)
        QtCore.QMetaObject.connectSlotsByName(CommondCommands)

    def retranslateUi(self, CommondCommands):
        _translate = QtCore.QCoreApplication.translate
        CommondCommands.setWindowTitle(_translate("CommondCommands", "Hexo常用命令查询"))

