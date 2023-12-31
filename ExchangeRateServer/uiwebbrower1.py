# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GETPOSTHEAD.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import threading
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from bs4 import BeautifulSoup

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.tab1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 674, 491))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 674, 491))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.verticalLayout_7.addWidget(self.plainTextEdit_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 674, 491))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_3)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.verticalLayout_8.addWidget(self.plainTextEdit_2)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.addWidget(self.scrollArea_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 674, 491))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_4)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_6.addWidget(self.plainTextEdit)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.addWidget(self.scrollArea_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # Edit
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.scrollArea.setWidget(self.browser)

        self.actionBack = QtWidgets.QAction(MainWindow)
        self.actionBack.setText("Back")
        self.actionBack.triggered.connect(self.browser.back)

        self.actionNext = QtWidgets.QAction(MainWindow)
        self.actionNext.setText("Next")
        self.actionNext.triggered.connect(self.browser.forward)

        self.actionReload = QtWidgets.QAction(MainWindow)
        self.actionReload.setText("Reload")
        self.actionReload.triggered.connect(self.browser.reload)

        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setText("Home")
        self.actionHome.triggered.connect(self.navigate_home)

        self.actionText = QtWidgets.QTextEdit(MainWindow)
        self.actionText.setMinimumHeight(30)
        self.actionText.setMaximumHeight(30)

        self.actionFind = QtWidgets.QAction(MainWindow)
        self.actionFind.setText("Find")
        self.actionFind.triggered.connect(self.navigate_to_url)

        self.toolBar.addAction(self.actionBack)
        self.toolBar.addAction(self.actionNext)
        self.toolBar.addAction(self.actionReload)
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addWidget(self.actionText)
        self.toolBar.addAction(self.actionFind)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):

        url = self.actionText.toPlainText()
        try:
            r = requests.get(url)
            self.browser.setUrl(QUrl(url))
            print(self.actionText.toPlainText())
            self.head()
        except:
            try:
                r = requests.get("http://" + url)
                self.browser.setUrl(QUrl("http://" + url))
                print(self.actionText.toPlainText())
                self.head()
            except:
                # a = url[0:4]
                # if (a != "http"):
                self.browser.setUrl(QUrl(
                    "https://www.google.com/search?q=" + url + "&rlz=1C1UEAD_enVN959VN959&oq=" + url + "&aqs=chrome..69i57.1033j1j7&sourceid=chrome&ie=UTF-8"))
                # else:
                #     self.browser.setUrl(QUrl(url))
                print(self.actionText.toPlainText())
                self.head()

    def update_url(self, q):
        self.actionText.setText(q.toString())

    def head1(self):
        a = self.actionText.toPlainText()
        import urllib.request
        self.plainTextEdit_3.setPlainText("")

        response = requests.get(a)
        soup = BeautifulSoup(response.content, "html.parser")
        self.plainTextEdit_3.appendPlainText(str(soup))

        html_content = requests.get(a).text
        # Parse the html content using any parser
        soup1 = BeautifulSoup(html_content, "html.parser")
        html= 0
        head= 0
        meta= 0
        script= 0
        style= 0
        noscript= 0
        link= 0
        body= 0
        i= 0
        h1= 0
        h2= 0
        h3= 0
        h4= 0
        li= 0
        ul=0
        p = 0
        aa = 0
        div = 0
        span = 0
        img = 0
        self.plainTextEdit_2.setPlainText("")
        for tag in soup1.find_all():

            if (tag.name == "html"):
                html += 1
            if (tag.name == "head"):
                head+= 1
            if (tag.name == "meta"):
                meta += 1
            if (tag.name == "script"):
                script += 1
            if (tag.name == "style"):
                style += 1
            if (tag.name == "noscript"):
                noscript += 1
            if (tag.name == "link"):
                link += 1
            if (tag.name == "body"):
                body += 1
            if (tag.name == "i"):
                i += 1
            if (tag.name == "h1"):
                h1 += 1
            if (tag.name == "h2"):
                h2 += 1
            if (tag.name == "h3"):
                h3 += 1
            if (tag.name == "h4"):
                h4 += 1
            if (tag.name == "li"):
                li += 1
            if (tag.name == "ul"):
                ul += 1
            if (tag.name == "p"):
                p += 1
            if (tag.name == "a"):
                aa += 1
            if (tag.name == "div"):
                div += 1
            if (tag.name == "span"):
                span += 1
            if (tag.name == "img"):
                img += 1
        self.plainTextEdit_2.appendPlainText("tag <html>: " + str(html) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <head>: " + str(head) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <meta>: " + str(meta) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <script>: " + str(script) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <style>: " + str(style) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <noscript>: " + str(noscript) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <link>: " + str(link) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <body>: " + str(body) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <i>: " + str(i) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <h1>: " + str(h1) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <h2>: " + str(h2) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <h3>: " + str(h3) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <h4>: " + str(h4) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <li>: " + str(li) + " Tag")
        self.plainTextEdit_2.appendPlainText("tag <ul>: " + str(ul) + " Tag")

        self.plainTextEdit_2.appendPlainText("tag <p>: "+ str(p)+ " Tag")
        self.plainTextEdit_2.appendPlainText("tag <a>: "+ str(aa)+ " Tag")
        self.plainTextEdit_2.appendPlainText("tag <div>: "+ str(div)+ " Tag")
        self.plainTextEdit_2.appendPlainText("tag <span>: "+ str(span)+ " Tag")
        self.plainTextEdit_2.appendPlainText("tag <img>: "+ str(img)+ " Tag")

        r = requests.head(a)
        print(r.headers)
        try:
            self.plainTextEdit.setPlainText("Content Type: " + r.headers['Content-Type'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("P3P: " + r.headers['P3P'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Date: "+r.headers['Date'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Server: " + r.headers['Server'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("X-XSS-Protection: " + r.headers['X-XSS-Protection'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("X-Frame-Options: " + r.headers['X-Frame-Options'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Transfer-Encoding: " + r.headers['Transfer-Encoding'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Expires: "+r.headers['Expires'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Cache Control: " + r.headers['Cache-Control'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Pragma: " + r.headers['Pragma'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Location: " + r.headers['Location'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Content Language: " + r.headers['Content-Language'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Vary: " + r.headers['Vary'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Keep Alive: " + r.headers['Keep-Alive'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Connection: " + r.headers['Connection'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Set-Cookie: " + r.headers['Set-Cookie'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Content Type: " + r.headers['Content-Type'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Content Encoding: " + r.headers['Content-Encoding'])
        except:
            print("1")
        try:
            self.plainTextEdit.appendPlainText("Alt-Svc: " + r.headers['Alt-Svc'])
        except:
            print("1")


    def head(self):
        receive_thread = threading.Thread(target=self.head1)
        receive_thread.start()

    # /Edit

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "HTML"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "GET/POST"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "HEAD"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
