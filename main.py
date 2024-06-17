import sqlite3

from PyQt5.uic.properties import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from vhod import Vhod
from register import Register
from profile import Profile
import sys

# Подключение к базе данных
myConnection = sqlite3.connect("Bada1.db")
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

# --- Обработчики событий ---

# Обработчик входа
def handle_login():
    email = acc_ui.Email_Vod.text()
    password = acc_ui.Pass_vod.text()
    myCursor.execute("SELECT * FROM Users WHERE Email=? AND Password=?", (email, password))
    user = myCursor.fetchone()
    if user:
        # Успешный вход
        sup_ui.Name_profile_2.setText(user[0])  # Установить имя в профиле
        sup_ui.Email_profile_2.setText(user[1])  # Установить email в профиле
        sup_win.show()
        acc_win.close()
    else:
        # Неверный логин или пароль
        QMessageBox.information(acc_win, "Ошибка", "Неверный пароль/логин")

acc_ui.Vhod.clicked.connect(handle_login)

# Обработчик регистрации
def handle_register():
    name = sin_ui.Name_vod_reg.text()
    email = sin_ui.Email_vod_reg.text()
    password = sin_ui.Pass_vod.text()
    try:
        myCursor.execute("INSERT INTO Users (UserName, Email, Password) VALUES (?, ?, ?)", (name, email, password))
        myConnection.commit()
        QMessageBox.information(sin_win, "Успешно", "Регистрация прошла успешно!")
        sin_win.close()
        acc_win.show()
    except sqlite3.IntegrityError:
        error_message = QMessageBox(QMessageBox.Warning, "Ошибка", "Этот email уже используется", QMessageBox.Ok)
        error_message.exec()

sin_ui.Zaregistr.clicked.connect(handle_register)
# Обработчик выхода
def handle_exit():
    sup_win.close()
    acc_win.show()

sup_ui.Vyhod.clicked.connect(handle_exit)

# --- Обработчики выхода ---
sin_ui.Vyhod.clicked.connect(lambda: [sin_win.close(), acc_win.show()])  # Выход в окно входа
acc_ui.Register.clicked.connect(lambda: [acc_win.close(), sin_win.show()]) # Переход в окно регистрации

# Отображение окна входа
acc_win.show()

app.exec()
myConnection.commit()
myConnection.close()
