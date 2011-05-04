from editorNotasUI import Ui_editorNotas
from PyQt4 import QtGui, QtCore
from modelos import *
import datetime
setup_all(True)
class editorNotas(QtGui.QWidget):
    def __init__(self, notaPedido=None):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_editorNotas()
        self.ui.setupUi(self)
        for proveedor in  Proveedor.query.all():
            self.ui.listaProvedores.addItem(proveedor.nombre)
        dt =datetime.date.today()
        self.ui.dateEdit.setDate(QtCore.QDate(dt.year, dt.month, dt.day))
    def new(self):
        pass


            
