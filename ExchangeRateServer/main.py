import yfinance as yf

msft = yf.Ticker("MSFT")
# show actions (dividends, splits)
print(f"{msft.info['zip']}")
# get stock info
# print(msft.info)

# et historical market data
# hist = msft.history(period="5d")
# print(hist)
# import time
#
# import matplotlib.pyplot as plt
# import seaborn
#
# import yfinance as yf

# msft = yf.Ticker("VXX")
# # get stock info
# print(msft.info)
#
# # get historical market data
# hist = msft.history(period="5d")
# # Plot everything by leveraging the very powerful matplotlib package
# hist['Close'].plot(figsize=(16, 9))
# # Change period to last full year
# msft.history(period="1y")
#
# # show actions (dividends, splits)
# msft.actions

# import json
# from urllib.request import urlopen
# info = json.loads(urlopen("https://api.polygon.io/v1/meta/exchanges?apiKey=krbZSiHGqiKO5m6A1P4L1EyavU2wDZd9").read().decode('utf-8'))
# # print(f"Your regionName: {info['regionName']}, {info['city']} city")
# print(info)
# import sys
# import yfinance as yf
# from PyQt5.QtWidgets import QMainWindow, QApplication
#
# from client import Ui_MainWindow
# import threading
# import socket
#
# # alias = input('Choose an alias >>> ')
# alias = "a"
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 59000))
# message = f'{alias}'
# client.send(message.encode('utf-8'))
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.main_win = QMainWindow()
#         # biến màn hình uic tạm
#         self.uic = Ui_MainWindow()
#         self.uic.setupUi(self.main_win)
#         # msft = yf.Ticker("BBJP")
#         # print(msft.info)
#
#     #     self.uic.pushButton.clicked.connect(self.run)
#     #     self.uic.pushButton_2.clicked.connect(self.start)
#     # def run(self):
#     #     self.client_send()
#     # def start(self):
#         receive_thread = threading.Thread(target=self.client_receive)
#         receive_thread.start()
#
#         # send_thread = threading.Thread(target=self.client_send)
#         # send_thread.start()
#
#     def client_receive(self):
#         while True:
#             try:
#                 message = client.recv(1024).decode('utf-8')
#                 # if message == "alias?":
#                 #     client.send(alias.encode('utf-8'))
#                 # else:
#                 self.uic.textEdit.append(message)
#             except:
#                 self.uic.textEdit.append('Error!')
#                 client.close()
#                 break
#
#     # def client_send(self):
#     #     while True:
#     #         # message = f'{alias}: {input("")}'
#     #         message = f'{alias}'
#     #         client.send(message.encode('utf-8'))
#     def show(self):
#         self.main_win.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_win = MainWindow()
#     main_win.show()
#     sys.exit(app.exec())
