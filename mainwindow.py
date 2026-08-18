from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_calculator import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)

        self.display.setText("0")

        self.btn_0.clicked.connect(lambda: self.append_character("0"))
        self.btn_1.clicked.connect(lambda: self.append_character("1"))
        self.btn_2.clicked.connect(lambda: self.append_character("2"))
        self.btn_3.clicked.connect(lambda: self.append_character("3"))
        self.btn_4.clicked.connect(lambda: self.append_character("4"))
        self.btn_5.clicked.connect(lambda: self.append_character("5"))
        self.btn_6.clicked.connect(lambda: self.append_character("6"))
        self.btn_7.clicked.connect(lambda: self.append_character("7"))
        self.btn_8.clicked.connect(lambda: self.append_character("8"))
        self.btn_9.clicked.connect(lambda: self.append_character("9"))
        self.btn_add.clicked.connect(lambda: self.append_character("+"))
        self.btn_sub.clicked.connect(lambda: self.append_character("-"))
        self.btn_div.clicked.connect(lambda: self.append_character("/"))
        self.btn_mul.clicked.connect(lambda: self.append_character("*"))
        self.btn_dot.clicked.connect(lambda: self.append_character("."))
        self.btn_clear.clicked.connect(self.clear_display)
        self.btn_bracket.clicked.connect(self.set_bracket)
        self.btn_equal.clicked.connect(self.calculate_result)

    def append_character(self, char):
        current_text = self.display.text()
        if current_text == "0" or current_text == "Error":
            if (
                char in "+-/*."
            ):  # If the input is any of these operations don't replace with 0.
                self.display.setText(current_text + char)
            else:
                self.display.setText(char)  # If it's normal digits then replace with 0.
        else:
            self.display.setText(
                current_text + char
            )  # If not zero, then do not overwrite.

    def clear_display(self):
        self.display.setText("0")

    def set_bracket(self):
        current_text = self.display.text()

        # Check the number of brackets
        open_count = current_text.count("(")
        close_count = current_text.count(")")

        # Validate the last character to avoid errors
        if current_text:
            last_char = current_text[-1]
        else:
            last_char = ""

        # If there is an open bracket and last chatacter isn't an operator
        if open_count > close_count and last_char not in "+-/*(.":
            self.append_character(")")
        else:
            # Start a new bracket with (
            if current_text == "0":
                self.display.setText("(")
            elif last_char in "0123456789":
                self.display.setText(current_text + "*(")
            else:
                self.append_character("(")

    def calculate_result(self):
        current_text = self.display.text()

        # Do not do anytihing in an empty screen
        if not current_text or current_text == 0:
            return

        try:
            # validate symbols
            expression = current_text.replace("x", "*")

            # calculate the result
            result = eval(expression)

            # format result
            if isinstance(result, float):
                # check for whole number
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 8)

            self.display.setText(str(result))

        except Exception:
            # in case of invalid input
            self.display.setText("Error")
