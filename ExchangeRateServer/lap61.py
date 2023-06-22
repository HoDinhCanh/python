import socket
import struct
import sys

from PyQt5 import QtCore, QtWidgets, QtGui

from lap6client import Ui_MainWindow
import subprocess
#file and directory listing
returned_text = subprocess.check_output("ipconfig/all", shell=True, universal_newlines=True)

class WorkerThread(QtCore.QThread):
    showmess = QtCore.pyqtSignal(str, str)
    newtabclient = QtCore.pyqtSignal(str)

    def __init__(self, client):
        QtCore.QThread.__init__(self, )
        self.client = client

    def run(self):
        checklist = False
        while True:
            try:
                data, addr = self.client.recvfrom(10240)
                if data == b"login_client_new":
                    checklist = True
                elif checklist == True:
                    if data == b"end_client_new":
                        checklist = False
                    else:
                        self.newtabclient.emit(data.decode('utf-8'))

                else:
                    self.showmess.emit(data.decode('utf-8'), "nhan")
            except:
                pass


class Clients():
    def __init__(self):

        self.multicast_group = ('224.0.0.1', 10000)

        # Create the datagram socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set a timeout so the socket does not block indefinitely when trying
        # to receive data.
        self.sock.settimeout(0.2)
        # Set the time-to-live for messages to 1 so they do not go past the
        # local network segment.
        ttl = struct.pack('b', 1)
        self.listclient = []
        self.addressclient = ""
        self.listcomponet = []
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        self.worker = WorkerThread(self.sock)
        self.worker.showmess.connect(self.showmess)
        self.worker.newtabclient.connect(self.newtabclient)
        self.worker.start()

        # self.worker.noti.connect(self.noti)
        self.app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        MainWindow.setWindowTitle("Client")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.ui.pushButton.clicked.connect(self.send)
        self.ui.tabWidget.currentChanged.connect(self.clicktab)
        self.sock.sendto(b"message_login", self.multicast_group)
        MainWindow.show()
        sys.exit(self.app.exec_())

        # self.ui.label.setText(self.addressclient)

    def clicktab(self):
        index = self.ui.tabWidget.currentIndex() - 1

        if index == -1:
            self.addressclient = ""
        else:
            self.addressclient = self.listclient[index]
            print("Địa chỉ hiện tại là:"+self.addressclient)

    def send(self):
        self.ui.textEdit_2.setText(returned_text)
        message = self.ui.textEdit_2.toPlainText()

        if self.addressclient != "":
            message = "{" + self.addressclient + "}" + message
        self.sock.sendto(message.encode('utf-8'), self.multicast_group)
        self.showmess(message, "gui")
        self.ui.textEdit_2.setText("")

    def newtabclient(self, data):

        self.listclient.append(data)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        # self.scrollArea_3.setGeometry(QtCore.QRect(0, 0, 691, 541))
        self.scrollArea_3.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.verticalLayout_10.addWidget(self.scrollArea_3)
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0,  394, 157))
        self.scrollAreaWidgetContents_3.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.ui.tabWidget.addTab(self.tab_2, data)
        self.listcomponet.append(self.verticalLayout_6)

    # 1111111111111111111111111111111111111112222222222222222222222222222222222222222233333333333333333333333333333333333333333444444444444444444444444444444444444444
    def showmess(self, data, position):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.label = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents)
        self.label.setMinimumSize(QtCore.QSize(10, 30))
        self.label.setMaximumSize(QtCore.QSize(350, 350))
        # d = data
        # data = ""
        # print(len(d))
        # a=""
        # if(len(d)>40):
        #     a = d[0:40]
        #     d = d[40:len(d)]
        #     data += a+"\n"+d

        self.label.setText("    " + data + "    ")

        if self.addressclient != "" and position == "gui":
            self.label.setStyleSheet("border-radius:15px; \n"
                                    "background-color:rgba(46,212,198,0.7);")
            self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
            self.label.setSizePolicy(sizePolicy)

            self.listcomponet[self.listclient.index(self.addressclient)].addWidget(self.label, 0,
                                                                                   QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        else:
            try:

                s = data
                s = s.replace("{('", "")
                arr = []
                arr = s.split(")}")
                listaddres = []

                arr[0] = arr[0].replace("'", "")
                listaddres = arr[0].split(",")
                addre = listaddres[0], int(listaddres[1])
                print("diachi", str(addre))
                if str(addre) in self.listclient:
                    print("zxcxczxcvasdf")
                    if position == "nhan":
                        self.label.setStyleSheet("border-radius:15px;\n"
                                                "background-color:rgba(206,206,206,0.7);")
                        print("nhan: ", self.listclient.index(str(addre)))
                        self.listcomponet[self.listclient.index(str(addre))].addWidget(self.label, 0,
                                                                                       QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

            except:

                if position == "nhan":
                    self.label.setStyleSheet("border-radius:15px;\n"
                                                "background-color:rgba(206,206,206,0.7);")
                    self.ui.verticalLayout_8.addWidget(self.label, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
                else:
                    self.label.setStyleSheet("border-radius:15px; \n"
                                    "background-color:rgba(46,212,198,0.7);")
                    self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
                    self.ui.verticalLayout_8.addWidget(self.label, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)



if __name__ == '__main__':
    Clients()

