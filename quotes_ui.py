# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quotes_ui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.author = QtWidgets.QLineEdit(self.centralwidget)
        self.author.setObjectName("author")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.author)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.quote = QtWidgets.QTextEdit(self.centralwidget)
        self.quote.setObjectName("quote")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.quote)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_quote_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_quote_btn.setObjectName("add_quote_btn")
        self.horizontalLayout.addWidget(self.add_quote_btn)
        self.list_quotes_btn = QtWidgets.QPushButton(self.centralwidget)
        self.list_quotes_btn.setObjectName("list_quotes_btn")
        self.horizontalLayout.addWidget(self.list_quotes_btn)
        self.save_quotes_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_quotes_btn.setObjectName("save_quotes_btn")
        self.horizontalLayout.addWidget(self.save_quotes_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.display_quotes = QtWidgets.QTextEdit(self.centralwidget)
        self.display_quotes.setObjectName("display_quotes")
        self.verticalLayout_4.addWidget(self.display_quotes)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionQuotes = QtWidgets.QAction(MainWindow)
        self.actionQuotes.setObjectName("actionQuotes")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quote Database"))
        self.label.setText(_translate("MainWindow", "Author"))
        self.label_2.setText(_translate("MainWindow", "Quote"))
        self.add_quote_btn.setText(_translate("MainWindow", "Add Quote"))
        self.list_quotes_btn.setText(_translate("MainWindow", "List Quotes"))
        self.save_quotes_btn.setText(_translate("MainWindow", "Save Quotes"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionQuotes.setText(_translate("MainWindow", "Quotes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

