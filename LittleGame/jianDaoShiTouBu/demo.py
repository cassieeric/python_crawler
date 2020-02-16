import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
class red(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(160, 120)#self.resize(40, 30)
        global rednum
        rednum = int(random.random() * 3)  # 随机
        print(rednum)
        choices = ['redcloth.jpg', 'redscissors.jpg', 'redstone.jpg']
        file=str(choices[int(rednum)])
        self.setStyleSheet("QPushButton{border-image: url(%s)}"%(file))
class blue(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(160, 120)#self.resize(40, 30)
        global bluenum
        bluenum = int(random.random() * 3)  # 随机
        choices = ['bluecloth.jpg', 'bluescissors.jpg', 'bluestone.jpg']
        file=str(choices[int(bluenum)])
        self.setStyleSheet("QPushButton{border-image: url(%s)}"%(file))
class GameWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.virusnum=0
        self.setWindowTitle("剪刀石头布小游戏")
        self.setWindowIcon(QIcon('图标.jpg'))
        self.gametimes=0
        self.redscores=0
        self.bluescores = 0
        self.tietimes=0
        self.imagelayout = QGridLayout()
        self.setLayout(self.imagelayout)  # 局部布局

        self.redText= QTextBrowser()
        self.redText.setText('红方选手')
        self.redText.setFixedSize(70, 50)
        self.imagelayout.addWidget(self.redText, 0, 0, Qt.AlignCenter)

        self.actionText = QTextBrowser()
        self.actionText.setText('第0轮')
        self.actionText.setFixedSize(70, 50)
        self.imagelayout.addWidget(self.actionText, 0, 1, Qt.AlignCenter)

        self.blueText = QTextBrowser()
        self.blueText.setText('蓝方选手')
        self.blueText.setFixedSize(70, 50)
        self.imagelayout.addWidget(self.blueText, 0, 2, Qt.AlignCenter)

        self.startPushButton = QPushButton("开始游戏")
        self.startPushButton.setFixedSize(60, 40)
        self.startPushButton.clicked.connect(self.gamestart)
        self.imagelayout.addWidget(self.startPushButton, 2, 1, Qt.AlignCenter)

        self.restartPushButton = QPushButton("重新开始")
        self.restartPushButton.setFixedSize(60, 40)
        self.restartPushButton.clicked.connect(self.restart)
        self.imagelayout.addWidget(self.restartPushButton, 2, 2, Qt.AlignCenter)
        #红方图片布局
        self.redlayout = QGridLayout()  # 网格布局
        self.redWidget = QWidget()
        self.redWidget.setFixedSize(300, 200)
        self.imagelayout.addWidget(self.redWidget, 1, 0)
        self.redWidget.setLayout(self.redlayout)

        #分数布局
        self.scorelayout = QGridLayout()  # 网格布局
        self.scoreWidget = QWidget()
        self.scoreWidget.setFixedSize(300, 200)
        self.imagelayout.addWidget(self.scoreWidget, 1, 1)
        self.scoreWidget.setLayout(self.scorelayout)
        self.scoreRedText = QTextBrowser()
        self.scoreRedText.setText('红方得分：{}分'.format(self.redscores))
        self.scoreRedText.setFixedSize(100, 30)
        self.scorelayout.addWidget(self.scoreRedText, 0, 0)

        self.scoreVsText = QTextBrowser()
        self.scoreVsText.setText('VS')
        self.scoreVsText.setFixedSize(30, 30)
        self.scorelayout.addWidget(self.scoreVsText, 0, 1)

        self.scoreBlueText = QTextBrowser()
        self.scoreBlueText.setText('蓝方得分：{}分'.format(self.bluescores))
        self.scoreBlueText.setFixedSize(100, 30)
        self.scorelayout.addWidget(self.scoreBlueText, 0, 2)

        self.tieText = QTextBrowser()
        self.tieText.setText('平局次数：{}次'.format(self.tietimes))
        self.tieText.setFixedSize(100, 50)
        self.scorelayout.addWidget(self.tieText, 1, 0, 1, 3, Qt.AlignCenter)

        #蓝方图片布局
        self.bluelayout = QGridLayout()  # 网格布局
        self.blueWidget = QWidget()
        self.blueWidget.setFixedSize(300, 200)
        self.imagelayout.addWidget(self.blueWidget, 1, 2)
        self.blueWidget.setLayout(self.bluelayout)

    def gamestart(self):
        self.gametimes+= 1
        self.actionText.setText('第{0}轮'.format(self.gametimes))
        self.redlayout.addWidget(red(), 0, 0)
        self.bluelayout.addWidget(blue(), 0, 0)
        self.judge()
    def judge(self):
        if rednum==0:
            if bluenum==0:
                self.tietimes+=1
                self.tieText.setText('平局次数：{}次'.format(self.tietimes))
            elif bluenum==1:
                self.bluescores+=1
                self.scoreBlueText.setText('蓝方得分：{}分'.format(self.bluescores))
            elif bluenum==2:
                self.redscores += 1
                self.scoreRedText.setText('红方得分：{}分'.format(self.redscores))
        elif rednum==1:
            if bluenum == 0:
                self.redscores += 1
                self.scoreRedText.setText('红方得分：{}分'.format(self.redscores))
            elif bluenum == 1:
                self.tietimes+=1
                self.tieText.setText('平局次数：{}次'.format(self.tietimes))
            elif bluenum == 2:
                self.bluescores += 1
                self.scoreBlueText.setText('蓝方得分：{}分'.format(self.bluescores))
        elif rednum==2:
            if bluenum == 0:
                self.bluescores += 1
                self.scoreBlueText.setText('蓝方得分：{}分'.format(self.bluescores))
            elif bluenum == 1:
                self.redscores += 1
                self.scoreRedText.setText('红方得分：{}分'.format(self.redscores))
            elif bluenum == 2:
                self.tietimes+=1
                self.tieText.setText('平局次数：{}次'.format(self.tietimes))
    def restart(self):
        self.gametimes=0
        self.redscores=0
        self.bluescores=0
        self.tietimes=0
        self.actionText.setText('第{0}轮'.format(self.gametimes))
        self.scoreRedText.setText('红方得分：{}分'.format(self.redscores))
        self.scoreBlueText.setText('蓝方得分：{}分'.format(self.bluescores))
        self.tieText.setText('平局次数：{}次'.format(self.tietimes))

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
class Game(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("剪刀石头布小游戏")
        self.setWindowIcon(QIcon('图标.jpg'))
        self.virusnum = 0
        self.gametimes = 0
        self.redscores = 0
        self.bluescores = 0
        self.tietimes = 0
        self.imagelayout = QGridLayout()
        self.setLayout(self.imagelayout)  # 局部布局

        self.redText = QTextBrowser()
        self.redText.setText('红方选手')
        self.redText.setFixedSize(70, 50)
        self.imagelayout.addWidget(self.redText, 0, 0, Qt.AlignCenter)

        self.actionText = QTextBrowser()
        self.actionText.setText('第0轮')
        self.actionText.setFixedSize(70, 50)
        self.imagelayout.addWidget(self.actionText, 0, 1, Qt.AlignCenter)

        self.blueText = QTextBrowser()
        self.blueText.setText('蓝方选手')
        self.blueText.setFixedSize(70, 50)
        self.imagelayout.addWidget(self.blueText, 0, 2, Qt.AlignCenter)
app = QApplication(sys.argv)
gameshow = GameWindow()
#gameshow=Game()
gameshow.setFixedSize(900, 400)
gameshow.show()
sys.exit(app.exec_())