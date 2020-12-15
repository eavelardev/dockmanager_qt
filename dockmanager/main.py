import sys
from PySide2.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout
from dockmanager import DockManager
from tilelayout import TileLayout
from audiobuffer import AudioBuffer 

class MainWindow(QMainWindow, ):
    def __init__(self):
        QMainWindow.__init__(self)

        # Setup the user interface
        self.setObjectName("MainWindow")
        self.resize(869, 573)

        self.centralwidget = QWidget()
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.audiobuffer = AudioBuffer()

        self.hboxLayout = QHBoxLayout(self.centralwidget)
        self.hboxLayout.setContentsMargins(0, 0, 0, 0)

        self.centralLayout = TileLayout()
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.hboxLayout.addLayout(self.centralLayout)
        
        self.dockmanager = DockManager(self)

        self.dockmanager.new_dock(1)
        self.dockmanager.new_dock(2)
        self.dockmanager.new_dock(3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.processEvents()
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())