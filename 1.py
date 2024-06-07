# vhod.py
from PyQt6 import QtCore, QtGui, QtWidgets

class Vhod(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 250)  # Изменено размер окна
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 171, 21))
        self.label.setObjectName("label")

        self.Email = QtWidgets.QLabel(parent=self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(40, 53, 47, 13))
        self.Email.setObjectName("Email")

        self.Email_Vod = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Email_Vod.setGeometry(QtCore.QRect(30, 89, 201, 21))
        self.Email_Vod.setObjectName("Email_Vod")

        self.Password = QtWidgets.QLabel(parent=self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(40, 132, 61, 16))
        self.Password.setObjectName("Password")

        self.Pass_vod = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Pass_vod.setGeometry(QtCore.QRect(30, 169, 171, 21))
        self.Pass_vod.setObjectName("Pass_vod")
        self.Pass_vod.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Установка режима скрытия пароля

        self.Vhod = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Vhod.setGeometry(QtCore.QRect(50, 202, 101, 31))
        self.Vhod.setObjectName("Vhod")

        self.Register = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Register.setGeometry(QtCore.QRect(170, 202, 101, 31))
        self.Register.setObjectName("Register")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход"))  # Изменено название окна
        self.label.setText(_translate("MainWindow", "Вход в систему"))
        self.Email.setText(_translate("MainWindow", "Email"))
        self.Password.setText(_translate("MainWindow", "Пароль"))
        self.Vhod.setText(_translate("MainWindow", "Вход"))
        self.Register.setText(_translate("MainWindow", "Регистрация"))

# register.py
from PyQt6 import QtCore, QtGui, QtWidgets

class Register(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)  # Изменено размер окна
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 141, 21))
        self.label.setObjectName("label")

        self.Name_reg = QtWidgets.QLabel(parent=self.centralwidget)
        self.Name_reg.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.Name_reg.setObjectName("Name_reg")

        self.Name_vod_reg = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Name_vod_reg.setGeometry(QtCore.QRect(30, 80, 201, 21))
        self.Name_vod_reg.setObjectName("Name_vod_reg")

        self.Email_reg = QtWidgets.QLabel(parent=self.centralwidget)
        self.Email_reg.setGeometry(QtCore.QRect(40, 110, 47, 13))
        self.Email_reg.setObjectName("Email_reg")

        self.Email_vod_reg = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Email_vod_reg.setGeometry(QtCore.QRect(30, 140, 201, 21))
        self.Email_vod_reg.setObjectName("Email_vod_reg")

        self.Pass_reg = QtWidgets.QLabel(parent=self.centralwidget)
        self.Pass_reg.setGeometry(QtCore.QRect(40, 170, 61, 16))
        self.Pass_reg.setObjectName("Pass_reg")

        self.Pass_vod = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Pass_vod.setGeometry(QtCore.QRect(30, 200, 201, 21))
        self.Pass_vod.setObjectName("Pass_vod")
        self.Pass_vod.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.Zaregistr = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Zaregistr.setGeometry(QtCore.QRect(50, 242, 141, 31))
        self.Zaregistr.setObjectName("Zaregistr")

        self.Vyhod = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Vyhod.setGeometry(QtCore.QRect(150, 242, 141, 31))
        self.Vyhod.setObjectName("Vyhod")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Регистрация"))  # Изменено название окна
        self.label.setText(_translate("MainWindow", "Регистрация"))
        self.Name_reg.setText(_translate("MainWindow", "Имя"))
        self.Email_reg.setText(_translate("MainWindow", "Email"))
        self.Pass_reg.setText(_translate("MainWindow", "Пароль"))
        self.Zaregistr.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.Vyhod.setText(_translate("MainWindow", "Выход"))

# profile.py
from PyQt6 import QtCore, QtGui, QtWidgets

class Profile(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)  # Изменено размер окна
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Vyhod = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Vyhod.setGeometry(QtCore.QRect(90, 242, 101, 31))
        self.Vyhod.setObjectName("Vyhod")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 81, 31))
        self.label.setObjectName("label")

        self.Name_profile = QtWidgets.QLabel(parent=self.centralwidget)
        self.Name_profile.setGeometry(QtCore.QRect(40, 50, 47, 13))
        self.Name_profile.setObjectName("Name_profile")

        self.Name_profile_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Name_profile_2.setGeometry(QtCore.QRect(30, 80, 201, 21))
        self.Name_profile_2.setObjectName("Name_profile_2")

        self.Email_profile = QtWidgets.QLabel(parent=self.centralwidget)
        self.Email_profile.setGeometry(QtCore.QRect(40, 110, 47, 13))
        self.Email_profile.setObjectName("Email_profile")

        self.Email_profile_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Email_profile_2.setGeometry(QtCore.QRect(30, 140, 201, 21))
        self.Email_profile_2.setObjectName("Email_profile_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Профиль"))  # Изменено название окна
        self.Vyhod.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Профиль"))
        self.Name_profile.setText(_translate("MainWindow", "Имя"))
        self.Email_profile.setText(_translate("MainWindow", "Email"))

# main.py
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow
from vhod import Vhod
from register import Register
from profile import Profile
import sys

myConnection = sqlite3.connect("mydatabase.db")  # Подключение к базе данных
myCursor = myConnection.cursor()

app = QApplication(sys.argv)

# Создание окон
acc_win = QMainWindow()
ch_win = QMainWindow()
sin_win = QMainWindow()
sup_win = QMainWindow()

# Создание объектов UI
acc_ui = Vhod()
sin_ui = Register()
sup_ui = Profile()

# Установка UI для окон
acc_ui.setupUi(acc_win)
sin_ui.setupUi(sin_win)
sup_ui.setupUi(sup_win)

# Отображение окна входа
acc_win.show()

app.exec()
myConnection.commit()
myConnection.close()