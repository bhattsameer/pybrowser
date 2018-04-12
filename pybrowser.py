from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("PyBrowser")

		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl("https://github.com"))

		self.setCentralWidget(self.browser) 


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()