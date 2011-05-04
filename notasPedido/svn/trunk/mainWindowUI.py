# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Sun Sep 27 21:34:58 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 435)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sarasa = QtGui.QStackedWidget(self.centralwidget)
        self.sarasa.setFrameShape(QtGui.QFrame.NoFrame)
        self.sarasa.setFrameShadow(QtGui.QFrame.Raised)
        self.sarasa.setObjectName("sarasa")
        self.editorNotas_2 = editorNotas()
        self.editorNotas_2.setObjectName("editorNotas_2")
        self.sarasa.addWidget(self.editorNotas_2)
        self.editorProveedor = editorProveedor()
        self.editorProveedor.setObjectName("editorProveedor")
        self.sarasa.addWidget(self.editorProveedor)
        self.verticalLayout.addWidget(self.sarasa)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 25))
        self.menubar.setObjectName("menubar")
        self.menu_Nuevo = QtGui.QMenu(self.menubar)
        self.menu_Nuevo.setObjectName("menu_Nuevo")
        self.menu_Informes = QtGui.QMenu(self.menubar)
        self.menu_Informes.setObjectName("menu_Informes")
        self.menu_Ver = QtGui.QMenu(self.menubar)
        self.menu_Ver.setObjectName("menu_Ver")
        self.menu_Herramientas = QtGui.QMenu(self.menubar)
        self.menu_Herramientas.setObjectName("menu_Herramientas")
        self.menu_Acerca_de = QtGui.QMenu(self.menubar)
        self.menu_Acerca_de.setObjectName("menu_Acerca_de")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionNueva_FT = QtGui.QAction(MainWindow)
        self.actionNueva_FT.setObjectName("actionNueva_FT")
        self.actionNueva_Nota_Pedido = QtGui.QAction(MainWindow)
        self.actionNueva_Nota_Pedido.setObjectName("actionNueva_Nota_Pedido")
        self.action_NuevoProveedor = QtGui.QAction(MainWindow)
        self.action_NuevoProveedor.setObjectName("action_NuevoProveedor")
        self.action_NuevoCliente = QtGui.QAction(MainWindow)
        self.action_NuevoCliente.setObjectName("action_NuevoCliente")
        self.menu_Nuevo.addAction(self.actionNueva_FT)
        self.menu_Nuevo.addAction(self.actionNueva_Nota_Pedido)
        self.menu_Nuevo.addAction(self.action_NuevoProveedor)
        self.menu_Nuevo.addAction(self.action_NuevoCliente)
        self.menubar.addAction(self.menu_Nuevo.menuAction())
        self.menubar.addAction(self.menu_Informes.menuAction())
        self.menubar.addAction(self.menu_Ver.menuAction())
        self.menubar.addAction(self.menu_Herramientas.menuAction())
        self.menubar.addAction(self.menu_Acerca_de.menuAction())

        self.retranslateUi(MainWindow)
        self.sarasa.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Nuevo.setTitle(QtGui.QApplication.translate("MainWindow", "&Nuevo", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Informes.setTitle(QtGui.QApplication.translate("MainWindow", "&Informes", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Ver.setTitle(QtGui.QApplication.translate("MainWindow", "&Ver", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Herramientas.setTitle(QtGui.QApplication.translate("MainWindow", "&Herramientas", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Acerca_de.setTitle(QtGui.QApplication.translate("MainWindow", "&Acerca de", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva_FT.setText(QtGui.QApplication.translate("MainWindow", "Ficha de &Trabajo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva_FT.setToolTip(QtGui.QApplication.translate("MainWindow", "Crea Una Nueva Ficha Técnica", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva_FT.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva_Nota_Pedido.setText(QtGui.QApplication.translate("MainWindow", "Nota de &Pedido", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva_Nota_Pedido.setToolTip(QtGui.QApplication.translate("MainWindow", "Crea una nueva nota de Pedido", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNueva_Nota_Pedido.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NuevoProveedor.setText(QtGui.QApplication.translate("MainWindow", "P&roveedor", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NuevoProveedor.setToolTip(QtGui.QApplication.translate("MainWindow", "Crea un nuevo proveedor", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NuevoProveedor.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NuevoCliente.setText(QtGui.QApplication.translate("MainWindow", "&Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NuevoCliente.setToolTip(QtGui.QApplication.translate("MainWindow", "Crea un nuevo Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.action_NuevoCliente.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))

from editorProveedor import editorProveedor
from editorNotas import editorNotas
