from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import threading
import requests
import io
from flask import Flask, Response, request, jsonify, render_template
from wsgiref.util import FileWrapper

global STATE
STATE = {}

app = Flask(__name__)

''' Client '''


@app.route('/')
def root():
    return render_template('/index.html')


@app.route('/rd', methods=['POST'])
def rd():
    req = request.get_json()
    key = req['_key']

    if req['filename'] == STATE[key]['filename']:
        attachment = io.BytesIO(b'')
    else:
        attachment = io.BytesIO(STATE[key]['im'])

    w = FileWrapper(attachment)
    resp = Response(w, mimetype='text/plain', direct_passthrough=True)
    resp.headers['filename'] = STATE[key]['filename']

    return resp


@app.route('/event_post', methods=['POST'])
def event_post():
    global STATE

    req = request.get_json()
    key = req['_key']

    STATE[key]['events'].append(request.get_json())
    return jsonify({'ok': True})


''' Remote '''


@app.route('/new_session', methods=['POST'])
def new_session():
    global STATE

    req = request.get_json()
    key = req['_key']
    STATE[key] = {
        'im': b'',
        'filename': 'none.png',
        'events': []
    }

    return jsonify({'ok': True})


@app.route('/capture_post', methods=['POST'])
def capture_post():
    global STATE

    with io.BytesIO() as image_data:
        filename = list(request.files.keys())[0]
        key = filename.split('_')[1]
        request.files[filename].save(image_data)
        STATE[key]['im'] = image_data.getvalue()
        STATE[key]['filename'] = filename

    return jsonify({'ok': True})


@app.route('/events_get', methods=['POST'])
def events_get():
    req = request.get_json()
    key = req['_key']
    events_to_execute = STATE[key]['events'].copy()
    STATE[key]['events'] = []
    return jsonify({'events': events_to_execute})


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 690, 473))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
#/edit
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.scrollArea.setWidget(self.browser)

        self.Text1 = QtWidgets.QLabel(MainWindow)
        self.Text1.setText("Address: ")

        self.actionText1 = QtWidgets.QTextEdit(MainWindow)
        self.actionText1.setMinimumHeight(25)
        self.actionText1.setMinimumWidth(120)
        self.actionText1.setMaximumHeight(25)
        self.actionText1.setMaximumWidth(120)

        self.Text2 = QtWidgets.QLabel(MainWindow)
        self.Text2.setText("  Pass: ")

        self.actionText2 = QtWidgets.QTextEdit(MainWindow)
        self.actionText2.setMinimumHeight(25)
        self.actionText2.setMinimumWidth(90)
        self.actionText2.setMaximumHeight(25)
        self.actionText2.setMaximumWidth(90)

        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setText('Accept connect ')

        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setText("||||")

        self.Text3 = QtWidgets.QLabel(MainWindow)
        self.Text3.setText(" Address: ")

        self.actionText = QtWidgets.QTextEdit(MainWindow)
        self.actionText.setMinimumHeight(25)
        self.actionText.setMinimumWidth(120)
        self.actionText.setMaximumHeight(25)
        self.actionText.setMaximumWidth(120)
        self.actionText.setReadOnly(True)

        self.Text4 = QtWidgets.QLabel(MainWindow)
        self.Text4.setText("  Pass: ")

        self.actionText3 = QtWidgets.QTextEdit(MainWindow)
        self.actionText3.setMinimumHeight(25)
        self.actionText3.setMinimumWidth(90)
        self.actionText3.setMaximumHeight(25)
        self.actionText3.setMaximumWidth(90)
        self.actionText3.setReadOnly(True)


        self.toolBar.addWidget(self.Text1)
        self.toolBar.addWidget(self.actionText1)
        self.toolBar.addWidget(self.Text2)
        self.toolBar.addWidget(self.actionText2)
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addWidget(self.Text3)
        self.toolBar.addWidget(self.actionText)
        self.toolBar.addWidget(self.Text4)
        self.toolBar.addWidget(self.actionText3)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.browser.urlChanged.connect(self.update_url)
    def server(self):
        app.run('0.0.0.0')


    # /Edit
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())