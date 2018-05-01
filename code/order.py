import sys, os
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("开启ssr", self)
        btn1.move(30, 50)

        btn2 = QPushButton("关闭ssr", self)
        btn2.move(150, 50)

        btn3 = QPushButton("打开pycharm", self)
        btn3.move(30, 100)

        btn4 = QPushButton("退出", self)
        btn4.move(150, 100)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked1)
        btn3.clicked.connect(self.buttonPyCharm)
        btn4.clicked.connect(QCoreApplication.instance().quit)
        self.statusBar()

        self.setGeometry(500, 500, 300, 200)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        # sender = self.sender()
        order = 'sslocal -c /home/martin/ssr.json'
        os.popen(order)
        text = "启动ssr成功！"
        self.statusBar().showMessage(text)
    def buttonClicked1(self):
        # sender = self.sender()
        order = 'killall sslocal'
        os.popen(order)
        text = "关闭ssr成功！"
        self.statusBar().showMessage(text)
    def buttonPyCharm(self):
        order = 'sh /home/martin/桌面/pycharm-2018.1/bin/pycharm.sh'
        os.popen(order)
        text = "启动pycharm成功！"
        self.statusBar().showMessage(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
