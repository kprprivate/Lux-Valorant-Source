from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
from . import resources_rc

class Ui_menuMain(object):
    def setupUi(self, menuMain):
        if not menuMain.objectName():
            menuMain.setObjectName(u"menuMain")
        menuMain.resize(725, 440)
        menuMain.setMinimumSize(QSize(725, 440))
        menuMain.setMaximumSize(QSize(16777215, 16777215))
        self.styleSheet = QWidget(menuMain)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* Dark Theme - Black with Green Details */\n"
"/* Background */\n"
"QWidget {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\";\n"
"	\n"
"	background-color: rgb(14, 15, 18);\n"
"}\n"
"\n"
"/* Tooltip */\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid rgb(106, 68, 177); /* Green */\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* Bg App */\n"
"#bgApp {\n"
"    background-color: rgb(15, 15, 15);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Left Menu */\n"
"#leftMenuBg {\n"
"    background-color: rgb(15, 15, 15);\n"
"}\n"
"#topLogo {\n"
"    background-color: rgb(15, 15, 15);\n"
"    background-position: centered;\n"
"    back"
                        "ground-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp {\n"
"    font: 63 12pt \"Segoe UI Semibold\";\n"
"}\n"
"#titleLeftDescription {\n"
"    font: 8pt \"Segoe UI\";\n"
"    color: rgb(106, 68, 177); /* Green */\n"
"}\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushB"
                        "utton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame {\n"
"    border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: rgb(37, 41, 48);\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo {\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/* Extra Tab */\n"
"#extraLeftBox {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
""
                        "}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"#extraCloseColumnBtn:hover {\n"
"    background-color: rgb(196, 161, 249);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#extraCloseColumnBtn:pressed {\n"
"    background-color: rgb(180, 141, 238);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Extra Content */\n"
"#extraContent {\n"
"    border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparen"
                        "t;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* DoubleSpinBox */\n"
"QDoubleSpinBox {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"/* SpinBox */\n"
"QSpinBox {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"}\n"
"QSpinBox:hover {\n"
"    border: 2px solid rgba(106, 68, 177, 50);\n"
"}\n"
"\n"
"/* Content App */\n"
"#contentTopBg {\n"
"    background-color: rgb(15, 15, 15);\n"
"}\n"
"#contentBottom {\n"
"    border-top: 3px solid rgb(15, 15, 15"
                        ");\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"#rightButtons .QPushButton:hover {\n"
