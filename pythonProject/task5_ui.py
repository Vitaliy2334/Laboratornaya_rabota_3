# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_for_task5.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(438, 313)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 21))
        self.label.setObjectName("label")
        self.startTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.startTextEdit.setGeometry(QtCore.QRect(90, 30, 321, 21))
        self.startTextEdit.setObjectName("startTextEdit")
        self.delWordsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.delWordsCheckBox.setGeometry(QtCore.QRect(90, 70, 191, 17))
        self.delWordsCheckBox.setObjectName("delWordsCheckBox")
        self.replaceDigitsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.replaceDigitsCheckBox.setGeometry(QtCore.QRect(90, 90, 161, 17))
        self.replaceDigitsCheckBox.setObjectName("replaceDigitsCheckBox")
        self.sortCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.sortCheckBox.setGeometry(QtCore.QRect(90, 130, 171, 17))
        self.sortCheckBox.setObjectName("sortCheckBox")
        self.insertSpacesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.insertSpacesCheckBox.setGeometry(QtCore.QRect(90, 110, 231, 17))
        self.insertSpacesCheckBox.setObjectName("insertSpacesCheckBox")
        self.sortSizeRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.sortSizeRadioButton.setEnabled(False)
        self.sortSizeRadioButton.setGeometry(QtCore.QRect(120, 150, 82, 17))
        self.sortSizeRadioButton.setObjectName("sortSizeRadioButton")
        self.sortLexRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.sortLexRadioButton.setEnabled(False)
        self.sortLexRadioButton.setGeometry(QtCore.QRect(120, 170, 131, 17))
        self.sortLexRadioButton.setObjectName("sortLexRadioButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 210, 321, 41))
        self.pushButton.setObjectName("pushButton")
        self.ResultTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ResultTextEdit.setGeometry(QtCore.QRect(90, 280, 321, 21))
        self.ResultTextEdit.setReadOnly(True)
        self.ResultTextEdit.setObjectName("ResultTextEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 71, 21))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setEnabled(False)
        self.spinBox.setGeometry(QtCore.QRect(280, 70, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 70, 31, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StringFormatter Demo"))
        self.label.setText(_translate("MainWindow", "Ваша строка:"))
        self.delWordsCheckBox.setText(_translate("MainWindow", "Удалить слова размером меньше"))
        self.replaceDigitsCheckBox.setText(_translate("MainWindow", "Заменить все цифры на *"))
        self.sortCheckBox.setText(_translate("MainWindow", "Сортировать слова в строке"))
        self.insertSpacesCheckBox.setText(_translate("MainWindow", "Вставить по пробелу между символами"))
        self.sortSizeRadioButton.setText(_translate("MainWindow", "По размеру"))
        self.sortLexRadioButton.setText(_translate("MainWindow", "Лексикографически"))
        self.pushButton.setText(_translate("MainWindow", "Форматировать"))
        self.label_2.setText(_translate("MainWindow", "Результат:"))
        self.label_3.setText(_translate("MainWindow", "букв"))
