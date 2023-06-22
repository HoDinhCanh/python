import socket
import sys
import threading
import time
from PyQt5.QtWidgets import QMainWindow, QApplication
from datetime import datetime
from client import Ui_MainWindow
from time import ctime
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
            self.uic.textEdit.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style="font-size:8.25pt; font-weight:400; font-style:normal;"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" background-color:#d3d3d3;">'+msg+'</span></p></body></html>')
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

            msg = "Server: {}".format(msgFromServer[0])
            self.uic.textEdit.append(
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style="font-size:8.25pt; font-weight:400; font-style:normal;"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span>' + msg + '</span></p></body></html>')
            self.uic.textEdit.append("\n")
            time.sleep(3)
    def thread2(self):
        receive_thread2 = threading.Thread(target=self.time)
        receive_thread2.start()
    def thread(self):
        receive_thread = threading.Thread(target=self.run)
        receive_thread.start()


    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())