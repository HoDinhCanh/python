import socket
import sys
import threading
import time

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow, QApplication
from datetime import datetime

from PyQt5.uic.properties import QtCore

from client2 import Ui_MainWindow
from time import ctime


class WorkerThread(QThread):
    recieicon = QtCore.pyqtSignal()
    noti = QtCore.pyqtSignal(str)
    addnew = QtCore.pyqtSignal(str)
    showcontent = QtCore.pyqtSignal(list)

    def __init__(self, client):
        QThread.__init__(self, )
        self.client = client

    def run(self):

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        # biến màn hình uic tạm
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.thread2()
        self.thread()
    def time(self):
        while(True):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.uic.label.setText(time.ctime())
            time.sleep(1)
    def run(self):
        while(True):
            self.worker = WorkerThread(self.clientSock)
            self.worker.recieicon.connect(self.mainUi)
            self.worker.noti.connect(self.noti)
            self.worker.addnew.connect(self.addrowtble)

            msgFromClient = ""
            #
            bytesToSend = str.encode(msgFromClient)

            serverAddressPort = ("127.0.0.1", 20001)

            bufferSize = 1024

            # Create a UDP socket at client side

            UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

            # Send to server using created UDP socket

            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)

            msg = "Server: {}".format(msgFromServer[0])
            self.uic.textEdit.append("\n")
            time.sleep(3)
            msgFromClient = ""
            #
            bytesToSend = str.encode(msgFromClient)

            serverAddressPort = ("127.0.0.1", 20001)

            bufferSize = 1024

            # Create a UDP socket at client side

            UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

            # Send to server using created UDP socket

            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)

            msg = format(msgFromServer[0])
            self.uic.textEdit.append("\n")
            time.sleep(3)
    def thread2(self):
        receive_thread2 = threading.Thread(target=self.time)
        receive_thread2.start()
    def thread(self):
        receive_thread = threading.Thread(target=self.run)
        receive_thread.start()
    def addNew(self):
        self.uic.tableWidget.setRowCount(14)
        item = self.uic.QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        


    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

