from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btn_names = [
            ["c", "+/-", "%", "<--"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "x"],
            ["1", "2", "3", "-"],
            ["0", ".", "+", "="],
        ]
        self.sign = self.num1 = self.num2 = ""

        self.setWindowTitle("Calculator")

        self.mainBox = QVBoxLayout()
        self.mainBox.setAlignment(Qt.AlignTop)

        self.layout1 = QHBoxLayout()

        self.input = QLineEdit()
        self.layout1.addWidget(self.input)
        self.mainBox.addLayout(self.layout1)

        for i in range(len(self.btn_names)):
            self.create_buttons(self.btn_names[i])

        container = QWidget()
        container.setLayout(self.mainBox)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def create_buttons(self, button_names):
        some_layout = QHBoxLayout()
        for i in range(len(button_names)):
            btn = QPushButton(button_names[i])
            btn.clicked.connect(lambda ch, char=button_names[i]: self.btn_actions(char))
            some_layout.addWidget(btn)

            self.mainBox.addLayout(some_layout)

    def btn_actions(self, char):
        if (not self.input.text() or self.sign) and char == ".":
            self.extend_number("0.")
        elif char.isnumeric() or (char == "." and "." not in self.input.text()):
            self.extend_number(char)
        else:
            self.sign_action(char)

    def sign_action(self, char):
        if char in ["+", "-", "x", "/", "%"]:
            self.sign = char
            self.num2 = ""
        elif char == "=":
            self.equal()
        elif char == "c":
            self.c_clicked()
        elif char == "<--":
            self.backspace()
        elif char == "+/-" and self.input.text():
            if self.sign:
                self.pos_neg("2")
            else:
                self.pos_neg("1")

    def pos_neg(self, num):
        if num == "2":
            if self.num2[0] != "-":
                self.num2 = "-" + self.num2
            else:
                self.num2 = self.num2[1:]
            self.input.setText(self.num2)
        else:
            if self.num1[0] != "-":
                self.num1 = "-" + self.num1
            else:
                self.num1 = self.num1[1:]
            self.input.setText(self.num1)

    def extend_number(self, char):
        if self.sign in ["+", "-", "x", "/", "%"]:
            self.num2 += char
            self.input.setText(self.num2)
        else:
            self.num1 += char
            self.input.setText(self.num1)

    def equal(self):
        if self.sign in ["+", "-", "x", "/", "%"]:
            if self.sign == "+":
                self.num1 = float(self.num1) + float(self.num2)
            elif self.sign == "-":
                self.num1 = float(self.num1) - float(self.num2)
            elif self.sign == "x":
                self.num1 = float(self.num1) * float(self.num2)
            elif self.sign == "/":
                self.num1 = float(self.num1) / float(self.num2)
            elif self.sign == "/":
                self.num1 = float(self.num1) / float(self.num2)
            elif self.sign == "%":
                self.num1 = float(self.num1) * float(self.num2) / 100

            son = float(self.num1)
            if son == math.floor(son):
                self.input.setText(str(int(self.num1)))
            else:
                self.input.setText(str(float(self.num1)))

    def c_clicked(self):
        self.sign = self.num1 = self.num2 = ""
        self.input.setText("")

    def backspace(self):
        if self.sign and self.num2:
            self.num2 = self.num2[:-1]
            self.input.setText(self.num2)
        elif self.num1:
            self.num1 = self.num1[:-1]
            self.input.setText(self.num1)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()