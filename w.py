import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from desingprog import Ui_MainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(644, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 220, 75, 23))
        self.pushButton.setObjectName("Загрузить")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Загрузить"))


class WorkThread(QtCore.QThread):
    ''' Потоковая задача '''
    threadSignal = QtCore.pyqtSignal(str)                      # int

    def __init__(self, text):                                  # +++
        super(WorkThread, self).__init__()  
        self.text = text

    def run(self):
#        print(self.lineEdit.text())     #данная функция в потоке не работает
        self.threadSignal.emit(self.text)
        QtCore.QThread.msleep(10)


class ExampleApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.func2)             # +++
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 150, 120, 30))


    def func2(self):
        self.thread = WorkThread(self.lineEdit.text())          # +++
        self.thread.threadSignal.connect(self.funcPrint)
        self.thread.start()

    def funcPrint(self, text):                                  # +++
        print(text)
        self.label.setText("---> {}".format(text))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()


if __name__ == '__main__':
    main()        
