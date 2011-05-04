# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sun Sep 13 19:52:15 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(340, 460)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.list = QtGui.QTreeWidget(self.centralwidget)
        self.list.setObjectName("list")
        self.horizontalLayout.addWidget(self.list)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 340, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Task", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Tags", None, QtGui.QApplication.UnicodeUTF8))

