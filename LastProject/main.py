import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from GiaoDien import Ui_MainWindow
from module import*
import subprocess
import tsp
import speedtest
from urllib.request import urlopen
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_win = QMainWindow()
        # biến màn hình uic tạm
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.textEdit.setText(getIP())
        self.uic.textEdit.setStyleSheet("color:Blue")
        self.uic.label_4.setText(yourIP())
        self.uic.label_5.setText(lanIP())
        self.uic.pushButton.clicked.connect(self.resIP1)
        self.uic.pushButton_2.clicked.connect(self.resIP2)
        self.uic.pushButton_3.clicked.connect(self.run)
        Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
        new = []
        # arrange the string into clear info
        for item in Id:
            new.append(str(item.split("\r")[:-1]))
        for i in new:
            self.uic.textEdit_2.append(i[2:-2])
    # def threa1(self):
    #     self.uic.textEdit_3.append(tsp.shell())
        self.callThread2 = threading.Thread(target=self.ping)
        self.callThread2.start()
    def testspeed(self):
        redText = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >"
        redText += "Please Waiting!!!!"
        redText += "</span>"
        self.uic.textEdit_3.append(redText+"\n")
        info = json.loads(urlopen("http://ip-api.com/json/").read().decode('utf-8'))
        test = speedtest.Speedtest()
        self.uic.textEdit_3.append("loading server list...")
        test.get_servers()  # Get list servers
        self.uic.textEdit_3.append("Choosing best server...")
        best = test.get_best_server()
        # self.uic.textEdit_3.append(best)
        redText = "Found: "
        redText += "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"
        redText += f"{best['host']}"+ "</span>"+" located in "+ "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"+f"{best['country']}"
        redText += "</span>"
        self.uic.textEdit_3.append(redText+"\n")
        time.sleep(1.0)
        redText = "Your regionName: "+"<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"+f"{info['regionName']}, {info['city']}" +"</span>"+ " City"
        self.uic.textEdit_3.append(redText + "\n")
        time.sleep(1.0)
        redText = "Time zone: "+ "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"+f"{info['timezone']}"+"</span>"
        self.uic.textEdit_3.append(redText + "\n")
        time.sleep(1.0)
        redText = "Testing from: " + "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >" + f"{info['org']} - {info['isp']} ({info['query']})" + "</span>"
        self.uic.textEdit_3.append(redText + "\n")
        time.sleep(1.0)
        redText = "Hosted: "
        redText += "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"
        redText += f"{best['sponsor']}"+ "</span>"+" place in "+ "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"+f"{best['name']}"
        redText += "</span>"
        self.uic.textEdit_3.append(redText + "\n")
        time.sleep(1.5)
        redText = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >"+"Performing download test..."+"</span>"
        self.uic.textEdit_3.append(redText + "\n")
        download_result = test.download()
        redText = "Download speed: "+ "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"+f"{download_result / 1024 / 1024:.2f}"+"</span>"+" Mbit/s"
        self.uic.textEdit_3.append(redText + "\n")
        redText = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >" + "Performing upload test..." + "</span>"
        self.uic.textEdit_3.append(redText + "\n")
        upload_result = test.download()
        redText = "Upload speed: "+ "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"+f"{upload_result / 1024 / 1024:.2f}"+"</span>"+" Mbit/s"
        self.uic.textEdit_3.append(redText + "\n")
        time.sleep(1.0)
        redText = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >" + "Performing ping..." + "</span>"
        self.uic.textEdit_3.append(redText + "\n")
        time.sleep(1.5)
        ping_result = test.results.ping
        redText = "Ping: "+ "<span style=\" font-size:8pt; font-weight:600; color:Blue;\" >"+f"{ping_result:.2f}"+"</span>"+" ms"
        self.uic.textEdit_3.append(redText + "\n")
        time.sleep(0.5)
        redText = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\" >"
        redText += "Done!!!!"
        redText += "</span>"
        self.uic.textEdit_3.append(redText+"\n")
    def run(self):
        self.callThread = threading.Thread(target=self.testspeed)
        self.callThread.start()
    def resIP1(self):
        self.uic.label_4.setText("Haha lỗi sấp mặt")

    def resIP2(self):
        self.uic.label_5.setText("Haha lại lỗi sấp mặt")
    def ping(self):
        test2 = speedtest.Speedtest()

        while(True):
            test2.get_servers()
            best2 = test2.get_best_server()
            ping_result2 = test2.results.ping
            self.uic.lcdNumber.display(f"{ping_result2:.2f}")
            time.sleep(1)

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
