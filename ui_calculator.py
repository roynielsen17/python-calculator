# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(360, 520))
        MainWindow.setMaximumSize(QSize(360, 520))
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"    border-image: url(:/images/background-1.png)\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/* Base Style: All Buttons & Numbers */\n"
"QPushButton {\n"
"    background-color: #1a162b;\n"
"    color: #ffffff;                             /* Crisp bright white text */\n"
"    font-family: \"Segoe UI\", \"Consolas\", sans-serif;\n"
"    font-size: 30px;                            /* Bigger, bolder text */\n"
"    font-weight: 700;                           /* Extra bold weight */\n"
"    border: 1px solid #2d2644;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"/* Hover Effect: Text Glows Light Cyan */\n"
"QPushButton:hover {\n"
"    background-color: #26203e;\n"
"    border: 1px solid #00f2fe;\n"
"    color: #00f2fe;                             /* Text lights up on hover! */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #120e20;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* -------------------------------------------------- */\n"
"/* SPECIAL NEON GLOWS FOR TEXT & BORDERS              */\n"
"/* -------------------------------------------------- */\n"
"\n"
"/* Top Function Keys (C, (), .) */\n"
""
                        "#btn_clear, #btn_bracket, #btn_dot {\n"
"    background-color: rgba(0, 242, 254, 0.08);\n"
"    color: #00f2fe;                             /* Neon Cyan Text */\n"
"    font-size: 30px;\n"
"    font-weight: 800;\n"
"    border: 1px solid rgba(0, 242, 254, 0.4);\n"
"}\n"
"\n"
"#btn_clear:hover, #btn_bracket:hover, #btn_dot:hover {\n"
"    background-color: rgba(0, 242, 254, 0.25);\n"
"    border: 1px solid #00f2fe;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Operator Keys (\u00f7, \u00d7, -, +) */\n"
"#btn_div, #btn_mul, #btn_sub, #btn_add {\n"
"    background-color: rgba(225, 0, 255, 0.08);\n"
"    color: #ff007f;                             /* Neon Magenta Text */\n"
"    font-size: 30px;                            /* Slightly larger for operator symbols */\n"
"    font-weight: 800;\n"
"    border: 1px solid rgba(225, 0, 255, 0.4);\n"
"}\n"
"\n"
"#btn_div:hover, #btn_mul:hover, #btn_sub:hover, #btn_add:hover {\n"
"    background-color: rgba(225, 0, 255, 0.25);\n"
"    border: 1px solid #ff007f;\n"
"    color: #"
                        "ffffff;\n"
"}\n"
"\n"
"/* Equals Key (=) */\n"
"#btn_equal {\n"
"    background: qlineargradient(\n"
"        spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
"        stop:0 #00f2fe, \n"
"        stop:1 #ff007f\n"
"    );\n"
"    color: #ffffff;\n"
"    font-size: 30px;\n"
"    font-weight: 900;\n"
"    border: none;\n"
"}")
        self.display = QLineEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(40, 50, 281, 91))
        self.display.setStyleSheet(u"QLineEdit#display {\n"
"    background-color: rgba(20, 15, 38, 0.85);\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 36px;\n"
"    font-weight: bold;\n"
"    border: 1px solid rgba(0, 242, 254, 0.4);\n"
"    border-radius: 14px;\n"
"    padding: 12px 16px;\n"
"}")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.display.setReadOnly(True)
        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(41, 151, 65, 60))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy1)
        self.btn_clear.setMinimumSize(QSize(60, 60))
        self.btn_bracket = QPushButton(self.centralwidget)
        self.btn_bracket.setObjectName(u"btn_bracket")
        self.btn_bracket.setGeometry(QRect(112, 151, 65, 60))
        sizePolicy1.setHeightForWidth(self.btn_bracket.sizePolicy().hasHeightForWidth())
        self.btn_bracket.setSizePolicy(sizePolicy1)
        self.btn_bracket.setMinimumSize(QSize(60, 60))
        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        self.btn_div.setGeometry(QRect(183, 151, 65, 60))
        sizePolicy1.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy1)
        self.btn_div.setMinimumSize(QSize(60, 60))
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(255, 151, 65, 60))
        sizePolicy1.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy1)
        self.btn_add.setMinimumSize(QSize(60, 60))
        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setGeometry(QRect(41, 430, 135, 61))
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setGeometry(QRect(41, 360, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy1)
        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setGeometry(QRect(112, 360, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy1)
        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setGeometry(QRect(183, 360, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy1)
        self.btn_equal = QPushButton(self.centralwidget)
        self.btn_equal.setObjectName(u"btn_equal")
        self.btn_equal.setGeometry(QRect(255, 360, 65, 130))
        sizePolicy1.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy1)
        self.btn_dot = QPushButton(self.centralwidget)
        self.btn_dot.setObjectName(u"btn_dot")
        self.btn_dot.setGeometry(QRect(183, 430, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy1)
        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        self.btn_sub.setGeometry(QRect(255, 221, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy1)
        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setGeometry(QRect(41, 221, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy1)
        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setGeometry(QRect(183, 221, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy1)
        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setGeometry(QRect(112, 221, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy1)
        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setGeometry(QRect(112, 291, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy1)
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setGeometry(QRect(41, 291, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy1)
        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        self.btn_mul.setGeometry(QRect(255, 291, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy1)
        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setGeometry(QRect(183, 291, 65, 59))
        sizePolicy1.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_bracket.setText(QCoreApplication.translate("MainWindow", u"( )", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0        ", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
    # retranslateUi

