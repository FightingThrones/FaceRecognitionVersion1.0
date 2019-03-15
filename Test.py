from PyQt5.QtWidgets import *
from window import Ui_MainWindow
from child import Ui_Child
import sys
from PyQt5.QtGui import QIcon
import qdarkstyle
from PyQt5.QtGui import*
class Main(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.Close_pushButton.clicked.connect(self.close)

class Child(QMainWindow,Ui_Child):
    def  __init__(self):
        super(Child,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close)

    def OPEN(self):
        self.show()
        main.close()

if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main=Main()
    main.setWindowIcon(QIcon("./IconLibrary/Icon.png"))
    movie = QMovie("./IconLibrary/Cool.gif")
    main.label.setMovie(movie)
    movie.start()
    ch=Child()
    main.show()
    main.Start_pushButton.clicked.connect(ch.OPEN)
    sys.exit(app.exec_())