"    background-color: rgb(44, 49, 57);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#rightButtons .QPushButton:pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#themeSettingsTopDetail {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"}\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#bottomBar QLabel {\n"
"    font-size: 11px;\n"
"    color: rgb(113, 126, 149);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 2px;\n"
"}\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"    backgr"
                        "ound-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"    background-color: rgb(15, 15, 15);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* QTableWidget */\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 58);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item {\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: rgb(33, 37, "
                        "43);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical {\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* LineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(69, 255, 252);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 1"
                        "24);\n"
"}\n"
"\n"
"/* PlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(69, 255, 252);\n"
"}\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"    width: 8px;\n"
"}\n"
"QPlainTextEdit QScrollBar:horizontal {\n"
"    height: 8px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(106, 68, 177);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-rig"
                        "ht-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(106, 68, 177);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"  "
                        "  border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:"
                        "checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* ComboBox */\n"
"QComboBox {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"   "
                        " border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"    background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(69, 255, 252);\n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::ha"
                        "ndle:horizontal:hover {\n"
"    background-color: rgb(153, 0, 255); /* Lighter Green */\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(174, 0, 255); /* Dark Green */\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(153, 0, 255); /* Lighter Green */\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(174, 0, 255); /* Dark Green */\n"
"}\n"
"\n"
"/* CommandLinkButton */\n"
"QCommandLinkButton {\n"
"    color: rgb(69, 255, 252);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: rgb(0"
                        ", 255, 255); /* Green */\n"
"}\n"
"QCommandLinkButton:hover {\n"
"    color: rgb(106, 68, 177); /* Green */\n"
"    background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"    color: rgb(106, 68, 177);\n"
"    background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* Button */\n"
"#pagesContainer QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* Option Box */\n"
"#configBox QFrame {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QWidget {\n"
"    color: rgb(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Tooltip */\n"
"QToolTip {\n"
"    col"
                        "or: #ffffff;\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid rgb(69, 255, 252);\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* Bg App */\n"
"#bgApp {\n"
"    background-color: rgb(40, 44, 52);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#topLogo {\n"
"    background-color: rgb(33, 37, 43);\n"
"    background-position: centered;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp {\n"
"    font: 63 12pt \"Segoe UI Semibold\";\n"
"}\n"
"#titleLeftDescription {\n"
"    font: 8pt \"Segoe UI\";\n"
"    color: rgb(106, 68, 177);\n"
"}\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border:"
                        " none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame {\n"
"    border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"    background-position: left center;\n"
"    background"
                        "-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: rgb(37, 41, 48);\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"    color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"    background-color: rgb(106, 68, 177);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo {\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"/* Extra Tab */\n"
"#extraLeftBox {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg {\n"
"    background-color: rgb(106, 68, 177);\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    bo"
                        "rder-radius: 5px;\n"
"}\n"
"#extraCloseColumnBtn:hover {\n"
"    background-color: rgb(196, 161, 249);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#extraCloseColumnBtn:pressed {\n"
"    background-color: rgb(180, 141, 238);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Extra Content */\n"
"#extraContent {\n"
"    border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* Content App */\n"
"#contentTopBg {\n"
"    background-color: rgb(33, 37, 43);"
                        "\n"
"}\n"
"#contentBottom {\n"
"    border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"#rightButtons .QPushButton:hover {\n"
"    background-color: rgb(44, 49, 57);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#rightButtons .QPushButton:pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#themeSettingsTopDetail {\n"
"    background-color: rgb(106, 68, 177);\n"
"}\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar {\n"
"    background-color: rgb(44, 49, 58);\n"
"}\n"
"#bottomBar QLabel {\n"
"    font-size: 11px;\n"
"    color: rgb(113, 126, 149);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-bottom: 2px;\n"
"}\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/*"
                        " MENUS */\n"
"#contentSettings .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* QTableWidget */\n"
"QTableWidget {\n"
"    background-color: transparent;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 58);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item {\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(106, 68, 177);\n"
"}\n"
"QHeaderView::section {\n"
""
                        "    background-color: rgb(33, 37, 43);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"    background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"    background-color: rgb(33, 37, 43);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical {\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* LineEdit */\n"
"QLineEdit {\n"
"    background-color: rgb(33, 37, 43);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(69, 255, 252);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"  "
                        "  border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* PlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    padding: 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(69, 255, 252);\n"
"}\n"
"QPlainTextEdit QScrollBar:vertical {\n"
"    width: 8px;\n"
"}\n"
"QPlainTextEdit QScrollBar:horizontal {\n"
"    height: 8px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
""
                        "    border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(153, 0, 255); /* Lighter Green */\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(174, 0, 255); /* Dark Green */\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(106, 68, 177); /* Green */\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(153, 0, 255); /* Lighter Green */\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(174, 0, 255); /* Dark Green */\n"
"}\n"
"\n"
"/* CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
""
                        "    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"}\n"
"\n"
"/* ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar"
                        "::handle:horizontal {\n"
"    background: rgb(106, 68, 177);\n"
"    min-width: 25px;\n"
"    border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal,\n"
"QScrollBar::down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    b"
                        "order-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(106, 68, 177);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:vertical,\n"
"QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/* CommandLinkButton */\n"
"QCommandLinkButton {"
                        "\n"
"    color: rgb(69, 255, 252);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    color: rgb(106, 68, 177); /* Green */\n"
"}\n"
"QCommandLinkButton:hover {\n"
"    color: rgb(106, 68, 177); /* Green */\n"
"    background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"    color: rgb(106, 68, 177);\n"
"    background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* Button */\n"
"#pagesContainer QPushButton {\n"
"    border: 2px solid rgb(52, 59, 72);\n"
"    border-radius: 5px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"    background-color: rgb(57, 65, 80);\n"
"    border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"    background-color: rgb(35, 40, 49);\n"
"    border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"/* Option Box */\n"
"#configBox QFrame {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"\n"
"QWidget {\n"
"    color: rgb"
                        "(221, 221, 221);\n"
"    font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* Tooltip */\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(33, 37, 43, 180);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"    background-image: none;\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 2px solid rgb(69, 255, 252);\n"
"    text-align: left;\n"
"    padding-left: 8px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* Bg App */\n"
"#bgApp {\n"
"    background-color: rgb(40, 44, 52);\n"
"    border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"#topLogo {\n"
"    background-color: rgb(33, 37, 43);\n"
"    background-position: centered;\n"
"    background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp {\n"
"    font: 63 12pt \"Segoe UI Semibold\";\n"
"}\n"
"#titleLeftDescription {\n"
"    font: 8pt \"Segoe UI\";\n"
"    color: rgb(106, 68, 177);\n"
"}\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPus"
                        "hButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 20px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"    background-color: rgb(106, 68, 177);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame {\n"
"    border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
""
                        "\n"
"/* DoubleSpinBox */\n"
"QDoubleSpinBox {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"/* SpinBox */\n"
"QSpinBox {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(33, 37, 43);\n"
"    padding-left: 10px;\n"
"}\n"
"QSpinBox:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#topButtons .QPushButton {\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}\n"
"#topButtons .QPushButton:hover {\n"
"    background-color: rgb(44, 49, 57);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}\n"
"#topButtons .QPushButton:pressed {\n"
"    background-color: rgb(23, 26, 30);\n"
"    border-style: solid;\n"
"    border-radius: 4px;\n"
"}")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.bgApp)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"#contentTopBg {\n"
"	background-image: url(:/images/images/images/lux.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-color: rgb(22, 24, 29);\n"
"}")
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.left = QFrame(self.contentTopBg)
        self.left.setObjectName(u"left")
        self.left.setMinimumSize(QSize(60, 50))
        self.left.setMaximumSize(QSize(60, 50))
        self.left.setStyleSheet(u".QPushButton {\n"
"    background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-left: 22px solid transparent;\n"
"    background-color: transparent;\n"
"    text-align: left;\n"
"    padding-left: 44px;\n"
"}\n"
".QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
".QFrame {\n"
"	background-color: rgb(22, 24, 29);\n"
"}")
        self.left.setFrameShape(QFrame.Shape.StyledPanel)
        self.left.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.left)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.left)
        self.toggleButton.setObjectName(u"toggleButton")
        self.toggleButton.setMinimumSize(QSize(60, 45))
        self.toggleButton.setMaximumSize(QSize(60, 45))
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-options-horizontal.png);")

        self.horizontalLayout_31.addWidget(self.toggleButton)


        self.horizontalLayout.addWidget(self.left, 0, Qt.AlignmentFlag.AlignLeft)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMaximumSize(QSize(60, 16777215))
        self.rightButtons.setStyleSheet(u"background-image: \"\";\n"
"background-color: rgb(22, 24, 29);")
        self.rightButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setStyleSheet(u".QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
".QPushButton {\n"
"	outline: 0;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.minimizeAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setStyleSheet(u".QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}\n"
"\n"
".QPushButton {\n"
"	outline: 0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)


        self.verticalLayout_21.addWidget(self.contentBox)

        self.mainContent = QFrame(self.bgApp)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setMinimumSize(QSize(0, 100))
        self.mainContent.setStyleSheet(u"")
        self.mainContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.mainContent)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraLeftBox = QFrame(self.mainContent)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.horizontalLayout_5.addWidget(self.extraLeftBox)

        self.leftMenuBg = QFrame(self.mainContent)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setStyleSheet(u"background-color: rgb(22, 24, 29);")
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u".QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);\n"
"}")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u".QPushButton {\n"
"	outline: 0;\n"
"}")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_aim = QPushButton(self.topMenu)
        self.btn_aim.setObjectName(u"btn_aim")
        sizePolicy.setHeightForWidth(self.btn_aim.sizePolicy().hasHeightForWidth())
        self.btn_aim.setSizePolicy(sizePolicy)
        self.btn_aim.setMinimumSize(QSize(0, 45))
        self.btn_aim.setFont(font)
        self.btn_aim.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_aim.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_aim.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-mouse.png);")

        self.verticalLayout_8.addWidget(self.btn_aim)

        self.btn_trigger = QPushButton(self.topMenu)
        self.btn_trigger.setObjectName(u"btn_trigger")
        self.btn_trigger.setMinimumSize(QSize(0, 45))
        self.btn_trigger.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-star.png);")

        self.verticalLayout_8.addWidget(self.btn_trigger)

        self.btn_flicksilent = QPushButton(self.topMenu)
        self.btn_flicksilent.setObjectName(u"btn_flicksilent")
        sizePolicy.setHeightForWidth(self.btn_flicksilent.sizePolicy().hasHeightForWidth())
        self.btn_flicksilent.setSizePolicy(sizePolicy)
        self.btn_flicksilent.setMinimumSize(QSize(0, 45))
        self.btn_flicksilent.setFont(font)
        self.btn_flicksilent.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_flicksilent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_flicksilent.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-ban.png);")

        self.verticalLayout_8.addWidget(self.btn_flicksilent)

        self.btn_instalock = QPushButton(self.topMenu)
        self.btn_instalock.setObjectName(u"btn_instalock")
        sizePolicy.setHeightForWidth(self.btn_instalock.sizePolicy().hasHeightForWidth())
        self.btn_instalock.setSizePolicy(sizePolicy)
        self.btn_instalock.setMinimumSize(QSize(0, 45))
        self.btn_instalock.setFont(font)
        self.btn_instalock.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_instalock.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_instalock.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-lock-unlocked.png);")

        self.verticalLayout_8.addWidget(self.btn_instalock)

        # self.btn_visual = QPushButton(self.topMenu)
        # self.btn_visual.setObjectName(u"btn_visual")
        # sizePolicy.setHeightForWidth(self.btn_visual.sizePolicy().hasHeightForWidth())
        # self.btn_visual.setSizePolicy(sizePolicy)
        # self.btn_visual.setMinimumSize(QSize(0, 45))
        # self.btn_visual.setFont(font)
        # self.btn_visual.setCursor(QCursor(Qt.PointingHandCursor))
        # self.btn_visual.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        # self.btn_visual.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-low-vision.png);")

        # self.verticalLayout_8.addWidget(self.btn_visual)

        self.btn_shortcuts = QPushButton(self.topMenu)
        self.btn_shortcuts.setObjectName(u"btn_shortcuts")
        sizePolicy.setHeightForWidth(self.btn_shortcuts.sizePolicy().hasHeightForWidth())
        self.btn_shortcuts.setSizePolicy(sizePolicy)
        self.btn_shortcuts.setMinimumSize(QSize(0, 45))
        self.btn_shortcuts.setFont(font)
        self.btn_shortcuts.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_shortcuts.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_shortcuts.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-settings.png);")

        self.verticalLayout_8.addWidget(self.btn_shortcuts)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.horizontalLayout_5.addWidget(self.leftMenuBg, 0, Qt.AlignmentFlag.AlignLeft)

        self.pagesContainer = QFrame(self.mainContent)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.aimPage = QWidget()
        self.aimPage.setObjectName(u"aimPage")
        self.horizontalLayout_4 = QHBoxLayout(self.aimPage)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.mainFrame = QFrame(self.aimPage)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setMinimumSize(QSize(632, 0))
        self.mainFrame.setMaximumSize(QSize(632, 16777215))
        self.mainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.mainFrame)
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.aimFrame = QFrame(self.mainFrame)
        self.aimFrame.setObjectName(u"aimFrame")
        self.aimFrame.setStyleSheet(u"")
        self.aimFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.aimFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.aimFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(2, 0, 0, 0)
        self.titleAim = QFrame(self.aimFrame)
        self.titleAim.setObjectName(u"titleAim")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleAim.sizePolicy().hasHeightForWidth())
        self.titleAim.setSizePolicy(sizePolicy1)
        self.titleAim.setMinimumSize(QSize(0, 0))
        self.titleAim.setStyleSheet(u"")
        self.titleAim.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleAim.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.titleAim)
        self.horizontalLayout_32.setSpacing(15)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, -1)
        self.titleAimLabel = QLabel(self.titleAim)
        self.titleAimLabel.setObjectName(u"titleAimLabel")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(15)
        font1.setWeight(QFont.ExtraBold)
        font1.setItalic(False)
        self.titleAimLabel.setFont(font1)
        self.titleAimLabel.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.titleAimLabel)

        self.configNumber = QComboBox(self.titleAim)
        self.configNumber.addItem("")
        self.configNumber.addItem("")
        self.configNumber.setObjectName(u"configNumber")
        self.configNumber.setMaximumSize(QSize(100, 25))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setWeight(QFont.DemiBold)
        font2.setItalic(False)
        self.configNumber.setFont(font2)
        self.configNumber.setStyleSheet(u"font: 600 10pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.configNumber)


        self.verticalLayout_14.addWidget(self.titleAim, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.aimOptions = QFrame(self.aimFrame)
        self.aimOptions.setObjectName(u"aimOptions")
        self.aimOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.aimOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.aimOptions)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.aimBox = QFrame(self.aimOptions)
        self.aimBox.setObjectName(u"aimBox")
        self.aimBox.setMinimumSize(QSize(300, 55))
        self.aimBox.setMaximumSize(QSize(300, 55))
        self.aimBox.setStyleSheet(u"#aimBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.aimBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.aimBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.aimBox)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.aimLabel = QLabel(self.aimBox)
        self.aimLabel.setObjectName(u"aimLabel")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setWeight(QFont.DemiBold)
        font3.setItalic(False)
        self.aimLabel.setFont(font3)
        self.aimLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_16.addWidget(self.aimLabel)

        self.aimBoxContent = QFrame(self.aimBox)
        self.aimBoxContent.setObjectName(u"aimBoxContent")
        self.aimBoxContent.setMinimumSize(QSize(150, 0))
        self.aimBoxContent.setMaximumSize(QSize(150, 16777215))
        self.aimBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.aimBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.aimBoxContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.aimKey = QComboBox(self.aimBoxContent)
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.addItem("")
        self.aimKey.setObjectName(u"aimKey")
        self.aimKey.setMinimumSize(QSize(0, 35))
        self.aimKey.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_8.addWidget(self.aimKey)


        self.horizontalLayout_16.addWidget(self.aimBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.aimBox)

        self.smoothBox = QFrame(self.aimOptions)
        self.smoothBox.setObjectName(u"smoothBox")
        self.smoothBox.setMinimumSize(QSize(300, 55))
        self.smoothBox.setMaximumSize(QSize(300, 55))
        self.smoothBox.setStyleSheet(u"#smoothBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.smoothBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.smoothBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.smoothBox)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.smoothLabel = QLabel(self.smoothBox)
        self.smoothLabel.setObjectName(u"smoothLabel")
        self.smoothLabel.setFont(font3)
        self.smoothLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_10.addWidget(self.smoothLabel)

        self.smoothBoxContent = QFrame(self.smoothBox)
        self.smoothBoxContent.setObjectName(u"smoothBoxContent")
        self.smoothBoxContent.setMinimumSize(QSize(150, 0))
        self.smoothBoxContent.setMaximumSize(QSize(150, 16777215))
        self.smoothBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.smoothBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.smoothBoxContent)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.smooth = QSlider(self.smoothBoxContent)
        self.smooth.setObjectName(u"smooth")
        self.smooth.setMinimumSize(QSize(120, 20))
        self.smooth.setMaximumSize(QSize(120, 16777215))
        self.smooth.setMinimum(10)
        self.smooth.setMaximum(40)
        self.smooth.setSingleStep(1)
        self.smooth.setPageStep(1)
        self.smooth.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_7.addWidget(self.smooth)

        self.smoothValue = QLabel(self.smoothBoxContent)
        self.smoothValue.setObjectName(u"smoothValue")

        self.horizontalLayout_7.addWidget(self.smoothValue, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_10.addWidget(self.smoothBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.smoothBox)

        self.fovBox = QFrame(self.aimOptions)
        self.fovBox.setObjectName(u"fovBox")
        self.fovBox.setMinimumSize(QSize(300, 55))
        self.fovBox.setMaximumSize(QSize(300, 55))
        self.fovBox.setStyleSheet(u"#fovBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.fovBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.fovBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.fovBox)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fovLabel = QLabel(self.fovBox)
        self.fovLabel.setObjectName(u"fovLabel")
        self.fovLabel.setFont(font3)
        self.fovLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_13.addWidget(self.fovLabel)

        self.fovBoxContent = QFrame(self.fovBox)
        self.fovBoxContent.setObjectName(u"fovBoxContent")
        self.fovBoxContent.setMinimumSize(QSize(150, 0))
        self.fovBoxContent.setMaximumSize(QSize(150, 16777215))
        self.fovBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.fovBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.fovBoxContent)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.aimFovx = QSpinBox(self.fovBoxContent)
        self.aimFovx.setObjectName(u"aimFovx")
        self.aimFovx.setMinimumSize(QSize(55, 35))
        self.aimFovx.setMaximum(200)

        self.horizontalLayout_6.addWidget(self.aimFovx)

        self.aimFovy = QSpinBox(self.fovBoxContent)
        self.aimFovy.setObjectName(u"aimFovy")
        self.aimFovy.setMinimumSize(QSize(55, 35))
        self.aimFovy.setMaximum(200)

        self.horizontalLayout_6.addWidget(self.aimFovy)


        self.horizontalLayout_13.addWidget(self.fovBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.fovBox)

        self.headBox = QFrame(self.aimOptions)
        self.headBox.setObjectName(u"headBox")
        self.headBox.setMinimumSize(QSize(300, 55))
        self.headBox.setMaximumSize(QSize(300, 55))
        self.headBox.setStyleSheet(u"#headBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.headBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.headBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.headBox)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.headLabel = QLabel(self.headBox)
        self.headLabel.setObjectName(u"headLabel")
        self.headLabel.setFont(font3)
        self.headLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_14.addWidget(self.headLabel)

        self.headBoxContent = QFrame(self.headBox)
        self.headBoxContent.setObjectName(u"headBoxContent")
        self.headBoxContent.setMinimumSize(QSize(150, 0))
        self.headBoxContent.setMaximumSize(QSize(150, 16777215))
        self.headBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.headBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.headBoxContent)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.aimHeadpos = QSlider(self.headBoxContent)
        self.aimHeadpos.setObjectName(u"aimHeadpos")
        self.aimHeadpos.setMinimumSize(QSize(120, 20))
        self.aimHeadpos.setMaximumSize(QSize(120, 16777215))
        self.aimHeadpos.setMaximum(30)
        self.aimHeadpos.setPageStep(1)
        self.aimHeadpos.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_15.addWidget(self.aimHeadpos)

        self.aimHeadposValue = QLabel(self.headBoxContent)
        self.aimHeadposValue.setObjectName(u"aimHeadposValue")

        self.horizontalLayout_15.addWidget(self.aimHeadposValue, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_14.addWidget(self.headBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_6.addWidget(self.headBox)


        self.verticalLayout_14.addWidget(self.aimOptions)


        self.horizontalLayout_17.addWidget(self.aimFrame)

        self.rcsFrame = QFrame(self.mainFrame)
        self.rcsFrame.setObjectName(u"rcsFrame")
        self.rcsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rcsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.rcsFrame)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.titleRCS = QFrame(self.rcsFrame)
        self.titleRCS.setObjectName(u"titleRCS")
        sizePolicy1.setHeightForWidth(self.titleRCS.sizePolicy().hasHeightForWidth())
        self.titleRCS.setSizePolicy(sizePolicy1)
        self.titleRCS.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleRCS.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.titleRCS)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, -1, -1)
        self.rcsTitleLabel = QLabel(self.titleRCS)
        self.rcsTitleLabel.setObjectName(u"rcsTitleLabel")
        self.rcsTitleLabel.setFont(font1)
        self.rcsTitleLabel.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.verticalLayout_28.addWidget(self.rcsTitleLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_27.addWidget(self.titleRCS, 0, Qt.AlignmentFlag.AlignTop)

        self.rcsOptions = QFrame(self.rcsFrame)
        self.rcsOptions.setObjectName(u"rcsOptions")
        self.rcsOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.rcsOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.rcsOptions)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.rcsBox = QFrame(self.rcsOptions)
        self.rcsBox.setObjectName(u"rcsBox")
        self.rcsBox.setMinimumSize(QSize(300, 55))
        self.rcsBox.setMaximumSize(QSize(300, 55))
        self.rcsBox.setStyleSheet(u"#rcsBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.rcsBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.rcsBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.rcsBox)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.rcsLabel = QLabel(self.rcsBox)
        self.rcsLabel.setObjectName(u"rcsLabel")
        self.rcsLabel.setFont(font3)
        self.rcsLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_29.addWidget(self.rcsLabel)

        self.rcsBoxContent = QFrame(self.rcsBox)
        self.rcsBoxContent.setObjectName(u"rcsBoxContent")
        self.rcsBoxContent.setMinimumSize(QSize(150, 0))
        self.rcsBoxContent.setMaximumSize(QSize(150, 16777215))
        self.rcsBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.rcsBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.rcsBoxContent)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.rcsenable = QRadioButton(self.rcsBoxContent)
        self.rcsenable.setObjectName(u"rcsenable")
        self.rcsenable.setStyleSheet(u"outline: 0;")

        self.horizontalLayout_30.addWidget(self.rcsenable)


        self.horizontalLayout_29.addWidget(self.rcsBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.rcsBox, 0, Qt.AlignmentFlag.AlignTop)

        self.downSpeedBox = QFrame(self.rcsOptions)
        self.downSpeedBox.setObjectName(u"downSpeedBox")
        self.downSpeedBox.setMinimumSize(QSize(300, 55))
        self.downSpeedBox.setMaximumSize(QSize(300, 55))
        self.downSpeedBox.setStyleSheet(u"#downSpeedBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.downSpeedBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.downSpeedBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.downSpeedBox)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.downSpeedLabel = QLabel(self.downSpeedBox)
        self.downSpeedLabel.setObjectName(u"downSpeedLabel")
        self.downSpeedLabel.setFont(font3)
        self.downSpeedLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_25.addWidget(self.downSpeedLabel)

        self.downSpeedBoxContent = QFrame(self.downSpeedBox)
        self.downSpeedBoxContent.setObjectName(u"downSpeedBoxContent")
        self.downSpeedBoxContent.setMinimumSize(QSize(150, 0))
        self.downSpeedBoxContent.setMaximumSize(QSize(150, 16777215))
        self.downSpeedBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.downSpeedBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.downSpeedBoxContent)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.downspeed = QSlider(self.downSpeedBoxContent)
        self.downspeed.setObjectName(u"downspeed")
        self.downspeed.setMinimumSize(QSize(120, 20))
        self.downspeed.setMaximumSize(QSize(120, 16777215))
        self.downspeed.setMinimum(10)
        self.downspeed.setMaximum(60)
        self.downspeed.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_26.addWidget(self.downspeed)

        self.downspeedValue = QLabel(self.downSpeedBoxContent)
        self.downspeedValue.setObjectName(u"downspeedValue")

        self.horizontalLayout_26.addWidget(self.downspeedValue, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_25.addWidget(self.downSpeedBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.downSpeedBox)

        self.downLimitBox = QFrame(self.rcsOptions)
        self.downLimitBox.setObjectName(u"downLimitBox")
        self.downLimitBox.setMinimumSize(QSize(300, 55))
        self.downLimitBox.setMaximumSize(QSize(300, 55))
        self.downLimitBox.setStyleSheet(u"#downLimitBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.downLimitBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.downLimitBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.downLimitBox)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.downLimitLabel = QLabel(self.downLimitBox)
        self.downLimitLabel.setObjectName(u"downLimitLabel")
        self.downLimitLabel.setFont(font3)
        self.downLimitLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_27.addWidget(self.downLimitLabel)

        self.downLimitBoxContent = QFrame(self.downLimitBox)
        self.downLimitBoxContent.setObjectName(u"downLimitBoxContent")
        self.downLimitBoxContent.setMinimumSize(QSize(150, 0))
        self.downLimitBoxContent.setMaximumSize(QSize(150, 16777215))
        self.downLimitBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.downLimitBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.downLimitBoxContent)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.downlimit = QSlider(self.downLimitBoxContent)
        self.downlimit.setObjectName(u"downlimit")
        self.downlimit.setMinimumSize(QSize(120, 20))
        self.downlimit.setMaximumSize(QSize(120, 16777215))
        self.downlimit.setMinimum(40)
        self.downlimit.setMaximum(200)
        self.downlimit.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_28.addWidget(self.downlimit)

        self.downlimitValue = QLabel(self.downLimitBoxContent)
        self.downlimitValue.setObjectName(u"downlimitValue")

        self.horizontalLayout_28.addWidget(self.downlimitValue, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_27.addWidget(self.downLimitBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.downLimitBox)


        self.verticalLayout_27.addWidget(self.rcsOptions, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_17.addWidget(self.rcsFrame, 0, Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_4.addWidget(self.mainFrame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.aimPage)
        self.example = QWidget()
        self.example.setObjectName(u"example")
        self.example.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.example)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.example)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.example)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon3)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.example)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.example)
        self.triggerPage = QWidget()
        self.triggerPage.setObjectName(u"triggerPage")
        self.verticalLayout_32 = QVBoxLayout(self.triggerPage)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, -1, 0)
        self.triggerMainFrame = QFrame(self.triggerPage)
        self.triggerMainFrame.setObjectName(u"triggerMainFrame")
        self.triggerMainFrame.setStyleSheet(u"")
        self.triggerMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.triggerMainFrame)
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.triggerFrame = QFrame(self.triggerMainFrame)
        self.triggerFrame.setObjectName(u"triggerFrame")
        self.triggerFrame.setStyleSheet(u"")
        self.triggerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.triggerFrame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(2, 0, 0, 0)
        self.titleTrigger = QFrame(self.triggerFrame)
        self.titleTrigger.setObjectName(u"titleTrigger")
        sizePolicy1.setHeightForWidth(self.titleTrigger.sizePolicy().hasHeightForWidth())
        self.titleTrigger.setSizePolicy(sizePolicy1)
        self.titleTrigger.setMinimumSize(QSize(0, 0))
        self.titleTrigger.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.titleTrigger.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleTrigger.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.titleTrigger)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, -1, -1)
        self.titleTriggerLabel = QLabel(self.titleTrigger)
        self.titleTriggerLabel.setObjectName(u"titleTriggerLabel")
        self.titleTriggerLabel.setFont(font1)
        self.titleTriggerLabel.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.verticalLayout_22.addWidget(self.titleTriggerLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_20.addWidget(self.titleTrigger, 0, Qt.AlignmentFlag.AlignTop)

        self.triggerOptions = QFrame(self.triggerFrame)
        self.triggerOptions.setObjectName(u"triggerOptions")
        self.triggerOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.triggerOptions)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.triggerBox = QFrame(self.triggerOptions)
        self.triggerBox.setObjectName(u"triggerBox")
        self.triggerBox.setMinimumSize(QSize(300, 55))
        self.triggerBox.setMaximumSize(QSize(300, 55))
        self.triggerBox.setStyleSheet(u"#triggerBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.triggerBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.triggerBox)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.triggerLabel = QLabel(self.triggerBox)
        self.triggerLabel.setObjectName(u"triggerLabel")
        self.triggerLabel.setFont(font3)
        self.triggerLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_19.addWidget(self.triggerLabel)

        self.triggerBoxContent = QFrame(self.triggerBox)
        self.triggerBoxContent.setObjectName(u"triggerBoxContent")
        self.triggerBoxContent.setMinimumSize(QSize(150, 0))
        self.triggerBoxContent.setMaximumSize(QSize(150, 16777215))
        self.triggerBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.triggerBoxContent)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.triggerKey = QComboBox(self.triggerBoxContent)
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.addItem("")
        self.triggerKey.setObjectName(u"triggerKey")
        self.triggerKey.setMinimumSize(QSize(0, 35))
        self.triggerKey.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_20.addWidget(self.triggerKey)


        self.horizontalLayout_19.addWidget(self.triggerBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_23.addWidget(self.triggerBox)

        self.triggerFovBox = QFrame(self.triggerOptions)
        self.triggerFovBox.setObjectName(u"triggerFovBox")
        self.triggerFovBox.setMinimumSize(QSize(300, 55))
        self.triggerFovBox.setMaximumSize(QSize(300, 55))
        self.triggerFovBox.setStyleSheet(u"#triggerFovBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.triggerFovBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerFovBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.triggerFovBox)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.triggerFovLabel = QLabel(self.triggerFovBox)
        self.triggerFovLabel.setObjectName(u"triggerFovLabel")
        self.triggerFovLabel.setFont(font3)
        self.triggerFovLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_23.addWidget(self.triggerFovLabel)

        self.triggerFovBoxContent = QFrame(self.triggerFovBox)
        self.triggerFovBoxContent.setObjectName(u"triggerFovBoxContent")
        self.triggerFovBoxContent.setMinimumSize(QSize(150, 0))
        self.triggerFovBoxContent.setMaximumSize(QSize(150, 16777215))
        self.triggerFovBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerFovBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.triggerFovBoxContent)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.triggerFovx = QSpinBox(self.triggerFovBoxContent)
        self.triggerFovx.setObjectName(u"triggerFovx")
        self.triggerFovx.setMinimumSize(QSize(55, 35))
        self.triggerFovx.setMaximum(8)

        self.horizontalLayout_24.addWidget(self.triggerFovx)

        self.triggerFovy = QSpinBox(self.triggerFovBoxContent)
        self.triggerFovy.setObjectName(u"triggerFovy")
        self.triggerFovy.setMinimumSize(QSize(55, 35))
        self.triggerFovy.setMaximum(8)

        self.horizontalLayout_24.addWidget(self.triggerFovy)


        self.horizontalLayout_23.addWidget(self.triggerFovBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_23.addWidget(self.triggerFovBox)

        self.triggerShootDelayBox = QFrame(self.triggerOptions)
        self.triggerShootDelayBox.setObjectName(u"triggerShootDelayBox")
        self.triggerShootDelayBox.setMinimumSize(QSize(300, 55))
        self.triggerShootDelayBox.setMaximumSize(QSize(300, 55))
        self.triggerShootDelayBox.setStyleSheet(u"#triggerShootDelayBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.triggerShootDelayBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerShootDelayBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.triggerShootDelayBox)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.triggerShootDelayLabel = QLabel(self.triggerShootDelayBox)
        self.triggerShootDelayLabel.setObjectName(u"triggerShootDelayLabel")
        self.triggerShootDelayLabel.setFont(font3)
        self.triggerShootDelayLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_47.addWidget(self.triggerShootDelayLabel)

        self.triggerShootDelayBoxContent = QFrame(self.triggerShootDelayBox)
        self.triggerShootDelayBoxContent.setObjectName(u"triggerShootDelayBoxContent")
        self.triggerShootDelayBoxContent.setMinimumSize(QSize(150, 0))
        self.triggerShootDelayBoxContent.setMaximumSize(QSize(150, 16777215))
        self.triggerShootDelayBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerShootDelayBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.triggerShootDelayBoxContent)
        self.horizontalLayout_48.setSpacing(10)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.triggerShootdelay = QSlider(self.triggerShootDelayBoxContent)
        self.triggerShootdelay.setObjectName(u"triggerShootdelay")
        self.triggerShootdelay.setMinimumSize(QSize(120, 20))
        self.triggerShootdelay.setMaximumSize(QSize(120, 16777215))
        self.triggerShootdelay.setMinimum(1)
        self.triggerShootdelay.setMaximum(3)
        self.triggerShootdelay.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_48.addWidget(self.triggerShootdelay)

        self.triggerShootdelayValue = QLabel(self.triggerShootDelayBoxContent)
        self.triggerShootdelayValue.setObjectName(u"triggerShootdelayValue")

        self.horizontalLayout_48.addWidget(self.triggerShootdelayValue, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_47.addWidget(self.triggerShootDelayBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_23.addWidget(self.triggerShootDelayBox)

        self.triggerModeFrame = QFrame(self.triggerOptions)
        self.triggerModeFrame.setObjectName(u"triggerModeFrame")
        self.triggerModeFrame.setMinimumSize(QSize(300, 55))
        self.triggerModeFrame.setMaximumSize(QSize(300, 55))
        self.triggerModeFrame.setStyleSheet(u"#triggerModeFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.triggerModeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerModeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.triggerModeFrame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.triggerModeLabel = QLabel(self.triggerModeFrame)
        self.triggerModeLabel.setObjectName(u"triggerModeLabel")
        self.triggerModeLabel.setFont(font3)
        self.triggerModeLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_21.addWidget(self.triggerModeLabel)

        self.triggerModeContent = QFrame(self.triggerModeFrame)
        self.triggerModeContent.setObjectName(u"triggerModeContent")
        self.triggerModeContent.setMinimumSize(QSize(150, 0))
        self.triggerModeContent.setMaximumSize(QSize(150, 16777215))
        self.triggerModeContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.triggerModeContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.triggerModeContent)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.triggerMode = QComboBox(self.triggerModeContent)
        self.triggerMode.addItem("")
        self.triggerMode.addItem("")
        self.triggerMode.setObjectName(u"triggerMode")
        self.triggerMode.setMinimumSize(QSize(0, 35))
        self.triggerMode.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_22.addWidget(self.triggerMode)


        self.horizontalLayout_21.addWidget(self.triggerModeContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_23.addWidget(self.triggerModeFrame)


        self.verticalLayout_20.addWidget(self.triggerOptions, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_18.addWidget(self.triggerFrame, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_32.addWidget(self.triggerMainFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.triggerPage)
        self.flicksilentPage = QWidget()
        self.flicksilentPage.setObjectName(u"flicksilentPage")
        self.verticalLayout_36 = QVBoxLayout(self.flicksilentPage)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, -1, 0)
        self.flicksilentMainFrame = QFrame(self.flicksilentPage)
        self.flicksilentMainFrame.setObjectName(u"flicksilentMainFrame")
        self.flicksilentMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.flicksilentMainFrame)
        self.horizontalLayout_39.setSpacing(20)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.flicksilentFrame = QFrame(self.flicksilentMainFrame)
        self.flicksilentFrame.setObjectName(u"flicksilentFrame")
        self.flicksilentFrame.setStyleSheet(u"")
        self.flicksilentFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.flicksilentFrame)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(2, 0, 0, 0)
        self.titleFlicksilent = QFrame(self.flicksilentFrame)
        self.titleFlicksilent.setObjectName(u"titleFlicksilent")
        sizePolicy1.setHeightForWidth(self.titleFlicksilent.sizePolicy().hasHeightForWidth())
        self.titleFlicksilent.setSizePolicy(sizePolicy1)
        self.titleFlicksilent.setMinimumSize(QSize(0, 0))
        self.titleFlicksilent.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.titleFlicksilent.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleFlicksilent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.titleFlicksilent)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, -1, -1)
        self.titletitleFlicksilentLabel = QLabel(self.titleFlicksilent)
        self.titletitleFlicksilentLabel.setObjectName(u"titletitleFlicksilentLabel")
        self.titletitleFlicksilentLabel.setFont(font1)
        self.titletitleFlicksilentLabel.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.verticalLayout_30.addWidget(self.titletitleFlicksilentLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_29.addWidget(self.titleFlicksilent, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.flicksilentOptions = QFrame(self.flicksilentFrame)
        self.flicksilentOptions.setObjectName(u"flicksilentOptions")
        self.flicksilentOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.flicksilentOptions)
        self.verticalLayout_31.setSpacing(10)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.flicksilentBox = QFrame(self.flicksilentOptions)
        self.flicksilentBox.setObjectName(u"flicksilentBox")
        self.flicksilentBox.setMinimumSize(QSize(300, 55))
        self.flicksilentBox.setMaximumSize(QSize(300, 55))
        self.flicksilentBox.setStyleSheet(u"#flicksilentBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.flicksilentBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.flicksilentBox)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.flicksilentLabel = QLabel(self.flicksilentBox)
        self.flicksilentLabel.setObjectName(u"flicksilentLabel")
        self.flicksilentLabel.setFont(font3)
        self.flicksilentLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_40.addWidget(self.flicksilentLabel)

        self.flicksilentBoxContent = QFrame(self.flicksilentBox)
        self.flicksilentBoxContent.setObjectName(u"flicksilentBoxContent")
        self.flicksilentBoxContent.setMinimumSize(QSize(150, 0))
        self.flicksilentBoxContent.setMaximumSize(QSize(150, 16777215))
        self.flicksilentBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.flicksilentBoxContent)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.flicksilentKey = QComboBox(self.flicksilentBoxContent)
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.addItem("")
        self.flicksilentKey.setObjectName(u"flicksilentKey")
        self.flicksilentKey.setMinimumSize(QSize(0, 35))
        self.flicksilentKey.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_41.addWidget(self.flicksilentKey)


        self.horizontalLayout_40.addWidget(self.flicksilentBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_31.addWidget(self.flicksilentBox)

        self.flicksilentModeFrame = QFrame(self.flicksilentOptions)
        self.flicksilentModeFrame.setObjectName(u"flicksilentModeFrame")
        self.flicksilentModeFrame.setMinimumSize(QSize(300, 55))
        self.flicksilentModeFrame.setMaximumSize(QSize(300, 55))
        self.flicksilentModeFrame.setStyleSheet(u"#flicksilentModeFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.flicksilentModeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentModeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.flicksilentModeFrame)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.flicksilentModeLabel = QLabel(self.flicksilentModeFrame)
        self.flicksilentModeLabel.setObjectName(u"flicksilentModeLabel")
        self.flicksilentModeLabel.setFont(font3)
        self.flicksilentModeLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_42.addWidget(self.flicksilentModeLabel)

        self.flicksilentModeContent = QFrame(self.flicksilentModeFrame)
        self.flicksilentModeContent.setObjectName(u"flicksilentModeContent")
        self.flicksilentModeContent.setMinimumSize(QSize(150, 0))
        self.flicksilentModeContent.setMaximumSize(QSize(150, 16777215))
        self.flicksilentModeContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentModeContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.flicksilentModeContent)
        self.horizontalLayout_43.setSpacing(10)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.flicksilentMode = QComboBox(self.flicksilentModeContent)
        self.flicksilentMode.addItem("")
        self.flicksilentMode.addItem("")
        self.flicksilentMode.setObjectName(u"flicksilentMode")
        self.flicksilentMode.setMinimumSize(QSize(0, 35))
        self.flicksilentMode.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_43.addWidget(self.flicksilentMode)


        self.horizontalLayout_42.addWidget(self.flicksilentModeContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_31.addWidget(self.flicksilentModeFrame)

        self.flicksilentfovBox = QFrame(self.flicksilentOptions)
        self.flicksilentfovBox.setObjectName(u"flicksilentfovBox")
        self.flicksilentfovBox.setMinimumSize(QSize(300, 55))
        self.flicksilentfovBox.setMaximumSize(QSize(300, 55))
        self.flicksilentfovBox.setStyleSheet(u"#flicksilentfovBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.flicksilentfovBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentfovBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.flicksilentfovBox)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.flicksilentFovLabel = QLabel(self.flicksilentfovBox)
        self.flicksilentFovLabel.setObjectName(u"flicksilentFovLabel")
        self.flicksilentFovLabel.setFont(font3)
        self.flicksilentFovLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.flicksilentFovLabel)

        self.flicksilentfovBoxContent = QFrame(self.flicksilentfovBox)
        self.flicksilentfovBoxContent.setObjectName(u"flicksilentfovBoxContent")
        self.flicksilentfovBoxContent.setMinimumSize(QSize(150, 0))
        self.flicksilentfovBoxContent.setMaximumSize(QSize(150, 16777215))
        self.flicksilentfovBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentfovBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.flicksilentfovBoxContent)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.flicksilentFovx = QSpinBox(self.flicksilentfovBoxContent)
        self.flicksilentFovx.setObjectName(u"flicksilentFovx")
        self.flicksilentFovx.setMinimumSize(QSize(55, 35))
        self.flicksilentFovx.setMaximum(200)

        self.horizontalLayout_45.addWidget(self.flicksilentFovx)

        self.flicksilentFovy = QSpinBox(self.flicksilentfovBoxContent)
        self.flicksilentFovy.setObjectName(u"flicksilentFovy")
        self.flicksilentFovy.setMinimumSize(QSize(55, 35))
        self.flicksilentFovy.setMaximum(200)

        self.horizontalLayout_45.addWidget(self.flicksilentFovy)


        self.horizontalLayout_44.addWidget(self.flicksilentfovBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_31.addWidget(self.flicksilentfovBox)

        self.flicksilentHeadBox = QFrame(self.flicksilentOptions)
        self.flicksilentHeadBox.setObjectName(u"flicksilentHeadBox")
        self.flicksilentHeadBox.setMinimumSize(QSize(300, 55))
        self.flicksilentHeadBox.setMaximumSize(QSize(300, 55))
        self.flicksilentHeadBox.setStyleSheet(u"#flicksilentHeadBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.flicksilentHeadBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentHeadBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.flicksilentHeadBox)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.flicksilentHeadPosLabel = QLabel(self.flicksilentHeadBox)
        self.flicksilentHeadPosLabel.setObjectName(u"flicksilentHeadPosLabel")
        self.flicksilentHeadPosLabel.setFont(font3)
        self.flicksilentHeadPosLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_46.addWidget(self.flicksilentHeadPosLabel)

        self.flicksilentHeadBoxContent = QFrame(self.flicksilentHeadBox)
        self.flicksilentHeadBoxContent.setObjectName(u"flicksilentHeadBoxContent")
        self.flicksilentHeadBoxContent.setMinimumSize(QSize(150, 0))
        self.flicksilentHeadBoxContent.setMaximumSize(QSize(150, 16777215))
        self.flicksilentHeadBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentHeadBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.flicksilentHeadBoxContent)
        self.horizontalLayout_49.setSpacing(10)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.flicksilentHeadpos = QSlider(self.flicksilentHeadBoxContent)
        self.flicksilentHeadpos.setObjectName(u"flicksilentHeadpos")
        self.flicksilentHeadpos.setMinimumSize(QSize(120, 20))
        self.flicksilentHeadpos.setMaximumSize(QSize(120, 16777215))
        self.flicksilentHeadpos.setMaximum(30)
        self.flicksilentHeadpos.setPageStep(1)
        self.flicksilentHeadpos.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_49.addWidget(self.flicksilentHeadpos)

        self.flicksilentHeadposValue = QLabel(self.flicksilentHeadBoxContent)
        self.flicksilentHeadposValue.setObjectName(u"flicksilentHeadposValue")

        self.horizontalLayout_49.addWidget(self.flicksilentHeadposValue, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_46.addWidget(self.flicksilentHeadBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_31.addWidget(self.flicksilentHeadBox)


        self.verticalLayout_29.addWidget(self.flicksilentOptions, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_39.addWidget(self.flicksilentFrame, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_36.addWidget(self.flicksilentMainFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.stackedWidget.addWidget(self.flicksilentPage)
        self.configsPage = QWidget()
        self.configsPage.setObjectName(u"configsPage")
        self.verticalLayout_41 = QVBoxLayout(self.configsPage)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, -1, -1)
        self.shortcutsMainFrame = QFrame(self.configsPage)
        self.shortcutsMainFrame.setObjectName(u"shortcutsMainFrame")
        self.shortcutsMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.shortcutsMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.shortcutsMainFrame)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.shortcutsFrame = QFrame(self.shortcutsMainFrame)
        self.shortcutsFrame.setObjectName(u"shortcutsFrame")
        self.shortcutsFrame.setStyleSheet(u"")
        self.shortcutsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.shortcutsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.shortcutsFrame)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(2, 0, 0, 0)
        self.tittleShortcuts = QFrame(self.shortcutsFrame)
        self.tittleShortcuts.setObjectName(u"tittleShortcuts")
        sizePolicy1.setHeightForWidth(self.tittleShortcuts.sizePolicy().hasHeightForWidth())
        self.tittleShortcuts.setSizePolicy(sizePolicy1)
        self.tittleShortcuts.setMinimumSize(QSize(0, 0))
        self.tittleShortcuts.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.tittleShortcuts.setFrameShape(QFrame.Shape.StyledPanel)
        self.tittleShortcuts.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.tittleShortcuts)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, -1, -1)
        self.tittleShortcutsLabel = QLabel(self.tittleShortcuts)
        self.tittleShortcutsLabel.setObjectName(u"tittleShortcutsLabel")
        self.tittleShortcutsLabel.setFont(font1)
        self.tittleShortcutsLabel.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.verticalLayout_39.addWidget(self.tittleShortcutsLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_38.addWidget(self.tittleShortcuts, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.shortcutsOptions = QFrame(self.shortcutsFrame)
        self.shortcutsOptions.setObjectName(u"shortcutsOptions")
        self.shortcutsOptions.setMinimumSize(QSize(0, 317))
        self.shortcutsOptions.setMaximumSize(QSize(16777215, 317))
        self.shortcutsOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.shortcutsOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.shortcutsOptions)
        self.verticalLayout_40.setSpacing(10)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.streamProofBox = QFrame(self.shortcutsOptions)
        self.streamProofBox.setObjectName(u"streamProofBox")
        self.streamProofBox.setMinimumSize(QSize(300, 55))
        self.streamProofBox.setMaximumSize(QSize(300, 55))
        self.streamProofBox.setStyleSheet(u"#streamProofBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.streamProofBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.streamProofBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.streamProofBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.streamProofLabel = QLabel(self.streamProofBox)
        self.streamProofLabel.setObjectName(u"streamProofLabel")
        self.streamProofLabel.setFont(font3)
        self.streamProofLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.streamProofLabel)

        self.streamProofBoxContent = QFrame(self.streamProofBox)
        self.streamProofBoxContent.setObjectName(u"streamProofBoxContent")
        self.streamProofBoxContent.setMinimumSize(QSize(150, 0))
        self.streamProofBoxContent.setMaximumSize(QSize(150, 16777215))
        self.streamProofBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.streamProofBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.streamProofBoxContent)
        self.horizontalLayout_62.setSpacing(10)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.streamproof = QRadioButton(self.streamProofBoxContent)
        self.streamproof.setObjectName(u"streamproof")
        self.streamproof.setStyleSheet(u"outline: 0;")

        self.horizontalLayout_62.addWidget(self.streamproof)


        self.horizontalLayout_2.addWidget(self.streamProofBoxContent)


        self.verticalLayout_40.addWidget(self.streamProofBox)

        self.switchConfig1Box = QFrame(self.shortcutsOptions)
        self.switchConfig1Box.setObjectName(u"switchConfig1Box")
        self.switchConfig1Box.setMinimumSize(QSize(300, 55))
        self.switchConfig1Box.setMaximumSize(QSize(300, 55))
        self.switchConfig1Box.setStyleSheet(u"#switchConfig1Box{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.switchConfig1Box.setFrameShape(QFrame.Shape.StyledPanel)
        self.switchConfig1Box.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.switchConfig1Box)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.switchConfig1Label = QLabel(self.switchConfig1Box)
        self.switchConfig1Label.setObjectName(u"switchConfig1Label")
        self.switchConfig1Label.setFont(font3)
        self.switchConfig1Label.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_56.addWidget(self.switchConfig1Label)

        self.switchConfig1BoxContent = QFrame(self.switchConfig1Box)
        self.switchConfig1BoxContent.setObjectName(u"switchConfig1BoxContent")
        self.switchConfig1BoxContent.setMinimumSize(QSize(150, 0))
        self.switchConfig1BoxContent.setMaximumSize(QSize(150, 16777215))
        self.switchConfig1BoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.switchConfig1BoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.switchConfig1BoxContent)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.switchconfig1 = QComboBox(self.switchConfig1BoxContent)
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.addItem("")
        self.switchconfig1.setObjectName(u"switchconfig1")
        self.switchconfig1.setMinimumSize(QSize(0, 35))
        self.switchconfig1.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_57.addWidget(self.switchconfig1)


        self.horizontalLayout_56.addWidget(self.switchConfig1BoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_40.addWidget(self.switchConfig1Box)

        self.switchConfig2Box = QFrame(self.shortcutsOptions)
        self.switchConfig2Box.setObjectName(u"switchConfig2Box")
        self.switchConfig2Box.setMinimumSize(QSize(300, 55))
        self.switchConfig2Box.setMaximumSize(QSize(300, 55))
        self.switchConfig2Box.setStyleSheet(u"#switchConfig2Box{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.switchConfig2Box.setFrameShape(QFrame.Shape.StyledPanel)
        self.switchConfig2Box.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.switchConfig2Box)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.switchConfig2Label = QLabel(self.switchConfig2Box)
        self.switchConfig2Label.setObjectName(u"switchConfig2Label")
        self.switchConfig2Label.setFont(font3)
        self.switchConfig2Label.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_64.addWidget(self.switchConfig2Label)

        self.switchConfig2BoxContent = QFrame(self.switchConfig2Box)
        self.switchConfig2BoxContent.setObjectName(u"switchConfig2BoxContent")
        self.switchConfig2BoxContent.setMinimumSize(QSize(150, 0))
        self.switchConfig2BoxContent.setMaximumSize(QSize(150, 16777215))
        self.switchConfig2BoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.switchConfig2BoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.switchConfig2BoxContent)
        self.horizontalLayout_65.setSpacing(10)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.switchconfig2 = QComboBox(self.switchConfig2BoxContent)
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.addItem("")
        self.switchconfig2.setObjectName(u"switchconfig2")
        self.switchconfig2.setMinimumSize(QSize(0, 35))
        self.switchconfig2.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_65.addWidget(self.switchconfig2)


        self.horizontalLayout_64.addWidget(self.switchConfig2BoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_40.addWidget(self.switchConfig2Box)

        self.spinbotBox = QFrame(self.shortcutsOptions)
        self.spinbotBox.setObjectName(u"spinbotBox")
        self.spinbotBox.setMinimumSize(QSize(300, 55))
        self.spinbotBox.setMaximumSize(QSize(300, 55))
        self.spinbotBox.setStyleSheet(u"#spinbotBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.spinbotBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.spinbotBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.spinbotBox)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.spinbotLabel = QLabel(self.spinbotBox)
        self.spinbotLabel.setObjectName(u"spinbotLabel")
        self.spinbotLabel.setFont(font3)
        self.spinbotLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.spinbotLabel)

        self.spinbotBoxContent = QFrame(self.spinbotBox)
        self.spinbotBoxContent.setObjectName(u"spinbotBoxContent")
        self.spinbotBoxContent.setMinimumSize(QSize(150, 0))
        self.spinbotBoxContent.setMaximumSize(QSize(150, 16777215))
        self.spinbotBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.spinbotBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.spinbotBoxContent)
        self.horizontalLayout_59.setSpacing(10)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.spinbot = QComboBox(self.spinbotBoxContent)
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.addItem("")
        self.spinbot.setObjectName(u"spinbot")
        self.spinbot.setMinimumSize(QSize(0, 35))
        self.spinbot.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_59.addWidget(self.spinbot)


        self.horizontalLayout_58.addWidget(self.spinbotBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_40.addWidget(self.spinbotBox)

        self.disableRcsBox = QFrame(self.shortcutsOptions)
        self.disableRcsBox.setObjectName(u"disableRcsBox")
        self.disableRcsBox.setMinimumSize(QSize(300, 55))
        self.disableRcsBox.setMaximumSize(QSize(300, 55))
        self.disableRcsBox.setStyleSheet(u"#disableRcsBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.disableRcsBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.disableRcsBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.disableRcsBox)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.disableRcsLabel = QLabel(self.disableRcsBox)
        self.disableRcsLabel.setObjectName(u"disableRcsLabel")
        self.disableRcsLabel.setFont(font3)
        self.disableRcsLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_60.addWidget(self.disableRcsLabel)

        self.disableRcsBoxContent = QFrame(self.disableRcsBox)
        self.disableRcsBoxContent.setObjectName(u"disableRcsBoxContent")
        self.disableRcsBoxContent.setMinimumSize(QSize(150, 0))
        self.disableRcsBoxContent.setMaximumSize(QSize(150, 16777215))
        self.disableRcsBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.disableRcsBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.disableRcsBoxContent)
        self.horizontalLayout_61.setSpacing(10)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.disablercs = QComboBox(self.disableRcsBoxContent)
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.addItem("")
        self.disablercs.setObjectName(u"disablercs")
        self.disablercs.setMinimumSize(QSize(0, 35))
        self.disablercs.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_61.addWidget(self.disablercs)


        self.horizontalLayout_60.addWidget(self.disableRcsBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_40.addWidget(self.disableRcsBox)


        self.verticalLayout_38.addWidget(self.shortcutsOptions, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_35.addWidget(self.shortcutsFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.configFrame = QFrame(self.shortcutsMainFrame)
        self.configFrame.setObjectName(u"configFrame")
        self.configFrame.setStyleSheet(u"")
        self.configFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.configFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.configFrame)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(2, 0, 0, 0)
        self.tittleConfigs = QFrame(self.configFrame)
        self.tittleConfigs.setObjectName(u"tittleConfigs")
        sizePolicy1.setHeightForWidth(self.tittleConfigs.sizePolicy().hasHeightForWidth())
        self.tittleConfigs.setSizePolicy(sizePolicy1)
        self.tittleConfigs.setMinimumSize(QSize(0, 0))
        self.tittleConfigs.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.tittleConfigs.setFrameShape(QFrame.Shape.StyledPanel)
        self.tittleConfigs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.tittleConfigs)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, -1, -1)
        self.tittleConfigsLabel = QLabel(self.tittleConfigs)
        self.tittleConfigsLabel.setObjectName(u"tittleConfigsLabel")
        self.tittleConfigsLabel.setFont(font1)
        self.tittleConfigsLabel.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.verticalLayout_46.addWidget(self.tittleConfigsLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_45.addWidget(self.tittleConfigs, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.configFrameOptions = QFrame(self.configFrame)
        self.configFrameOptions.setObjectName(u"configFrameOptions")
        self.configFrameOptions.setMinimumSize(QSize(0, 317))
        self.configFrameOptions.setMaximumSize(QSize(16777215, 317))
        self.configFrameOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.configFrameOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.configFrameOptions)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.colorFrame = QFrame(self.configFrameOptions)
        self.colorFrame.setObjectName(u"colorFrame")
        self.colorFrame.setMinimumSize(QSize(300, 55))
        self.colorFrame.setMaximumSize(QSize(300, 55))
        self.colorFrame.setStyleSheet(u"#colorFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.colorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.colorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.colorFrame)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.colorLabel = QLabel(self.colorFrame)
        self.colorLabel.setObjectName(u"colorLabel")
        self.colorLabel.setFont(font3)
        self.colorLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_75.addWidget(self.colorLabel)

        self.colorFrameBox = QFrame(self.colorFrame)
        self.colorFrameBox.setObjectName(u"colorFrameBox")
        self.colorFrameBox.setMinimumSize(QSize(150, 0))
        self.colorFrameBox.setMaximumSize(QSize(150, 16777215))
        self.colorFrameBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.colorFrameBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.colorFrameBox)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.color = QComboBox(self.colorFrameBox)
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.setObjectName(u"color")
        self.color.setEnabled(True)
        self.color.setMinimumSize(QSize(0, 35))
        self.color.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_76.addWidget(self.color)


        self.horizontalLayout_75.addWidget(self.colorFrameBox, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_4.addWidget(self.colorFrame)

        self.mouseFrame = QFrame(self.configFrameOptions)
        self.mouseFrame.setObjectName(u"mouseFrame")
        self.mouseFrame.setMinimumSize(QSize(300, 55))
        self.mouseFrame.setMaximumSize(QSize(300, 55))
        self.mouseFrame.setStyleSheet(u"#mouseFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.mouseFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mouseFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.mouseFrame)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.mouseLabel = QLabel(self.mouseFrame)
        self.mouseLabel.setObjectName(u"mouseLabel")
        self.mouseLabel.setFont(font3)
        self.mouseLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_79.addWidget(self.mouseLabel)

        self.mouseFrameBox = QFrame(self.mouseFrame)
        self.mouseFrameBox.setObjectName(u"mouseFrameBox")
        self.mouseFrameBox.setMinimumSize(QSize(150, 0))
        self.mouseFrameBox.setMaximumSize(QSize(150, 16777215))
        self.mouseFrameBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.mouseFrameBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.mouseFrameBox)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.mousesens = QDoubleSpinBox(self.mouseFrameBox)
        self.mousesens.setObjectName(u"mousesens")
        self.mousesens.setMinimumSize(QSize(0, 35))
        self.mousesens.setMaximumSize(QSize(16777215, 35))
        self.mousesens.setSingleStep(0.010000000000000)

        self.horizontalLayout_80.addWidget(self.mousesens)


        self.horizontalLayout_79.addWidget(self.mouseFrameBox, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_4.addWidget(self.mouseFrame)

        self.frame = QFrame(self.configFrameOptions)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_45.addWidget(self.configFrameOptions, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_35.addWidget(self.configFrame, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_41.addWidget(self.shortcutsMainFrame)

        self.stackedWidget.addWidget(self.configsPage)
        self.visualPage = QWidget()
        self.visualPage.setObjectName(u"visualPage")
        self.verticalLayout_26 = QVBoxLayout(self.visualPage)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, -1, -1)
        self.shortcutsMainFrame_3 = QFrame(self.visualPage)
        self.shortcutsMainFrame_3.setObjectName(u"shortcutsMainFrame_3")
        self.shortcutsMainFrame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.shortcutsMainFrame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.shortcutsMainFrame_3)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.configFrame_5 = QFrame(self.shortcutsMainFrame_3)
        self.configFrame_5.setObjectName(u"configFrame_5")
        self.configFrame_5.setStyleSheet(u"")
        self.configFrame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.configFrame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.configFrame_5)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(2, 0, 0, 0)
        self.tittleConfigs_5 = QFrame(self.configFrame_5)
        self.tittleConfigs_5.setObjectName(u"tittleConfigs_5")
        sizePolicy1.setHeightForWidth(self.tittleConfigs_5.sizePolicy().hasHeightForWidth())
        self.tittleConfigs_5.setSizePolicy(sizePolicy1)
        self.tittleConfigs_5.setMinimumSize(QSize(0, 0))
        self.tittleConfigs_5.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.tittleConfigs_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.tittleConfigs_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.tittleConfigs_5)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, -1, -1)
        self.tittleConfigsLabel_5 = QLabel(self.tittleConfigs_5)
        self.tittleConfigsLabel_5.setObjectName(u"tittleConfigsLabel_5")
        self.tittleConfigsLabel_5.setFont(font1)
        self.tittleConfigsLabel_5.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.verticalLayout_57.addWidget(self.tittleConfigsLabel_5, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_56.addWidget(self.tittleConfigs_5, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.configFrameOptions_5 = QFrame(self.configFrame_5)
        self.configFrameOptions_5.setObjectName(u"configFrameOptions_5")
        self.configFrameOptions_5.setMinimumSize(QSize(0, 317))
        self.configFrameOptions_5.setMaximumSize(QSize(16777215, 317))
        self.configFrameOptions_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.configFrameOptions_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.configFrameOptions_5)
        self.verticalLayout_58.setSpacing(10)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.flicksilentHeadBox_4 = QFrame(self.configFrameOptions_5)
        self.flicksilentHeadBox_4.setObjectName(u"flicksilentHeadBox_4")
        self.flicksilentHeadBox_4.setMinimumSize(QSize(300, 55))
        self.flicksilentHeadBox_4.setMaximumSize(QSize(300, 55))
        self.flicksilentHeadBox_4.setStyleSheet(u"#flicksilentHeadBox_4{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.flicksilentHeadBox_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentHeadBox_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.flicksilentHeadBox_4)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.flicksilentHeadPosLabel_4 = QLabel(self.flicksilentHeadBox_4)
        self.flicksilentHeadPosLabel_4.setObjectName(u"flicksilentHeadPosLabel_4")
        self.flicksilentHeadPosLabel_4.setFont(font3)
        self.flicksilentHeadPosLabel_4.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_92.addWidget(self.flicksilentHeadPosLabel_4)

        self.flicksilentHeadBoxContent_4 = QFrame(self.flicksilentHeadBox_4)
        self.flicksilentHeadBoxContent_4.setObjectName(u"flicksilentHeadBoxContent_4")
        self.flicksilentHeadBoxContent_4.setMinimumSize(QSize(150, 0))
        self.flicksilentHeadBoxContent_4.setMaximumSize(QSize(150, 16777215))
        self.flicksilentHeadBoxContent_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentHeadBoxContent_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.flicksilentHeadBoxContent_4)
        self.horizontalLayout_106.setSpacing(10)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.menuposx = QSlider(self.flicksilentHeadBoxContent_4)
        self.menuposx.setObjectName(u"menuposx")
        self.menuposx.setMinimumSize(QSize(100, 20))
        self.menuposx.setMaximumSize(QSize(100, 16777215))
        self.menuposx.setMaximum(30)
        self.menuposx.setPageStep(1)
        self.menuposx.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_106.addWidget(self.menuposx)

        self.menuPosXValue = QLabel(self.flicksilentHeadBoxContent_4)
        self.menuPosXValue.setObjectName(u"menuPosXValue")

        self.horizontalLayout_106.addWidget(self.menuPosXValue, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_92.addWidget(self.flicksilentHeadBoxContent_4, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_58.addWidget(self.flicksilentHeadBox_4)

        self.flicksilentHeadBox_5 = QFrame(self.configFrameOptions_5)
        self.flicksilentHeadBox_5.setObjectName(u"flicksilentHeadBox_5")
        self.flicksilentHeadBox_5.setMinimumSize(QSize(300, 55))
        self.flicksilentHeadBox_5.setMaximumSize(QSize(300, 55))
        self.flicksilentHeadBox_5.setStyleSheet(u"#flicksilentHeadBox_5{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.flicksilentHeadBox_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentHeadBox_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.flicksilentHeadBox_5)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.flicksilentHeadPosLabel_5 = QLabel(self.flicksilentHeadBox_5)
        self.flicksilentHeadPosLabel_5.setObjectName(u"flicksilentHeadPosLabel_5")
        self.flicksilentHeadPosLabel_5.setFont(font3)
        self.flicksilentHeadPosLabel_5.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_107.addWidget(self.flicksilentHeadPosLabel_5)

        self.flicksilentHeadBoxContent_5 = QFrame(self.flicksilentHeadBox_5)
        self.flicksilentHeadBoxContent_5.setObjectName(u"flicksilentHeadBoxContent_5")
        self.flicksilentHeadBoxContent_5.setMinimumSize(QSize(150, 0))
        self.flicksilentHeadBoxContent_5.setMaximumSize(QSize(150, 16777215))
        self.flicksilentHeadBoxContent_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.flicksilentHeadBoxContent_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.flicksilentHeadBoxContent_5)
        self.horizontalLayout_108.setSpacing(10)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalLayout_108.setContentsMargins(0, 0, 0, 0)
        self.menuposy = QSlider(self.flicksilentHeadBoxContent_5)
        self.menuposy.setObjectName(u"menuposy")
        self.menuposy.setMinimumSize(QSize(100, 20))
        self.menuposy.setMaximumSize(QSize(100, 16777215))
        self.menuposy.setMaximum(30)
        self.menuposy.setPageStep(1)
        self.menuposy.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_108.addWidget(self.menuposy)

        self.menuPosYValue = QLabel(self.flicksilentHeadBoxContent_5)
        self.menuPosYValue.setObjectName(u"menuPosYValue")

        self.horizontalLayout_108.addWidget(self.menuPosYValue, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_107.addWidget(self.flicksilentHeadBoxContent_5, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_58.addWidget(self.flicksilentHeadBox_5)

        self.drawFov_6 = QFrame(self.configFrameOptions_5)
        self.drawFov_6.setObjectName(u"drawFov_6")
        self.drawFov_6.setMinimumSize(QSize(300, 55))
        self.drawFov_6.setMaximumSize(QSize(300, 55))
        self.drawFov_6.setStyleSheet(u"#drawFov_6{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.drawFov_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.drawFov_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.drawFov_6)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.drawFovLabel_6 = QLabel(self.drawFov_6)
        self.drawFovLabel_6.setObjectName(u"drawFovLabel_6")
        self.drawFovLabel_6.setFont(font3)
        self.drawFovLabel_6.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_109.addWidget(self.drawFovLabel_6)

        self.drawFovBoxConten_6 = QFrame(self.drawFov_6)
        self.drawFovBoxConten_6.setObjectName(u"drawFovBoxConten_6")
        self.drawFovBoxConten_6.setMinimumSize(QSize(150, 0))
        self.drawFovBoxConten_6.setMaximumSize(QSize(150, 16777215))
        self.drawFovBoxConten_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.drawFovBoxConten_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.drawFovBoxConten_6)
        self.horizontalLayout_110.setSpacing(10)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.drawfovaim = QRadioButton(self.drawFovBoxConten_6)
        self.drawfovaim.setObjectName(u"drawfovaim")
        self.drawfovaim.setStyleSheet(u"outline: 0;")

        self.horizontalLayout_110.addWidget(self.drawfovaim)


        self.horizontalLayout_109.addWidget(self.drawFovBoxConten_6)


        self.verticalLayout_58.addWidget(self.drawFov_6)

        self.drawFov_7 = QFrame(self.configFrameOptions_5)
        self.drawFov_7.setObjectName(u"drawFov_7")
        self.drawFov_7.setMinimumSize(QSize(300, 55))
        self.drawFov_7.setMaximumSize(QSize(300, 55))
        self.drawFov_7.setStyleSheet(u"#drawFov_7{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.drawFov_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.drawFov_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.drawFov_7)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.drawFovLabel_7 = QLabel(self.drawFov_7)
        self.drawFovLabel_7.setObjectName(u"drawFovLabel_7")
        self.drawFovLabel_7.setFont(font3)
        self.drawFovLabel_7.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_111.addWidget(self.drawFovLabel_7)

        self.drawFovBoxConten_7 = QFrame(self.drawFov_7)
        self.drawFovBoxConten_7.setObjectName(u"drawFovBoxConten_7")
        self.drawFovBoxConten_7.setMinimumSize(QSize(150, 0))
        self.drawFovBoxConten_7.setMaximumSize(QSize(150, 16777215))
        self.drawFovBoxConten_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.drawFovBoxConten_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_112 = QHBoxLayout(self.drawFovBoxConten_7)
        self.horizontalLayout_112.setSpacing(10)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.drawfovflick = QRadioButton(self.drawFovBoxConten_7)
        self.drawfovflick.setObjectName(u"drawfovflick")
        self.drawfovflick.setStyleSheet(u"outline: 0;")

        self.horizontalLayout_112.addWidget(self.drawfovflick)


        self.horizontalLayout_111.addWidget(self.drawFovBoxConten_7)


        self.verticalLayout_58.addWidget(self.drawFov_7)

        self.drawFov_8 = QFrame(self.configFrameOptions_5)
        self.drawFov_8.setObjectName(u"drawFov_8")
        self.drawFov_8.setMinimumSize(QSize(300, 55))
        self.drawFov_8.setMaximumSize(QSize(300, 55))
        self.drawFov_8.setStyleSheet(u"#drawFov_8{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.drawFov_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.drawFov_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_113 = QHBoxLayout(self.drawFov_8)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.drawFovLabel_8 = QLabel(self.drawFov_8)
        self.drawFovLabel_8.setObjectName(u"drawFovLabel_8")
        self.drawFovLabel_8.setFont(font3)
        self.drawFovLabel_8.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_113.addWidget(self.drawFovLabel_8)

        self.drawFovBoxConten_8 = QFrame(self.drawFov_8)
        self.drawFovBoxConten_8.setObjectName(u"drawFovBoxConten_8")
        self.drawFovBoxConten_8.setMinimumSize(QSize(150, 0))
        self.drawFovBoxConten_8.setMaximumSize(QSize(150, 16777215))
        self.drawFovBoxConten_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.drawFovBoxConten_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_114 = QHBoxLayout(self.drawFovBoxConten_8)
        self.horizontalLayout_114.setSpacing(10)
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.horizontalLayout_114.setContentsMargins(0, 0, 0, 0)
        self.drawinstalock = QRadioButton(self.drawFovBoxConten_8)
        self.drawinstalock.setObjectName(u"drawinstalock")
        self.drawinstalock.setStyleSheet(u"outline: 0;")

        self.horizontalLayout_114.addWidget(self.drawinstalock)


        self.horizontalLayout_113.addWidget(self.drawFovBoxConten_8)


        self.verticalLayout_58.addWidget(self.drawFov_8)


        self.verticalLayout_56.addWidget(self.configFrameOptions_5, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_34.addWidget(self.configFrame_5)

        self.configFrame_4 = QFrame(self.shortcutsMainFrame_3)
        self.configFrame_4.setObjectName(u"configFrame_4")
        self.configFrame_4.setStyleSheet(u"")
        self.configFrame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.configFrame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.configFrame_4)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(2, 0, 0, 0)
        self.tittleConfigs_4 = QFrame(self.configFrame_4)
        self.tittleConfigs_4.setObjectName(u"tittleConfigs_4")
        sizePolicy1.setHeightForWidth(self.tittleConfigs_4.sizePolicy().hasHeightForWidth())
        self.tittleConfigs_4.setSizePolicy(sizePolicy1)
        self.tittleConfigs_4.setMinimumSize(QSize(0, 0))
        self.tittleConfigs_4.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.tittleConfigs_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.tittleConfigs_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.tittleConfigs_4)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, -1, -1)
        self.tittleConfigsLabel_4 = QLabel(self.tittleConfigs_4)
        self.tittleConfigsLabel_4.setObjectName(u"tittleConfigsLabel_4")
        self.tittleConfigsLabel_4.setFont(font1)
        self.tittleConfigsLabel_4.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.verticalLayout_55.addWidget(self.tittleConfigsLabel_4, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_54.addWidget(self.tittleConfigs_4, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.configFrameOptions_4 = QFrame(self.configFrame_4)
        self.configFrameOptions_4.setObjectName(u"configFrameOptions_4")
        self.configFrameOptions_4.setMinimumSize(QSize(0, 317))
        self.configFrameOptions_4.setMaximumSize(QSize(16777215, 317))
        self.configFrameOptions_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.configFrameOptions_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.configFrameOptions_4)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.colorFrame_3 = QFrame(self.configFrameOptions_4)
        self.colorFrame_3.setObjectName(u"colorFrame_3")
        self.colorFrame_3.setMinimumSize(QSize(300, 55))
        self.colorFrame_3.setMaximumSize(QSize(300, 55))
        self.colorFrame_3.setStyleSheet(u"#colorFrame_3{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.colorFrame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.colorFrame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.colorFrame_3)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.colorLabel_3 = QLabel(self.colorFrame_3)
        self.colorLabel_3.setObjectName(u"colorLabel_3")
        self.colorLabel_3.setFont(font3)
        self.colorLabel_3.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_102.addWidget(self.colorLabel_3)

        self.colorFrameBox_3 = QFrame(self.colorFrame_3)
        self.colorFrameBox_3.setObjectName(u"colorFrameBox_3")
        self.colorFrameBox_3.setMinimumSize(QSize(150, 0))
        self.colorFrameBox_3.setMaximumSize(QSize(150, 16777215))
        self.colorFrameBox_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.colorFrameBox_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.colorFrameBox_3)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.sproof = QRadioButton(self.colorFrameBox_3)
        self.sproof.setObjectName(u"sproof")

        self.horizontalLayout_103.addWidget(self.sproof)


        self.horizontalLayout_102.addWidget(self.colorFrameBox_3, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_25.addWidget(self.colorFrame_3)

        self.frame_3 = QFrame(self.configFrameOptions_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_25.addWidget(self.frame_3)


        self.verticalLayout_54.addWidget(self.configFrameOptions_4, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_34.addWidget(self.configFrame_4)


        self.verticalLayout_26.addWidget(self.shortcutsMainFrame_3)

        self.stackedWidget.addWidget(self.visualPage)
        self.instalockPage = QWidget()
        self.instalockPage.setObjectName(u"instalockPage")
        self.verticalLayout_37 = QVBoxLayout(self.instalockPage)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, -1, 0)
        self.instalockMainFrame = QFrame(self.instalockPage)
        self.instalockMainFrame.setObjectName(u"instalockMainFrame")
        self.instalockMainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.instalockMainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.instalockMainFrame)
        self.horizontalLayout_50.setSpacing(20)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.instalockFrame = QFrame(self.instalockMainFrame)
        self.instalockFrame.setObjectName(u"instalockFrame")
        self.instalockFrame.setStyleSheet(u"")
        self.instalockFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.instalockFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.instalockFrame)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(2, 0, 0, 0)
        self.titleInstalock = QFrame(self.instalockFrame)
        self.titleInstalock.setObjectName(u"titleInstalock")
        sizePolicy1.setHeightForWidth(self.titleInstalock.sizePolicy().hasHeightForWidth())
        self.titleInstalock.setSizePolicy(sizePolicy1)
        self.titleInstalock.setMinimumSize(QSize(0, 0))
        self.titleInstalock.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")
        self.titleInstalock.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleInstalock.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.titleInstalock)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, -1, 9)
        self.titleInstalockLabel = QLabel(self.titleInstalock)
        self.titleInstalockLabel.setObjectName(u"titleInstalockLabel")
        self.titleInstalockLabel.setFont(font1)
        self.titleInstalockLabel.setStyleSheet(u"font: 800 15pt \"Segoe UI\";")

        self.verticalLayout_34.addWidget(self.titleInstalockLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_33.addWidget(self.titleInstalock, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.instalockOptions = QFrame(self.instalockFrame)
        self.instalockOptions.setObjectName(u"instalockOptions")
        self.instalockOptions.setFrameShape(QFrame.Shape.StyledPanel)
        self.instalockOptions.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.instalockOptions)
        self.verticalLayout_35.setSpacing(10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.instalockBox = QFrame(self.instalockOptions)
        self.instalockBox.setObjectName(u"instalockBox")
        self.instalockBox.setMinimumSize(QSize(300, 55))
        self.instalockBox.setMaximumSize(QSize(300, 55))
        self.instalockBox.setStyleSheet(u"#instalockBox{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.instalockBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.instalockBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.instalockBox)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.instalockLabel = QLabel(self.instalockBox)
        self.instalockLabel.setObjectName(u"instalockLabel")
        self.instalockLabel.setFont(font3)
        self.instalockLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_51.addWidget(self.instalockLabel)

        self.instalockBoxContent = QFrame(self.instalockBox)
        self.instalockBoxContent.setObjectName(u"instalockBoxContent")
        self.instalockBoxContent.setMinimumSize(QSize(150, 0))
        self.instalockBoxContent.setMaximumSize(QSize(150, 16777215))
        self.instalockBoxContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.instalockBoxContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.instalockBoxContent)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.instalockStatus = QRadioButton(self.instalockBoxContent)
        self.instalockStatus.setObjectName(u"instalockStatus")
        self.instalockStatus.setStyleSheet(u"outline: 0;")

        self.horizontalLayout_52.addWidget(self.instalockStatus)


        self.horizontalLayout_51.addWidget(self.instalockBoxContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_35.addWidget(self.instalockBox)

        self.instalockModeFrame = QFrame(self.instalockOptions)
        self.instalockModeFrame.setObjectName(u"instalockModeFrame")
        self.instalockModeFrame.setMinimumSize(QSize(300, 55))
        self.instalockModeFrame.setMaximumSize(QSize(300, 55))
        self.instalockModeFrame.setStyleSheet(u"#instalockModeFrame{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(10, 11, 13);\n"
"}")
        self.instalockModeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.instalockModeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.instalockModeFrame)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.instalockModeLabel = QLabel(self.instalockModeFrame)
        self.instalockModeLabel.setObjectName(u"instalockModeLabel")
        self.instalockModeLabel.setFont(font3)
        self.instalockModeLabel.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_53.addWidget(self.instalockModeLabel)

        self.instalockModeContent = QFrame(self.instalockModeFrame)
        self.instalockModeContent.setObjectName(u"instalockModeContent")
        self.instalockModeContent.setMinimumSize(QSize(150, 0))
        self.instalockModeContent.setMaximumSize(QSize(150, 16777215))
        self.instalockModeContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.instalockModeContent.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.instalockModeContent)
        self.horizontalLayout_54.setSpacing(10)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.instalockAgent = QComboBox(self.instalockModeContent)
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.addItem("")
        self.instalockAgent.setObjectName(u"instalockAgent")
        self.instalockAgent.setMinimumSize(QSize(0, 35))
        self.instalockAgent.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_54.addWidget(self.instalockAgent)


        self.horizontalLayout_53.addWidget(self.instalockModeContent, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_35.addWidget(self.instalockModeFrame)


        self.verticalLayout_33.addWidget(self.instalockOptions, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_50.addWidget(self.instalockFrame, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_37.addWidget(self.instalockMainFrame)

        self.stackedWidget.addWidget(self.instalockPage)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.pagesContainer)


        self.verticalLayout_21.addWidget(self.mainContent)


        self.appMargins.addWidget(self.bgApp)

        menuMain.setCentralWidget(self.styleSheet)

        self.retranslateUi(menuMain)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(menuMain)
    # setupUi

    def retranslateUi(self, menuMain):
        menuMain.setWindowTitle(QCoreApplication.translate("menuMain", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("menuMain", u"PushButton", None))
        self.minimizeAppBtn.setText("")
        self.closeAppBtn.setText("")
        self.extraLabel.setText(QCoreApplication.translate("menuMain", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("menuMain", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("menuMain", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("menuMain", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("menuMain", u"More", None))
        self.btn_aim.setText(QCoreApplication.translate("menuMain", u"Aimbot/RCS", None))
        self.btn_trigger.setText(QCoreApplication.translate("menuMain", u"Triggerbot", None))
        self.btn_flicksilent.setText(QCoreApplication.translate("menuMain", u"Flick/Silent", None))
        self.btn_instalock.setText(QCoreApplication.translate("menuMain", u"Instalock", None))
        # self.btn_visual.setText(QCoreApplication.translate("menuMain", u"Visuals", None))
        self.btn_shortcuts.setText(QCoreApplication.translate("menuMain", u"Configs", None))
        self.titleAimLabel.setText(QCoreApplication.translate("menuMain", u"Aimbot", None))
        self.configNumber.setItemText(0, QCoreApplication.translate("menuMain", u"1", None))
        self.configNumber.setItemText(1, QCoreApplication.translate("menuMain", u"2", None))

        self.aimLabel.setText(QCoreApplication.translate("menuMain", u"Key", None))
        self.aimKey.setItemText(0, "")
        self.aimKey.setItemText(1, QCoreApplication.translate("menuMain", u"Left Click", None))
        self.aimKey.setItemText(2, QCoreApplication.translate("menuMain", u"Right Click", None))
        self.aimKey.setItemText(3, QCoreApplication.translate("menuMain", u"Middle Click", None))
        self.aimKey.setItemText(4, QCoreApplication.translate("menuMain", u"Mouse 4", None))
        self.aimKey.setItemText(5, QCoreApplication.translate("menuMain", u"Mouse 5", None))
        self.aimKey.setItemText(6, QCoreApplication.translate("menuMain", u"CTRL", None))
        self.aimKey.setItemText(7, QCoreApplication.translate("menuMain", u"SHIFT", None))
        self.aimKey.setItemText(8, QCoreApplication.translate("menuMain", u"ALT", None))
        self.aimKey.setItemText(9, QCoreApplication.translate("menuMain", u"CAPSLOCK", None))
        self.aimKey.setItemText(10, QCoreApplication.translate("menuMain", u"TAB", None))
        self.aimKey.setItemText(11, QCoreApplication.translate("menuMain", u"A", None))
        self.aimKey.setItemText(12, QCoreApplication.translate("menuMain", u"B", None))
        self.aimKey.setItemText(13, QCoreApplication.translate("menuMain", u"C", None))
        self.aimKey.setItemText(14, QCoreApplication.translate("menuMain", u"D", None))
        self.aimKey.setItemText(15, QCoreApplication.translate("menuMain", u"E", None))
        self.aimKey.setItemText(16, QCoreApplication.translate("menuMain", u"F", None))
        self.aimKey.setItemText(17, QCoreApplication.translate("menuMain", u"G", None))
        self.aimKey.setItemText(18, QCoreApplication.translate("menuMain", u"H", None))
        self.aimKey.setItemText(19, QCoreApplication.translate("menuMain", u"I", None))
        self.aimKey.setItemText(20, QCoreApplication.translate("menuMain", u"J", None))
        self.aimKey.setItemText(21, QCoreApplication.translate("menuMain", u"K", None))
        self.aimKey.setItemText(22, QCoreApplication.translate("menuMain", u"L", None))
        self.aimKey.setItemText(23, QCoreApplication.translate("menuMain", u"M", None))
        self.aimKey.setItemText(24, QCoreApplication.translate("menuMain", u"N", None))
        self.aimKey.setItemText(25, QCoreApplication.translate("menuMain", u"O", None))
        self.aimKey.setItemText(26, QCoreApplication.translate("menuMain", u"P", None))
        self.aimKey.setItemText(27, QCoreApplication.translate("menuMain", u"Q", None))
        self.aimKey.setItemText(28, QCoreApplication.translate("menuMain", u"R", None))
        self.aimKey.setItemText(29, QCoreApplication.translate("menuMain", u"S", None))
        self.aimKey.setItemText(30, QCoreApplication.translate("menuMain", u"T", None))
        self.aimKey.setItemText(31, QCoreApplication.translate("menuMain", u"U", None))
        self.aimKey.setItemText(32, QCoreApplication.translate("menuMain", u"V", None))
        self.aimKey.setItemText(33, QCoreApplication.translate("menuMain", u"W", None))
        self.aimKey.setItemText(34, QCoreApplication.translate("menuMain", u"X", None))
        self.aimKey.setItemText(35, QCoreApplication.translate("menuMain", u"Y", None))
        self.aimKey.setItemText(36, QCoreApplication.translate("menuMain", u"Z", None))

        self.smoothLabel.setText(QCoreApplication.translate("menuMain", u"Smooth", None))
        self.smoothValue.setText(QCoreApplication.translate("menuMain", u"0", None))
        self.fovLabel.setText(QCoreApplication.translate("menuMain", u"FOV (x/y)", None))
        self.headLabel.setText(QCoreApplication.translate("menuMain", u"Head Position", None))
        self.aimHeadposValue.setText(QCoreApplication.translate("menuMain", u"0", None))
        self.rcsTitleLabel.setText(QCoreApplication.translate("menuMain", u"Recoil Control System", None))
        self.rcsLabel.setText(QCoreApplication.translate("menuMain", u"Enable RCS", None))
        self.rcsenable.setText("")
        self.downSpeedLabel.setText(QCoreApplication.translate("menuMain", u"RCS Down Speed", None))
        self.downspeedValue.setText(QCoreApplication.translate("menuMain", u"0", None))
        self.downLimitLabel.setText(QCoreApplication.translate("menuMain", u"RCS Down Limit", None))
        self.downlimitValue.setText(QCoreApplication.translate("menuMain", u"0", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("menuMain", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("menuMain", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("menuMain", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("menuMain", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("menuMain", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("menuMain", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("menuMain", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("menuMain", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("menuMain", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("menuMain", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("menuMain", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("menuMain", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("menuMain", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("menuMain", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("menuMain", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("menuMain", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("menuMain", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("menuMain", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("menuMain", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("menuMain", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("menuMain", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.titleTriggerLabel.setText(QCoreApplication.translate("menuMain", u"Triggerbot", None))
        self.triggerLabel.setText(QCoreApplication.translate("menuMain", u"Key", None))
        self.triggerKey.setItemText(0, "")
        self.triggerKey.setItemText(1, QCoreApplication.translate("menuMain", u"Mouse 4", None))
        self.triggerKey.setItemText(2, QCoreApplication.translate("menuMain", u"Mouse 5", None))
        self.triggerKey.setItemText(3, QCoreApplication.translate("menuMain", u"CTRL", None))
        self.triggerKey.setItemText(4, QCoreApplication.translate("menuMain", u"SHIFT", None))
        self.triggerKey.setItemText(5, QCoreApplication.translate("menuMain", u"ALT", None))
        self.triggerKey.setItemText(6, QCoreApplication.translate("menuMain", u"CAPSLOCK", None))
        self.triggerKey.setItemText(7, QCoreApplication.translate("menuMain", u"TAB", None))
        self.triggerKey.setItemText(8, QCoreApplication.translate("menuMain", u"A", None))
        self.triggerKey.setItemText(9, QCoreApplication.translate("menuMain", u"B", None))
        self.triggerKey.setItemText(10, QCoreApplication.translate("menuMain", u"C", None))
        self.triggerKey.setItemText(11, QCoreApplication.translate("menuMain", u"D", None))
        self.triggerKey.setItemText(12, QCoreApplication.translate("menuMain", u"E", None))
        self.triggerKey.setItemText(13, QCoreApplication.translate("menuMain", u"F", None))
        self.triggerKey.setItemText(14, QCoreApplication.translate("menuMain", u"G", None))
        self.triggerKey.setItemText(15, QCoreApplication.translate("menuMain", u"H", None))
        self.triggerKey.setItemText(16, QCoreApplication.translate("menuMain", u"I", None))
        self.triggerKey.setItemText(17, QCoreApplication.translate("menuMain", u"J", None))
        self.triggerKey.setItemText(18, QCoreApplication.translate("menuMain", u"K", None))
        self.triggerKey.setItemText(19, QCoreApplication.translate("menuMain", u"L", None))
        self.triggerKey.setItemText(20, QCoreApplication.translate("menuMain", u"M", None))
        self.triggerKey.setItemText(21, QCoreApplication.translate("menuMain", u"N", None))
        self.triggerKey.setItemText(22, QCoreApplication.translate("menuMain", u"O", None))
        self.triggerKey.setItemText(23, QCoreApplication.translate("menuMain", u"P", None))
        self.triggerKey.setItemText(24, QCoreApplication.translate("menuMain", u"Q", None))
        self.triggerKey.setItemText(25, QCoreApplication.translate("menuMain", u"R", None))
        self.triggerKey.setItemText(26, QCoreApplication.translate("menuMain", u"S", None))
        self.triggerKey.setItemText(27, QCoreApplication.translate("menuMain", u"T", None))
        self.triggerKey.setItemText(28, QCoreApplication.translate("menuMain", u"U", None))
        self.triggerKey.setItemText(29, QCoreApplication.translate("menuMain", u"V", None))
        self.triggerKey.setItemText(30, QCoreApplication.translate("menuMain", u"W", None))
        self.triggerKey.setItemText(31, QCoreApplication.translate("menuMain", u"X", None))
        self.triggerKey.setItemText(32, QCoreApplication.translate("menuMain", u"Y", None))
        self.triggerKey.setItemText(33, QCoreApplication.translate("menuMain", u"Z", None))
        self.triggerKey.setItemText(34, QCoreApplication.translate("menuMain", u"F1", None))
        self.triggerKey.setItemText(35, QCoreApplication.translate("menuMain", u"F2", None))
        self.triggerKey.setItemText(36, QCoreApplication.translate("menuMain", u"F3", None))
        self.triggerKey.setItemText(37, QCoreApplication.translate("menuMain", u"F4", None))
        self.triggerKey.setItemText(38, QCoreApplication.translate("menuMain", u"F5", None))
        self.triggerKey.setItemText(39, QCoreApplication.translate("menuMain", u"F6", None))
        self.triggerKey.setItemText(40, QCoreApplication.translate("menuMain", u"F7", None))
        self.triggerKey.setItemText(41, QCoreApplication.translate("menuMain", u"F8", None))
        self.triggerKey.setItemText(42, QCoreApplication.translate("menuMain", u"F9", None))
        self.triggerKey.setItemText(43, QCoreApplication.translate("menuMain", u"F10", None))
        self.triggerKey.setItemText(44, QCoreApplication.translate("menuMain", u"F11", None))
        self.triggerKey.setItemText(45, QCoreApplication.translate("menuMain", u"F12", None))

        self.triggerFovLabel.setText(QCoreApplication.translate("menuMain", u"FOV (x/y)", None))
        self.triggerShootDelayLabel.setText(QCoreApplication.translate("menuMain", u"Shoot Delay", None))
        self.triggerShootdelayValue.setText(QCoreApplication.translate("menuMain", u"0", None))
        self.triggerModeLabel.setText(QCoreApplication.translate("menuMain", u"Mode", None))
        self.triggerMode.setItemText(0, QCoreApplication.translate("menuMain", u"Holding", None))
        self.triggerMode.setItemText(1, QCoreApplication.translate("menuMain", u"Toggle", None))

        self.titletitleFlicksilentLabel.setText(QCoreApplication.translate("menuMain", u"Flick & Silent", None))
        self.flicksilentLabel.setText(QCoreApplication.translate("menuMain", u"Key", None))
        self.flicksilentKey.setItemText(0, "")
        self.flicksilentKey.setItemText(1, QCoreApplication.translate("menuMain", u"Middle Click", None))
        self.flicksilentKey.setItemText(2, QCoreApplication.translate("menuMain", u"Mouse 4", None))
        self.flicksilentKey.setItemText(3, QCoreApplication.translate("menuMain", u"Mouse 5", None))
        self.flicksilentKey.setItemText(4, QCoreApplication.translate("menuMain", u"CTRL", None))
        self.flicksilentKey.setItemText(5, QCoreApplication.translate("menuMain", u"SHIFT", None))
        self.flicksilentKey.setItemText(6, QCoreApplication.translate("menuMain", u"ALT", None))
        self.flicksilentKey.setItemText(7, QCoreApplication.translate("menuMain", u"CAPSLOCK", None))
        self.flicksilentKey.setItemText(8, QCoreApplication.translate("menuMain", u"TAB", None))
        self.flicksilentKey.setItemText(9, QCoreApplication.translate("menuMain", u"A", None))
        self.flicksilentKey.setItemText(10, QCoreApplication.translate("menuMain", u"B", None))
        self.flicksilentKey.setItemText(11, QCoreApplication.translate("menuMain", u"C", None))
        self.flicksilentKey.setItemText(12, QCoreApplication.translate("menuMain", u"D", None))
        self.flicksilentKey.setItemText(13, QCoreApplication.translate("menuMain", u"E", None))
        self.flicksilentKey.setItemText(14, QCoreApplication.translate("menuMain", u"F", None))
        self.flicksilentKey.setItemText(15, QCoreApplication.translate("menuMain", u"G", None))
        self.flicksilentKey.setItemText(16, QCoreApplication.translate("menuMain", u"H", None))
        self.flicksilentKey.setItemText(17, QCoreApplication.translate("menuMain", u"I", None))
        self.flicksilentKey.setItemText(18, QCoreApplication.translate("menuMain", u"J", None))
        self.flicksilentKey.setItemText(19, QCoreApplication.translate("menuMain", u"K", None))
        self.flicksilentKey.setItemText(20, QCoreApplication.translate("menuMain", u"L", None))
        self.flicksilentKey.setItemText(21, QCoreApplication.translate("menuMain", u"M", None))
        self.flicksilentKey.setItemText(22, QCoreApplication.translate("menuMain", u"N", None))
        self.flicksilentKey.setItemText(23, QCoreApplication.translate("menuMain", u"O", None))
        self.flicksilentKey.setItemText(24, QCoreApplication.translate("menuMain", u"P", None))
        self.flicksilentKey.setItemText(25, QCoreApplication.translate("menuMain", u"Q", None))
        self.flicksilentKey.setItemText(26, QCoreApplication.translate("menuMain", u"R", None))
        self.flicksilentKey.setItemText(27, QCoreApplication.translate("menuMain", u"S", None))
        self.flicksilentKey.setItemText(28, QCoreApplication.translate("menuMain", u"T", None))
        self.flicksilentKey.setItemText(29, QCoreApplication.translate("menuMain", u"U", None))
        self.flicksilentKey.setItemText(30, QCoreApplication.translate("menuMain", u"V", None))
        self.flicksilentKey.setItemText(31, QCoreApplication.translate("menuMain", u"W", None))
        self.flicksilentKey.setItemText(32, QCoreApplication.translate("menuMain", u"X", None))
        self.flicksilentKey.setItemText(33, QCoreApplication.translate("menuMain", u"Y", None))
        self.flicksilentKey.setItemText(34, QCoreApplication.translate("menuMain", u"Z", None))

        self.flicksilentModeLabel.setText(QCoreApplication.translate("menuMain", u"Mode", None))
        self.flicksilentMode.setItemText(0, QCoreApplication.translate("menuMain", u"Flickbot", None))
        self.flicksilentMode.setItemText(1, QCoreApplication.translate("menuMain", u"Silentbot", None))

        self.flicksilentFovLabel.setText(QCoreApplication.translate("menuMain", u"FOV (x/y)", None))
        self.flicksilentHeadPosLabel.setText(QCoreApplication.translate("menuMain", u"Head Position", None))
        self.flicksilentHeadposValue.setText(QCoreApplication.translate("menuMain", u"0", None))
        self.tittleShortcutsLabel.setText(QCoreApplication.translate("menuMain", u"Shortcuts", None))
        self.streamProofLabel.setText(QCoreApplication.translate("menuMain", u"Stream Proof", None))
        self.streamproof.setText("")
        self.switchConfig1Label.setText(QCoreApplication.translate("menuMain", u"Switch Config 1", None))
        self.switchconfig1.setItemText(0, "")
        self.switchconfig1.setItemText(1, QCoreApplication.translate("menuMain", u"F1", None))
        self.switchconfig1.setItemText(2, QCoreApplication.translate("menuMain", u"F2", None))
        self.switchconfig1.setItemText(3, QCoreApplication.translate("menuMain", u"F3", None))
        self.switchconfig1.setItemText(4, QCoreApplication.translate("menuMain", u"F4", None))
        self.switchconfig1.setItemText(5, QCoreApplication.translate("menuMain", u"F5", None))
        self.switchconfig1.setItemText(6, QCoreApplication.translate("menuMain", u"F6", None))
        self.switchconfig1.setItemText(7, QCoreApplication.translate("menuMain", u"F7", None))
        self.switchconfig1.setItemText(8, QCoreApplication.translate("menuMain", u"F8", None))
        self.switchconfig1.setItemText(9, QCoreApplication.translate("menuMain", u"F9", None))
        self.switchconfig1.setItemText(10, QCoreApplication.translate("menuMain", u"F10", None))
        self.switchconfig1.setItemText(11, QCoreApplication.translate("menuMain", u"F11", None))
        self.switchconfig1.setItemText(12, QCoreApplication.translate("menuMain", u"F12", None))
        self.switchconfig1.setItemText(13, QCoreApplication.translate("menuMain", u"A", None))
        self.switchconfig1.setItemText(14, QCoreApplication.translate("menuMain", u"B", None))
        self.switchconfig1.setItemText(15, QCoreApplication.translate("menuMain", u"C", None))
        self.switchconfig1.setItemText(16, QCoreApplication.translate("menuMain", u"D", None))
        self.switchconfig1.setItemText(17, QCoreApplication.translate("menuMain", u"E", None))
        self.switchconfig1.setItemText(18, QCoreApplication.translate("menuMain", u"F", None))
        self.switchconfig1.setItemText(19, QCoreApplication.translate("menuMain", u"G", None))
        self.switchconfig1.setItemText(20, QCoreApplication.translate("menuMain", u"H", None))
        self.switchconfig1.setItemText(21, QCoreApplication.translate("menuMain", u"I", None))
        self.switchconfig1.setItemText(22, QCoreApplication.translate("menuMain", u"J", None))
        self.switchconfig1.setItemText(23, QCoreApplication.translate("menuMain", u"K", None))
        self.switchconfig1.setItemText(24, QCoreApplication.translate("menuMain", u"L", None))
        self.switchconfig1.setItemText(25, QCoreApplication.translate("menuMain", u"M", None))
        self.switchconfig1.setItemText(26, QCoreApplication.translate("menuMain", u"N", None))
        self.switchconfig1.setItemText(27, QCoreApplication.translate("menuMain", u"O", None))
        self.switchconfig1.setItemText(28, QCoreApplication.translate("menuMain", u"P", None))
        self.switchconfig1.setItemText(29, QCoreApplication.translate("menuMain", u"Q", None))
        self.switchconfig1.setItemText(30, QCoreApplication.translate("menuMain", u"R", None))
        self.switchconfig1.setItemText(31, QCoreApplication.translate("menuMain", u"S", None))
        self.switchconfig1.setItemText(32, QCoreApplication.translate("menuMain", u"T", None))
        self.switchconfig1.setItemText(33, QCoreApplication.translate("menuMain", u"U", None))
        self.switchconfig1.setItemText(34, QCoreApplication.translate("menuMain", u"V", None))
        self.switchconfig1.setItemText(35, QCoreApplication.translate("menuMain", u"W", None))
        self.switchconfig1.setItemText(36, QCoreApplication.translate("menuMain", u"X", None))
        self.switchconfig1.setItemText(37, QCoreApplication.translate("menuMain", u"Y", None))
        self.switchconfig1.setItemText(38, QCoreApplication.translate("menuMain", u"Z", None))

        self.switchconfig1.setCurrentText("")
        self.switchConfig2Label.setText(QCoreApplication.translate("menuMain", u"Switch Config 2", None))
        self.switchconfig2.setItemText(0, "")
        self.switchconfig2.setItemText(1, QCoreApplication.translate("menuMain", u"F1", None))
        self.switchconfig2.setItemText(2, QCoreApplication.translate("menuMain", u"F2", None))
        self.switchconfig2.setItemText(3, QCoreApplication.translate("menuMain", u"F3", None))
        self.switchconfig2.setItemText(4, QCoreApplication.translate("menuMain", u"F4", None))
        self.switchconfig2.setItemText(5, QCoreApplication.translate("menuMain", u"F5", None))
        self.switchconfig2.setItemText(6, QCoreApplication.translate("menuMain", u"F6", None))
        self.switchconfig2.setItemText(7, QCoreApplication.translate("menuMain", u"F7", None))
        self.switchconfig2.setItemText(8, QCoreApplication.translate("menuMain", u"F8", None))
        self.switchconfig2.setItemText(9, QCoreApplication.translate("menuMain", u"F9", None))
        self.switchconfig2.setItemText(10, QCoreApplication.translate("menuMain", u"F10", None))
        self.switchconfig2.setItemText(11, QCoreApplication.translate("menuMain", u"F11", None))
        self.switchconfig2.setItemText(12, QCoreApplication.translate("menuMain", u"F12", None))
        self.switchconfig2.setItemText(13, QCoreApplication.translate("menuMain", u"A", None))
        self.switchconfig2.setItemText(14, QCoreApplication.translate("menuMain", u"B", None))
        self.switchconfig2.setItemText(15, QCoreApplication.translate("menuMain", u"C", None))
        self.switchconfig2.setItemText(16, QCoreApplication.translate("menuMain", u"D", None))
        self.switchconfig2.setItemText(17, QCoreApplication.translate("menuMain", u"E", None))
        self.switchconfig2.setItemText(18, QCoreApplication.translate("menuMain", u"F", None))
        self.switchconfig2.setItemText(19, QCoreApplication.translate("menuMain", u"G", None))
        self.switchconfig2.setItemText(20, QCoreApplication.translate("menuMain", u"H", None))
        self.switchconfig2.setItemText(21, QCoreApplication.translate("menuMain", u"I", None))
        self.switchconfig2.setItemText(22, QCoreApplication.translate("menuMain", u"J", None))
        self.switchconfig2.setItemText(23, QCoreApplication.translate("menuMain", u"K", None))
        self.switchconfig2.setItemText(24, QCoreApplication.translate("menuMain", u"L", None))
        self.switchconfig2.setItemText(25, QCoreApplication.translate("menuMain", u"M", None))
        self.switchconfig2.setItemText(26, QCoreApplication.translate("menuMain", u"N", None))
        self.switchconfig2.setItemText(27, QCoreApplication.translate("menuMain", u"O", None))
        self.switchconfig2.setItemText(28, QCoreApplication.translate("menuMain", u"P", None))
        self.switchconfig2.setItemText(29, QCoreApplication.translate("menuMain", u"Q", None))
        self.switchconfig2.setItemText(30, QCoreApplication.translate("menuMain", u"R", None))
        self.switchconfig2.setItemText(31, QCoreApplication.translate("menuMain", u"S", None))
        self.switchconfig2.setItemText(32, QCoreApplication.translate("menuMain", u"T", None))
        self.switchconfig2.setItemText(33, QCoreApplication.translate("menuMain", u"U", None))
        self.switchconfig2.setItemText(34, QCoreApplication.translate("menuMain", u"V", None))
        self.switchconfig2.setItemText(35, QCoreApplication.translate("menuMain", u"W", None))
        self.switchconfig2.setItemText(36, QCoreApplication.translate("menuMain", u"X", None))
        self.switchconfig2.setItemText(37, QCoreApplication.translate("menuMain", u"Y", None))
        self.switchconfig2.setItemText(38, QCoreApplication.translate("menuMain", u"Z", None))

        self.spinbotLabel.setText(QCoreApplication.translate("menuMain", u"Spin (misc)", None))
        self.spinbot.setItemText(0, "")
        self.spinbot.setItemText(1, QCoreApplication.translate("menuMain", u"Arrow Up", None))
        self.spinbot.setItemText(2, QCoreApplication.translate("menuMain", u"Arrow Down", None))
        self.spinbot.setItemText(3, QCoreApplication.translate("menuMain", u"Arrow Left", None))
        self.spinbot.setItemText(4, QCoreApplication.translate("menuMain", u"Arrow Right", None))
        self.spinbot.setItemText(5, QCoreApplication.translate("menuMain", u"A", None))
        self.spinbot.setItemText(6, QCoreApplication.translate("menuMain", u"B", None))
        self.spinbot.setItemText(7, QCoreApplication.translate("menuMain", u"C", None))
        self.spinbot.setItemText(8, QCoreApplication.translate("menuMain", u"D", None))
        self.spinbot.setItemText(9, QCoreApplication.translate("menuMain", u"E", None))
        self.spinbot.setItemText(10, QCoreApplication.translate("menuMain", u"F", None))
        self.spinbot.setItemText(11, QCoreApplication.translate("menuMain", u"G", None))
        self.spinbot.setItemText(12, QCoreApplication.translate("menuMain", u"H", None))
        self.spinbot.setItemText(13, QCoreApplication.translate("menuMain", u"I", None))
        self.spinbot.setItemText(14, QCoreApplication.translate("menuMain", u"J", None))
        self.spinbot.setItemText(15, QCoreApplication.translate("menuMain", u"K", None))
        self.spinbot.setItemText(16, QCoreApplication.translate("menuMain", u"L", None))
        self.spinbot.setItemText(17, QCoreApplication.translate("menuMain", u"M", None))
        self.spinbot.setItemText(18, QCoreApplication.translate("menuMain", u"N", None))
        self.spinbot.setItemText(19, QCoreApplication.translate("menuMain", u"O", None))
        self.spinbot.setItemText(20, QCoreApplication.translate("menuMain", u"P", None))
        self.spinbot.setItemText(21, QCoreApplication.translate("menuMain", u"Q", None))
        self.spinbot.setItemText(22, QCoreApplication.translate("menuMain", u"R", None))
        self.spinbot.setItemText(23, QCoreApplication.translate("menuMain", u"S", None))
        self.spinbot.setItemText(24, QCoreApplication.translate("menuMain", u"T", None))
        self.spinbot.setItemText(25, QCoreApplication.translate("menuMain", u"U", None))
        self.spinbot.setItemText(26, QCoreApplication.translate("menuMain", u"V", None))
        self.spinbot.setItemText(27, QCoreApplication.translate("menuMain", u"W", None))
        self.spinbot.setItemText(28, QCoreApplication.translate("menuMain", u"X", None))
        self.spinbot.setItemText(29, QCoreApplication.translate("menuMain", u"Y", None))
        self.spinbot.setItemText(30, QCoreApplication.translate("menuMain", u"Z", None))

        self.disableRcsLabel.setText(QCoreApplication.translate("menuMain", u"Disable RCS", None))
        self.disablercs.setItemText(0, "")
        self.disablercs.setItemText(1, QCoreApplication.translate("menuMain", u"A", None))
        self.disablercs.setItemText(2, QCoreApplication.translate("menuMain", u"B", None))
        self.disablercs.setItemText(3, QCoreApplication.translate("menuMain", u"C", None))
        self.disablercs.setItemText(4, QCoreApplication.translate("menuMain", u"D", None))
        self.disablercs.setItemText(5, QCoreApplication.translate("menuMain", u"E", None))
        self.disablercs.setItemText(6, QCoreApplication.translate("menuMain", u"F", None))
        self.disablercs.setItemText(7, QCoreApplication.translate("menuMain", u"G", None))
        self.disablercs.setItemText(8, QCoreApplication.translate("menuMain", u"H", None))
        self.disablercs.setItemText(9, QCoreApplication.translate("menuMain", u"I", None))
        self.disablercs.setItemText(10, QCoreApplication.translate("menuMain", u"J", None))
        self.disablercs.setItemText(11, QCoreApplication.translate("menuMain", u"K", None))
        self.disablercs.setItemText(12, QCoreApplication.translate("menuMain", u"L", None))
        self.disablercs.setItemText(13, QCoreApplication.translate("menuMain", u"M", None))
        self.disablercs.setItemText(14, QCoreApplication.translate("menuMain", u"N", None))
        self.disablercs.setItemText(15, QCoreApplication.translate("menuMain", u"O", None))
        self.disablercs.setItemText(16, QCoreApplication.translate("menuMain", u"P", None))
        self.disablercs.setItemText(17, QCoreApplication.translate("menuMain", u"Q", None))
        self.disablercs.setItemText(18, QCoreApplication.translate("menuMain", u"R", None))
        self.disablercs.setItemText(19, QCoreApplication.translate("menuMain", u"S", None))
        self.disablercs.setItemText(20, QCoreApplication.translate("menuMain", u"T", None))
        self.disablercs.setItemText(21, QCoreApplication.translate("menuMain", u"U", None))
        self.disablercs.setItemText(22, QCoreApplication.translate("menuMain", u"V", None))
        self.disablercs.setItemText(23, QCoreApplication.translate("menuMain", u"W", None))
        self.disablercs.setItemText(24, QCoreApplication.translate("menuMain", u"X", None))
        self.disablercs.setItemText(25, QCoreApplication.translate("menuMain", u"Y", None))
        self.disablercs.setItemText(26, QCoreApplication.translate("menuMain", u"Z", None))
        self.disablercs.setItemText(27, QCoreApplication.translate("menuMain", u"F1", None))
        self.disablercs.setItemText(28, QCoreApplication.translate("menuMain", u"F2", None))
        self.disablercs.setItemText(29, QCoreApplication.translate("menuMain", u"F3", None))
        self.disablercs.setItemText(30, QCoreApplication.translate("menuMain", u"F4", None))
        self.disablercs.setItemText(31, QCoreApplication.translate("menuMain", u"F5", None))
        self.disablercs.setItemText(32, QCoreApplication.translate("menuMain", u"F6", None))
        self.disablercs.setItemText(33, QCoreApplication.translate("menuMain", u"F7", None))
        self.disablercs.setItemText(34, QCoreApplication.translate("menuMain", u"F8", None))
        self.disablercs.setItemText(35, QCoreApplication.translate("menuMain", u"F9", None))
        self.disablercs.setItemText(36, QCoreApplication.translate("menuMain", u"F10", None))
        self.disablercs.setItemText(37, QCoreApplication.translate("menuMain", u"F11", None))
        self.disablercs.setItemText(38, QCoreApplication.translate("menuMain", u"F12", None))

        self.tittleConfigsLabel.setText(QCoreApplication.translate("menuMain", u"Configs", None))
        self.colorLabel.setText(QCoreApplication.translate("menuMain", u"Color", None))
        self.color.setItemText(0, QCoreApplication.translate("menuMain", u"Purple", None))
        self.color.setItemText(1, QCoreApplication.translate("menuMain", u"Red", None))
        self.color.setItemText(2, QCoreApplication.translate("menuMain", u"Yellow", None))

        self.color.setCurrentText(QCoreApplication.translate("menuMain", u"Purple", None))
        self.mouseLabel.setText(QCoreApplication.translate("menuMain", u"Mouse Sens", None))
        self.tittleConfigsLabel_5.setText(QCoreApplication.translate("menuMain", u"Visuals Draw", None))
        self.flicksilentHeadPosLabel_4.setText(QCoreApplication.translate("menuMain", u"Menu Position X", None))
        self.menuPosXValue.setText(QCoreApplication.translate("menuMain", u"0", None))
        self.flicksilentHeadPosLabel_5.setText(QCoreApplication.translate("menuMain", u"Menu Position Y", None))
        self.menuPosYValue.setText(QCoreApplication.translate("menuMain", u"0", None))
        self.drawFovLabel_6.setText(QCoreApplication.translate("menuMain", u"Fov Aim", None))
        self.drawfovaim.setText("")
        self.drawFovLabel_7.setText(QCoreApplication.translate("menuMain", u"Fov Flick & Silent", None))
        self.drawfovflick.setText("")
        self.drawFovLabel_8.setText(QCoreApplication.translate("menuMain", u"Instalock Status", None))
        self.drawinstalock.setText("")
        self.tittleConfigsLabel_4.setText(QCoreApplication.translate("menuMain", u"Configs Draw", None))
        self.colorLabel_3.setText(QCoreApplication.translate("menuMain", u"Stream Proof", None))
        self.sproof.setText("")
        self.titleInstalockLabel.setText(QCoreApplication.translate("menuMain", u"Instalock", None))
        self.instalockLabel.setText(QCoreApplication.translate("menuMain", u"Status", None))
        self.instalockStatus.setText("")
        self.instalockModeLabel.setText(QCoreApplication.translate("menuMain", u"Agent", None))
        self.instalockAgent.setItemText(0, QCoreApplication.translate("menuMain", u"Astra", None))
        self.instalockAgent.setItemText(1, QCoreApplication.translate("menuMain", u"Breach", None))
        self.instalockAgent.setItemText(2, QCoreApplication.translate("menuMain", u"Brimstone", None))
        self.instalockAgent.setItemText(3, QCoreApplication.translate("menuMain", u"Chamber", None))
        self.instalockAgent.setItemText(4, QCoreApplication.translate("menuMain", u"Clove", None))
        self.instalockAgent.setItemText(5, QCoreApplication.translate("menuMain", u"Cypher", None))
        self.instalockAgent.setItemText(6, QCoreApplication.translate("menuMain", u"Fade", None))
        self.instalockAgent.setItemText(7, QCoreApplication.translate("menuMain", u"Gekko", None))
        self.instalockAgent.setItemText(8, QCoreApplication.translate("menuMain", u"Harbor", None))
        self.instalockAgent.setItemText(9, QCoreApplication.translate("menuMain", u"Iso", None))
        self.instalockAgent.setItemText(10, QCoreApplication.translate("menuMain", u"Jett", None))
        self.instalockAgent.setItemText(11, QCoreApplication.translate("menuMain", u"KAY/O", None))
        self.instalockAgent.setItemText(12, QCoreApplication.translate("menuMain", u"Killjoy", None))
        self.instalockAgent.setItemText(13, QCoreApplication.translate("menuMain", u"Neon", None))
        self.instalockAgent.setItemText(14, QCoreApplication.translate("menuMain", u"Omen", None))
        self.instalockAgent.setItemText(15, QCoreApplication.translate("menuMain", u"Phoenix", None))
        self.instalockAgent.setItemText(16, QCoreApplication.translate("menuMain", u"Raze", None))
        self.instalockAgent.setItemText(17, QCoreApplication.translate("menuMain", u"Reyna", None))
        self.instalockAgent.setItemText(18, QCoreApplication.translate("menuMain", u"Sage", None))
        self.instalockAgent.setItemText(19, QCoreApplication.translate("menuMain", u"Skye", None))
        self.instalockAgent.setItemText(20, QCoreApplication.translate("menuMain", u"Sova", None))
        self.instalockAgent.setItemText(21, QCoreApplication.translate("menuMain", u"Viper", None))
        self.instalockAgent.setItemText(22, QCoreApplication.translate("menuMain", u"Yoru", None))
        self.instalockAgent.setItemText(23, QCoreApplication.translate("menuMain", u"Random Agent", None))

    # retranslateUi

