import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from vhod import Vhod
from register import Register
from profile import Profile
from newpass import NewPass
import sys

# Подключение к базе данных
myConnection = sqlite3.connect("Baza.db")
myCursor = myConnection.cursor()
app = QApplication(sys.argv)

# Создание окон
acc_win = QMainWindow()
sin_win = QMainWindow()
sup_win = QMainWindow()
newpass_win = QMainWindow()

# Создание объектов UI
acc_ui = Vhod()
sin_ui = Register()
sup_ui = Profile()
newpass_ui = NewPass()

# Установка UI для окон
acc_ui.setupUi(acc_win)
sin_ui.setupUi(sin_win)
sup_ui.setupUi(sup_win)
newpass_ui.setupUi(newpass_win)


# --- Обработчики событий ---

# Обработчик входа
def handle_login():
    email = acc_ui.Email_Vod.text()
    password = acc_ui.Pass_vod.text()

    if '@' not in email:
        QMessageBox.warning(acc_win, "Ошибка", "Некорректный email")
        return

    myCursor.execute("SELECT * FROM USER WHERE Email=? AND Password=?", (email, password))
    user = myCursor.fetchone()

    if user:
        # Успешный вход
        sup_ui.Name_prof.setText(user[1])  # Установить имя в профиле
        sup_ui.Surname_prof.setText(user[2])
        sup_ui.Ot_Name_prof.setText(user[3])
        sup_ui.NickName_prof.setText(user[4])
        sup_ui.Email_prof.setText(user[5])  # Установить email в профиле
        sup_ui.Pass_prof.setText(user[6])
        sup_win.show()
        acc_win.close()
        acc_ui.Email_Vod.clear()
        acc_ui.Pass_vod.clear()
    else:
        # Неверный логин или пароль
        QMessageBox.information(acc_win, "Ошибка", "Неверный пароль/логин")


acc_ui.Vhod.clicked.connect(handle_login)


# Обработчик регистрации
def handle_register():
    name = sin_ui.Name_reg.text()
    surname = sin_ui.Surname_reg.text()
    otname = sin_ui.Ot_Name_reg.text()
    nickname = sin_ui.NickName_reg.text()
    email = sin_ui.Email_reg.text()
    password = sin_ui.Pass_reg.text()

    if '@' not in email:
        QMessageBox.warning(sin_win, "Ошибка", "Некорректный email")
        return

    try:
        myCursor.execute(
            "INSERT INTO USER (Name, Surname, Ot_name, NickName, Email, Password) VALUES (?, ?, ?, ?, ?, ?)",
            (name, surname, otname, nickname, email, password))
        myConnection.commit()
        QMessageBox.information(sin_win, "Успешно", "Регистрация прошла успешно!")
        sin_win.close()
        acc_win.show()
        sin_ui.Name_reg.clear()
        sin_ui.Surname_reg.clear()
        sin_ui.Ot_Name_reg.clear()
        sin_ui.NickName_reg.clear()
        sin_ui.Email_reg.clear()
        sin_ui.Pass_reg.clear()
    except sqlite3.IntegrityError:
        QMessageBox.warning(sin_win, "Ошибка", "Этот email уже используется")


sin_ui.Zaregistr.clicked.connect(handle_register)


# Обработчик выхода из профиля
def handle_exit():
    sup_win.close()
    acc_win.show()


sup_ui.Vyhod.clicked.connect(handle_exit)

# Обработчик выхода из регистрации
sin_ui.Vyhod.clicked.connect(lambda: [sin_win.close(), acc_win.show()])  # Выход в окно входа

# Обработчик перехода в регистрацию
acc_ui.Register.clicked.connect(lambda: [acc_win.close(), sin_win.show()])  # Переход в окно регистрации


# Обработчик "Забыл пароль"
def handle_forgot_password():
    acc_win.close()
    newpass_win.show()


acc_ui.Zabl_pass.clicked.connect(handle_forgot_password)


# Обработчик смены пароля
def handle_change_password():
    nickname = newpass_ui.NickName_pass.text()
    email = newpass_ui.Email_pass.text()
    new_password = newpass_ui.NewPass_pass.text()
    confirm_password = newpass_ui.Repeat_NewPass_pass.text()

    if new_password == confirm_password:
        myCursor.execute("UPDATE USER SET Password=? WHERE NickName=? AND Email=?", (new_password, nickname, email))
        myConnection.commit()
        QMessageBox.information(newpass_win, "Успешно", "Пароль успешно изменен!")
        newpass_win.close()
        acc_win.show()
        newpass_ui.NickName_pass.clear()
        newpass_ui.Email_pass.clear()
        newpass_ui.NewPass_pass.clear()
        newpass_ui.Repeat_NewPass_pass.clear()
    else:
        QMessageBox.warning(newpass_win, "Ошибка", "Пароли не совпадают!")


newpass_ui.OK.clicked.connect(handle_change_password)

# Обработчик выхода из окна смены пароля
newpass_ui.Vyhod.clicked.connect(lambda: [newpass_win.close(), acc_win.show()])  # Выход в окно входа

# Отображение окна входа
acc_win.show()

app.exec()
myConnection.commit()
myConnection.close()