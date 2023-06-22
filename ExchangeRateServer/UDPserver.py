import socket
import sys
import threading
from datetime import datetime
import yfinance as yf
import random


from PyQt5.QtWidgets import QMainWindow, QApplication

from client import Ui_MainWindow

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

msft = yf.Ticker("BBJP")
msgFromServer0 = f"Name:  {msft.info['longName']} |   phone: {msft.info['phone']}   |   day hight: {msft.info['dayHigh']}   |   regular Market Price: {msft.info['regularMarketPrice']}   |   nav Price: {msft.info['navPrice']}"

msft = yf.Ticker("0388.HK")
msgFromServer1 = f"Name:  {msft.info['longName']} |   phone: {msft.info['phone']}   |    target Low Price: {msft.info['targetLowPrice']}   |   target Median Price: {msft.info['targetMedianPrice']}   |   current Price: {msft.info['currentPrice']}   |   Earning Growth: {msft.info['earningsGrowth']}"

msft = yf.Ticker("NYT")
msgFromServer2 = f"Name:  {msft.info['longName']} |   phone: {msft.info['phone']}   |   target Low Price: {msft.info['targetLowPrice']}   |   target Median Price: {msft.info['targetMedianPrice']}   |   current Price: {msft.info['currentPrice']}   |   Earning Growth: {msft.info['earningsGrowth']}"

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))


# Listen for incoming datagrams

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        # biến màn hình uic tạm
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.textEdit.append("UDP server up and listening")
        self.thread()

    def run(self):
        while (True):
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

            # message = bytesAddressPair[0]

            address = bytesAddressPair[1]

            # clientMsg = "Message from Client:{}".format(message)
            clientIP = "Send to Client IP Address:{}".format(address)

            # self.uic.textEdit.append(clientMsg)
            self.uic.textEdit.append(clientIP)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            # generate some integers
            t=random.randint(0,2)
            if(t ==0):
                bytesToSend = str.encode(current_time+": "+ msgFromServer0)
                UDPServerSocket.sendto(bytesToSend, address)
            else:
                if(t == 1):
                    bytesToSend = str.encode(current_time+": "+msgFromServer1)
                    UDPServerSocket.sendto(bytesToSend, address)
                else:
                    bytesToSend = str.encode(current_time+": "+msgFromServer2)
                    UDPServerSocket.sendto(bytesToSend, address)
            # Sending a reply to client


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