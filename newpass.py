# Form implementation generated from reading ui file 'newpass.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6.QtWidgets import QLineEdit
from PyQt6 import QtCore, QtGui, QtWidgets


class NewPass(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setStyleSheet("background-color:#242582;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 400, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.NickName_pass = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.NickName_pass.setGeometry(QtCore.QRect(50, 100, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.NickName_pass.setFont(font)
        self.NickName_pass.setStyleSheet("background-color:#553d67")
        self.NickName_pass.setObjectName("NickName_pass")
        self.Email_pass = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Email_pass.setGeometry(QtCore.QRect(50, 200, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Email_pass.setFont(font)
        self.Email_pass.setStyleSheet("background-color:#553d67")
        self.Email_pass.setObjectName("Email_pass")
        self.Repeat_NewPass_pass = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Repeat_NewPass_pass.setGeometry(QtCore.QRect(400, 200, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.Repeat_NewPass_pass.setFont(font)
        self.Repeat_NewPass_pass.setStyleSheet("background-color:#553d67")
        self.Repeat_NewPass_pass.setObjectName("Repeat_NewPass_pass")
        self.NewPass_pass = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Repeat_NewPass_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.NewPass_pass.setGeometry(QtCore.QRect(400, 100, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.NewPass_pass.setFont(font)
        self.NewPass_pass.setStyleSheet("background-color:#553d67")
        self.NewPass_pass.setObjectName("NewPass_pass")
        self.NickName = QtWidgets.QLabel(parent=self.centralwidget)
        self.NewPass_pass.setEchoMode(QLineEdit.EchoMode.Password)
        self.NickName.setGeometry(QtCore.QRect(50, 50, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        self.NickName.setFont(font)
        self.NickName.setObjectName("NickName")
        self.Email_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Email_2.setGeometry(QtCore.QRect(50, 150, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        self.Email_2.setFont(font)
        self.Email_2.setObjectName("Email_2")
        self.Newpass = QtWidgets.QLabel(parent=self.centralwidget)
        self.Newpass.setGeometry(QtCore.QRect(400, 50, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        self.Newpass.setFont(font)
        self.Newpass.setObjectName("Newpass")
        self.Repnewpass = QtWidgets.QLabel(parent=self.centralwidget)
        self.Repnewpass.setGeometry(QtCore.QRect(400, 150, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        self.Repnewpass.setFont(font)
        self.Repnewpass.setObjectName("Repnewpass")
        self.Vyhod = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Vyhod.setGeometry(QtCore.QRect(400, 300, 200, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        self.Vyhod.setFont(font)
        self.Vyhod.setStyleSheet("background-color: #99738e")
        self.Vyhod.setObjectName("Vyhod")
        self.OK = QtWidgets.QPushButton(parent=self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(250, 300, 100, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        self.OK.setFont(font)
        self.OK.setStyleSheet("background-color: #99738e")
        self.OK.setObjectName("OK")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Восстановление пароля"))
        self.NickName.setText(_translate("MainWindow", "NickName"))
        self.Email_2.setText(_translate("MainWindow", "Email"))
        self.Newpass.setText(_translate("MainWindow", "New Password"))
        self.Repnewpass.setText(_translate("MainWindow", "Repeat  new password"))
        self.Vyhod.setText(_translate("MainWindow", "Выход"))
        self.OK.setText(_translate("MainWindow", "Ок"))