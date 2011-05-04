import os, sys
from PyQt4 import QtCore,QtGui

from mainWindowUI import Ui_MainWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sarasa.hide()
    def on_actionNueva_Nota_Pedido_triggered(self):
        self.ui.sarasa.show()
              
    def on_action_NuevoProveedor_triggered(self):
        self.ui.sarasa.show()
        
       
def main():
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

