import datetime
import sys
import os
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QAction, QPlainTextEdit, QMessageBox, QStatusBar, \
    QLabel, QListWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.log_filename = "script18.log"
        self.initUI()

    def initUI(self):
        self.resize(800, 600)
        self.setWindowTitle("Script Window")

        self.list_widget = QListWidget()
        self.setCentralWidget(self.list_widget)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")
        log_menu = menubar.addMenu("Лог")

        open_action = QAction("Открыть...", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        export_action = QAction("Экспорт...", self)
        export_action.triggered.connect(self.export_log)
        log_menu.addAction(export_action)

        add_action = QAction("Добавить в лог", self)
        add_action.triggered.connect(self.add_to_log)
        log_menu.addAction(add_action)

        view_action = QAction("Просмотр", self)
        view_action.triggered.connect(self.view_log)
        log_menu.addAction(view_action)

        self.status_bar = QStatusBar(self)
        self.status = QLabel("")
        self.status_bar.addWidget(self.status, 60)
        self.file_size = QLabel("")
        self.status_bar.addWidget(self.file_size, 40)
        self.setStatusBar(self.status_bar)

        if not os.path.exists(self.log_filename):
            msg = QMessageBox(self)
            msg.setWindowTitle("Внимание")
            msg.setText("Файл лога не найден. Файл будет создан автоматически.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

            with open(self.log_filename, "w") as log_file:
                pass

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                data = file.read()

            # Поиск строк вида "x: type [N]"
            pattern = re.compile(r"(\w+): (int|short|byte) \[(\d+)\]")
            matches = pattern.finditer(data)
            # После поиска добавьте результаты в виджет списка

            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            self.list_widget.addItem(f'Файл {file_name} был обработан {now}')
            self.list_widget.addItem("")
            for match in matches:
                try:
                    tmp_str = f"строка " + str(data.count('\n', 0, match.start()) + 1) + f", позиция {match.start()}: найдено {match.group(0)}"
                    self.list_widget.addItem(tmp_str)
                except Exception as e:
                    print(e)
            self.list_widget.addItem("")

            self.status.setText(f"Обработан файл {file_name}")
            self.file_size.setText(f"{os.path.getsize(file_name):,} байт".replace(",", " "))

    def export_log(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "All Files (*)")
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.list_widget.toPlainText())

    def add_to_log(self):
        with open(self.log_filename, 'a') as log_file:
            for i in range(self.list_widget.count()):
                log_file.write(self.list_widget.item(i).text() + '\n')

    def view_log(self):
        response = QMessageBox.question(self, "Подтверждение", "Вы действительно хотите открыть лог? Данные последних поисков будут потеряны!",
                                 QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            self.list_widget.clear()
            with open(self.log_filename, 'r') as log_file:
                for line in log_file:
                    self.list_widget.addItem(line.strip())

            self.status_message.setText("Открыт лог")
            self.file_size_message.setText("")
#py .\Task3.py

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
