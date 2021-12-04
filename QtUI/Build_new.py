# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Build_new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BuildWindow(object):
    def setupUi(self, BuildWindow):
        BuildWindow.setObjectName("BuildWindow")
        BuildWindow.resize(461, 191)
        self.centralwidget = QtWidgets.QWidget(BuildWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setMaximumSize(QtCore.QSize(16777215, 31))
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.lineEdit_title = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.gridLayout.addWidget(self.lineEdit_title, 0, 1, 1, 3)
        self.toc = QtWidgets.QRadioButton(self.centralwidget)
        self.toc.setAcceptDrops(False)
        self.toc.setChecked(True)
        self.toc.setObjectName("toc")
        self.gridLayout.addWidget(self.toc, 4, 0, 1, 1)
        self.choose_img = QtWidgets.QPushButton(self.centralwidget)
        self.choose_img.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_img.sizePolicy().hasHeightForWidth())
        self.choose_img.setSizePolicy(sizePolicy)
        self.choose_img.setBaseSize(QtCore.QSize(0, 0))
        self.choose_img.setIconSize(QtCore.QSize(16, 16))
        self.choose_img.setObjectName("choose_img")
        self.gridLayout.addWidget(self.choose_img, 4, 1, 1, 3)
        self.essay_type = QtWidgets.QComboBox(self.centralwidget)
        self.essay_type.setObjectName("essay_type")
        self.gridLayout.addWidget(self.essay_type, 1, 2, 1, 2)
        self.open_essay = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_essay.sizePolicy().hasHeightForWidth())
        self.open_essay.setSizePolicy(sizePolicy)
        self.open_essay.setObjectName("open_essay")
        self.gridLayout.addWidget(self.open_essay, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        BuildWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BuildWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 23))
        self.menubar.setObjectName("menubar")
        BuildWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BuildWindow)
        self.statusbar.setObjectName("statusbar")
        BuildWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BuildWindow)
        QtCore.QMetaObject.connectSlotsByName(BuildWindow)

    def retranslateUi(self, BuildWindow):
        _translate = QtCore.QCoreApplication.translate
        BuildWindow.setWindowTitle(_translate("BuildWindow", "New Blog"))
        self.title.setText(_translate("BuildWindow", "文章标题"))
        self.toc.setText(_translate("BuildWindow", "是否设置目录toc"))
        self.choose_img.setText(_translate("BuildWindow", "选择文章缩略图"))
        self.open_essay.setText(_translate("BuildWindow", "打开文章"))
        self.label.setText(_translate("BuildWindow", "选择文章类别"))

