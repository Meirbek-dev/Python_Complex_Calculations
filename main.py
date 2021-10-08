#!/usr/bin/env python3
# coding=utf-8

import math
import sys
from random import randint

# from PyQt6.QtGui import (QPixmap)
from PyQt6.QtWidgets import *
from PyQt6.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)
        # self.setWindowTitle('Сложные табличные вычисления PyQt6')
        # self.setWindowIcon(QIcon('logo.png'))
        # self.label_img.setPixmap(QPixmap('variant.png'))

        self.btn_random_number.clicked.connect(self.fill_random_numbers)
        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_exit.clicked.connect(self.exit)

    def fill_random_numbers(self):
        i = 0
        while i < self.tableWidget.rowCount():
            random_num = randint(0, 100)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(random_num)))
            i += 1

    def solve(self):
        try:
            if validation_of_data(self.tableWidget):
                i = sum_of_multiplication_of_k_i_minus_1 = 0
                j = multiplication_of_k_i_minus_1 = 1
                self.tableWidget.resizeColumnToContents(0)
                while i < self.tableWidget.rowCount():
                    item = self.tableWidget.item(i, 0).text()
                    self.tableWidget.resizeColumnToContents(1)
                    a = float(self.lineEdit_a.text())
                    b = float(self.lineEdit_b.text())
                    try:
                        # item_minus_1 выкинет исключение при первой итерации,
                        # поэтому перехватываем её и выводим none
                        item_minus_1 = self.tableWidget.item(i - 1, 0).text()
                        multiplication_of_k_i_minus_1 *= int(item_minus_1)
                        sum_of_multiplication_of_k_i_minus_1 += multiplication_of_k_i_minus_1
                        answer = (((math.cos(int(item)) ** 2) / ((a ** 2 + b ** 2) - (math.sin(int(item))))) *
                                  float(sum_of_multiplication_of_k_i_minus_1))
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(answer)))
                    except Exception:
                        self.tableWidget.setItem(i, j, QTableWidgetItem('none'))
                    i += 1
                self.label_error.setStyleSheet('color: rgb(0, 200, 0); font: bold')
                self.label_error.setText('Задание выполнено')
        except Exception:
            self.label_error.setText('Введены некорректные данные!')
            self.label_error.setStyleSheet('color: rgb(200, 0, 0); font: bold')

    def clear(self):
        self.tableWidget.clearContents()
        self.label_error.setText('')
        self.lineEdit_a.setText('')
        self.lineEdit_b.setText('')

    def exit(self):
        self.close()


def validation_of_data(table_widget):
    i = 0
    while i < table_widget.rowCount():
        try:
            float(table_widget.item(i, 0).text())
            i += 1
        except Exception:
            return False
    return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())
