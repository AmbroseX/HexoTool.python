# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchBlog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(382, 624)
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_SearchContent = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_SearchContent.setObjectName("listWidget_SearchContent")
        self.verticalLayout.addWidget(self.listWidget_SearchContent)
        self.pushButton_OpenChooseContent = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OpenChooseContent.setObjectName("pushButton_OpenChooseContent")
        self.verticalLayout.addWidget(self.pushButton_OpenChooseContent)
        SearchWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 23))
        self.menubar.setObjectName("menubar")
        SearchWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "SearchBlog"))
        self.pushButton_OpenChooseContent.setText(_translate("SearchWindow", "Open"))

