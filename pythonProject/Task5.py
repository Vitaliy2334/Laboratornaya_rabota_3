import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from task5_ui import Ui_MainWindow


class Task5Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # инициализация UI
        super().__init__()
        self.setupUi(self)

        self.string = ""

        # бинд кнопок на методы
        self.pushButton.clicked.connect(self.format_string)
        self.delWordsCheckBox.clicked.connect(self.del_words_checkbox_change_status)
        self.sortCheckBox.clicked.connect(self.sort_change_status)
        self.sortSizeRadioButton.clicked.connect(self.change_state_sort_size)
        self.sortLexRadioButton.clicked.connect(self.change_state_sort_lex)

    # меняет статус радио кнопки для сортировки строки
    def change_state_sort_size(self):
        if self.sortSizeRadioButton.isChecked():
            self.sortSizeRadioButton.setChecked(False)

    # меняет статус радио кнопки для сортировки строки
    def change_state_sort_lex(self):
        if self.sortLexRadioButton.isChecked():
            self.sortSizeRadioButton.setChecked(False)

    # метод для изменения статуса чекбокса удаления слов размером меньше чем X
    def del_words_checkbox_change_status(self):
        if not self.delWordsCheckBox.isChecked():
            self.spinBox.setEnabled(False)
        elif self.delWordsCheckBox.isChecked():
            self.spinBox.setEnabled(True)

    # метод для изменения стаутса чекбокса сортировки
    def sort_change_status(self):
        if self.sortCheckBox.isChecked():
            self.sortSizeRadioButton.setEnabled(True)
            self.sortLexRadioButton.setEnabled(True)
        elif not self.sortCheckBox.isChecked():
            self.sortSizeRadioButton.setEnabled(False)
            self.sortLexRadioButton.setEnabled(False)

    # метод для форматирования строки
    def format_string(self):
        self.string = self.startTextEdit.toPlainText()

        if self.delWordsCheckBox.isChecked():
            self.remove_short_words(self.spinBox.value())
        if self.replaceDigitsCheckBox.isChecked():
            self.replace_digits()
        if self.insertSpacesCheckBox.isChecked():
            self.insert_spaces()
        if self.sortCheckBox.isChecked():
            if self.sortSizeRadioButton.isChecked():
                self.sort_by_size()
            elif self.sortLexRadioButton.isChecked():
                self.sort_lexicographically()

        self.ResultTextEdit.setText(self.string)

    # метод для удалия слов, длина которых меньше чем n
    def remove_short_words(self, n):
        words = self.string.split()
        words = [word for word in words if len(word) >= n]
        self.string = ' '.join(words)

    # метод для замены цифр на *
    def replace_digits(self):
        self.string = ''.join(['*' if char.isdigit() else char for char in self.string])

    # метод дял вставки пробелов между каждым символом в строке
    def insert_spaces(self):
        self.string = ' '.join(self.string)

    # метод для сортировки строки по размеру слов
    def sort_by_size(self):
        words = self.string.split()
        words.sort(key=len)
        self.string = ' '.join(words)

    # метод для сортировки строки лексикологически
    def sort_lexicographically(self):
        words = self.string.split()
        words.sort()
        self.string = ' '.join(words)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Task5Window()
    main_window.show()
    sys.exit(app.exec_())