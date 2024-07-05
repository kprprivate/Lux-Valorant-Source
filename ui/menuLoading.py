# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menuLoadingPlbUNK.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)
from . import resources_rc

class Ui_menuLoading(object):
    def setupUi(self, menuLoading):
        if not menuLoading.objectName():
            menuLoading.setObjectName(u"menuLoading")
        menuLoading.resize(200, 200)
        menuLoading.setMinimumSize(QSize(200, 200))
        menuLoading.setMaximumSize(QSize(200, 200))
        self.styleSheet = QWidget(menuLoading)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"background-image: url(:/images/images/images/luxicon2.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-color: rgba(0, 0, 0, 0);")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(0, 0, 0, 0)
        menuLoading.setCentralWidget(self.styleSheet)

        self.retranslateUi(menuLoading)

        QMetaObject.connectSlotsByName(menuLoading)
    # setupUi

    def retranslateUi(self, menuLoading):
        menuLoading.setWindowTitle(QCoreApplication.translate("menuLoading", u"MainWindow", None))
    # retranslateUi

