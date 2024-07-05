from . import *

MENU_SELECTED_STYLESHEET = """
    border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(140, 0, 255, 255), stop:0.5 rgba(85, 170, 255, 0));
    background-color: rgb(40, 44, 52);
    """
class UIFunctions:
    def flagsDefault(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def flagsLoading(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.X11BypassWindowManagerHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def visualDefinitions(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.setGraphicsEffect(self.shadow)

    def defaultDefinitions(self):
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.contentTopBg.mouseMoveEvent = moveWindow

        UIFunctions.visualDefinitions(self)
        UIFunctions.flagsDefault(self)

        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())
        self.ui.closeAppBtn.clicked.connect(lambda: self.close())

    def mainDefinitions(self):
        UIFunctions.defaultDefinitions(self)

    def toggleMenu(self, enable):
        if enable:
            width = self.ui.leftMenuBg.width()
            width2 = self.width()

            maxExtend = 170
            standard = 60

            maxExtend2 = 835
            standard2 = 725

            widthExtended = maxExtend if width == standard else standard
            widthExtended2 = maxExtend2 if width2 == standard2 else standard2

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)

            self.animation2 = QPropertyAnimation(self, b"size")
            self.animation2.setDuration(500)
            self.animation2.setStartValue(QSize(width2, self.height()))
            self.animation2.setEndValue(QSize(widthExtended2, self.height()))
            self.animation2.setEasingCurve(QEasingCurve.InOutQuart)

            self.animation.start()
            self.animation2.start()

    def selectMenu(getStyle):
        select = getStyle + MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(MENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
    def selectStandardMenu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() == widget:
                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))
