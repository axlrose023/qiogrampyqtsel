# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_label(object):
    def setupUi(self, label):
        label.setObjectName("label")
        label.resize(280, 320)
        self.centralwidget = QtWidgets.QWidget(label)
        self.centralwidget.setObjectName("centralwidget")
        self.labelresult = QtWidgets.QLabel(self.centralwidget)
        self.labelresult.setGeometry(QtCore.QRect(0, 0, 400, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelresult.setFont(font)
        self.labelresult.setStyleSheet("background-color: rgb(156, 26, 134);\n"
"color: rgb(255, 255, 255);")
        self.labelresult.setObjectName("labelresult")
        self.pushButton_zero = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zero.setGeometry(QtCore.QRect(0, 250, 101, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_zero.setFont(font)
        self.pushButton_zero.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_zero.setObjectName("pushButton_zero")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(100, 250, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"background-color: rgb(85, 255, 0);")
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(210, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_plus.setAutoRepeatDelay(297)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(210, 110, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_mult = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mult.setGeometry(QtCore.QRect(210, 180, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_mult.setFont(font)
        self.pushButton_mult.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"background-color: rgb(0, 0, 255);")
        self.pushButton_mult.setObjectName("pushButton_mult")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(210, 250, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton_div.setObjectName("pushButton_div")
        label.setCentralWidget(self.centralwidget)

        self.retranslateUi(label)
        QtCore.QMetaObject.connectSlotsByName(label)
        self.add_functions()
        self.is_equal = False


    def retranslateUi(self, label):
        _translate = QtCore.QCoreApplication.translate
        label.setWindowTitle(_translate("label", "Калькулятор"))
        self.labelresult.setText(_translate("label", "0"))
        self.pushButton_zero.setText(_translate("label", "0"))
        self.pushButton_1.setText(_translate("label", "1"))
        self.pushButton_2.setText(_translate("label", "2"))
        self.pushButton_3.setText(_translate("label", "3"))
        self.pushButton_4.setText(_translate("label", "4"))
        self.pushButton_5.setText(_translate("label", "5"))
        self.pushButton_6.setText(_translate("label", "6"))
        self.pushButton_7.setText(_translate("label", "7"))
        self.pushButton_8.setText(_translate("label", "8"))
        self.pushButton_9.setText(_translate("label", "9"))
        self.pushButton_equal.setText(_translate("label", "="))
        self.pushButton_plus.setText(_translate("label", "+"))
        self.pushButton_minus.setText(_translate("label", "-"))
        self.pushButton_mult.setText(_translate("label", "*"))
        self.pushButton_div.setText(_translate("label", "/"))

    def add_functions(self):
        self.pushButton_zero.clicked.connect(lambda: self.write_number(self.pushButton_zero.text()))
        self.pushButton_1.clicked.connect(lambda: self.write_number(self.pushButton_1.text()))
        self.pushButton_2.clicked.connect(lambda: self.write_number(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.write_number(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.write_number(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.write_number(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.write_number(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.write_number(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.write_number(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.write_number(self.pushButton_9.text()))
        self.pushButton_plus.clicked.connect(lambda: self.write_number(self.pushButton_plus.text()))
        self.pushButton_minus.clicked.connect(lambda: self.write_number(self.pushButton_minus.text()))
        self.pushButton_mult.clicked.connect(lambda: self.write_number(self.pushButton_mult.text()))
        self.pushButton_div.clicked.connect(lambda: self.write_number(self.pushButton_div.text()))
        self.pushButton_equal.clicked.connect(self.results)


    def write_number(self, number):
        if self.labelresult.text() == "0" or self.is_equal == True:
            self.labelresult.setText(number)
            self.is_equal = False
        else:
            self.labelresult.setText(self.labelresult.text()+number)
    def results(self):
        if not self.is_equal:
            res = eval(self.labelresult.text())
            self.labelresult.setText("Результат: " + str(res))
            self.is_equal = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset)
            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Два раза действие не выполнить")
            error.setDetailedText("Детали")
            error.buttonClicked.connect(self.popup_action)

            error.exec_()
    def popup_action(self, btn):
        if btn.text() == "Ok":
            print("OK")
        elif btn.text() == "Reset":
            self.labelresult.setText("")
            self.is_equal



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    label = QtWidgets.QMainWindow()
    ui = Ui_label()
    ui.setupUi(label)
    label.show()
    sys.exit(app.exec_())
