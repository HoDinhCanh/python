import sys

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import*
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from uiwebbrowerGD import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        # biến màn hình uic tạm
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)


        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.uic.scrollArea.setWidget(self.browser)

        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setText("Back")

        self.actionNext = QtWidgets.QAction(MainWindow)
        self.actionNext.setText("Next")

        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setText("Reload")

        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setText("Home")

        self.actionText = QtWidgets.QTextEdit(MainWindow)
        self.actionText.setMinimumHeight(30)
        self.actionText.setMaximumHeight(30)

        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setText("Find")

        self.toolBar.addAction(self.actionBack)
        self.toolBar.addAction(self.actionNext)
        self.toolBar.addAction(self.actionReload)
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addWidget(self.actionText)
        self.toolBar.addAction(self.actionFind)

        self.actionBack.triggered.connect(self.browser.back)
        self.actionNext.triggered.connect(self.browser.forward)
        self.actionReload.triggered.connect(self.browser.reload)
        self.actionHome.triggered.connect(self.navigate_home)
        self.actionFind.triggered.connect(self.navigate_to_url)



    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):

        url = self.actionText.toPlainText()
        try:
            r = requests.get(url)
            print(r.headers)
            self.browser.setUrl(QUrl(url))
        except:
            try:
                r = requests.get("http://"+url)
                print(r.headers)
                self.browser.setUrl(QUrl("http://"+url))
            except:
                # a = url[0:4]
                # if (a != "http"):
                self.browser.setUrl(QUrl(
                    "https://www.google.com/search?q=" + url + "&rlz=1C1UEAD_enVN959VN959&oq=" + url + "&aqs=chrome..69i57.1033j1j7&sourceid=chrome&ie=UTF-8"))
                # else:
                #     self.browser.setUrl(QUrl(url))


    def update_url(self, q):
        self.actionText.setText(q.toString())

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())