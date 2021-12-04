__author__ = 'Rong_kang_Xiong'
# -*- coding: utf-8 -*-
import sys
import os
import threading
import subprocess
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
from lib.FileAction import readymldir

def open_file_path(path):
    if os.path.isdir(path):  # 目标目录存在
        cmd = 'explorer.exe ' + path
        os.system(cmd)
        return path
    else:
        return "目标目录不存在"
        print("目标目录不存在")

__config__ = readymldir("lib/config.yml")  #配置文件导入

blog_position = __config__["BlogInfo"]["blog_position"]
cmd = 'explorer.exe ' + blog_position

open_file_path(blog_position)