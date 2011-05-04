from editorProveedorUI import Ui_editorProveedor
from PyQt4 import QtCore, QtGui

class editorProveedor(QtGui.QWidget):
    
    def __init__(self, proveedor = None):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_editorProveedor()
        self.ui.setupUi(self)

    
