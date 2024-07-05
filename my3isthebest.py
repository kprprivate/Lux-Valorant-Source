import json
from ctypes import wintypes, WINFUNCTYPE

from ui import *
from modules import *

import os
import sys
import random
import time
import string

from threading import Thread

objError = False
versionNumb = 1.0

class functionStarter(QThread):
    # def __init__(self, overlay):
    def __init__(self):
        super().__init__()
        # self.overlay = overlay

    def run(self):
        Thread(target=self.aim).start()
        Thread(target=self.rcsMagic).start()
        Thread(target=self.trigger).start()
        Thread(target=self.flicksilent).start()
        Thread(target=self.instalock).start()
        Thread(target=self.spin).start()
        Thread(target=self.switchConfig).start()
        Thread(target=self.auth).start()
        return

    @staticmethod
    def auth():
        if expiry != "Lifetime":
            time.sleep(expiry)
            lux.deactivate()
            showErrorMessageBox("Expired", "Renew your sub to keep using.")

    @staticmethod
    def aim():
        while True:
            try:
                key = varManager.getVar("key", "AIM" + varManager.configNumb)
                if keyPressed(key):
                    enemy = luxFunctions.findEnemyAim()
                    if enemy:
                        lux.move(enemy[0], enemy[1] + varManager.rcs)
                time.sleep(0.005)
            except Exception as e:
                print(e)
                pass

    @staticmethod
    def rcsMagic():
        rcsAllow = True
        while True:
            try:
                keyDisable = varManager.getVar("disablercs", "CONFIGS")
                key = varManager.getVar("key", "AIM" + varManager.configNumb)
                downspeed = int(varManager.getVar("downspeed", "AIM" + varManager.configNumb))
                downlimit = int(varManager.getVar("downlimit", "AIM" + varManager.configNumb))
                status = json.loads(varManager.getVar("rcsenable", "AIM" + varManager.configNumb).lower())

                width, height = getScreenResolution()

                timeStart = 0

                if keyPressed(keyDisable):
                    rcsAllow = not rcsAllow

                    if rcsAllow:
                        beepSound(440, 75)
                        beepSound(700, 100)
                    else:
                        beepSound(440, 75)
                        beepSound(200, 100)

                    while keyPressed(keyDisable):
                        pass

                while keyPressed(f"Left Click + {key}") and rcsAllow and status:

                    timeStart = time.time() if timeStart == 0 else timeStart

                    if time.time() < timeStart + (60 / 1000):
                        continue

                    rcsDownlimit = (downlimit / 5) * (1080 / height) * 1
                    varManager.rcs += (downspeed / 50) * (1080 / height) * 1

                    varManager.rcs = min(varManager.rcs, rcsDownlimit)

                    time.sleep(10 / 1000)

                varManager.rcs = 0

                time.sleep(0.005)
            except:
                pass

    @staticmethod
    def trigger():
        clicked = False
        while True:
            try:
                key = varManager.getVar("key", "TRIGGER")
                mode = varManager.getVar("mode", "TRIGGER")
                delay = int(varManager.getVar("shootdelay", "TRIGGER"))

                if mode == "Toggle" and keyPressed(key):
                    clicked = not clicked

                    if clicked:
                        beepSound(440, 75)
                        beepSound(700, 100)
                    else:
                        beepSound(440, 75)
                        beepSound(200, 100)

                    while keyPressed(key):
                        pass

                # Checking if either in "Toggle" mode and triggered, or in non-"Toggle" mode
                elif (((mode == "Toggle" and clicked) or mode == "Holding" and keyPressed(key))
                      and not any([keyPressed("W"), keyPressed("A"), keyPressed("S"), keyPressed("D")])):
                    enemy = luxFunctions.findEnemyTrigger()
                    if enemy:
                        lux.shoot()
                        time.sleep(200 * delay / 1000)

                time.sleep(0.005)
            except:
                pass

    @staticmethod
    def flicksilent():
        while True:
            try:
                key = varManager.getVar("key", "FLICKSILENT")
                mode = varManager.getVar("mode", "FLICKSILENT")

                if keyPressed(key):
                    enemy = luxFunctions.findEnemyFlick()
                    if enemy:
                        lux.move(enemy[0], enemy[1] + varManager.rcs)
                        time.sleep(0.01)
                        lux.shoot() if key != "Left Click" else ""
                        if mode == "Silentbot":
                            time.sleep(0.001)
                            lux.move(-enemy[0], -enemy[1] + varManager.rcs)

                        while keyPressed(key):
                            pass

                time.sleep(0.005)
            except:
                pass

    @staticmethod
    def instalock():
        seenMatches = []

        game = Client()
        game.activate()

        while True:
            try:
                status = json.loads(varManager.getVar("status", "INSTALOCK").lower())
                agent = varManager.getVar("agent", "INSTALOCK").lower()

                if status and game.activated:
                    sessionState = game.fetch_presence(game.puuid)['sessionLoopState']
                    if sessionState == "PREGAME":
                        matchID = game.pregame_fetch_match()['ID']
                        if matchID not in seenMatches:
                            if agent == "Random Agent":
                                agent = random.choice(Client.agents.keys())

                            game.pregame_select_character(Client.agents[agent])
                            game.pregame_lock_character(Client.agents[agent])
                            seenMatches.append(game.pregame_fetch_match()['ID'])

                            beepSound(440, 75)
                            beepSound(200, 100)

                time.sleep(0.005)
            except:
                pass

    @staticmethod
    def spin():
        upCounter = 0
        while True:
            try:
                key = varManager.getVar("spinbot", "CONFIGS")

                while keyPressed(key):
                    upCounter += 1
                    lux.move(1500, int((upCounter - (0 if upCounter < 40 else 39)) * 9) * (
                        -1 if upCounter < 40 else 1))
                    upCounter = 0 if upCounter > 80 else upCounter

                    time.sleep(0.005)

                time.sleep(0.005)
            except:
                pass

    def switchConfig(self):
        while True:
            try:
                switchConfigKey = list(
                    set([varManager.getVar("switchconfig1", "CONFIGS"), varManager.getVar("switchconfig2", "CONFIGS")]))

                def handleKeyPress(key, value):
                    if keyPressed(key):
                        widgets.configNumber.setCurrentText(value)
                        # self.overlay.update()
                        while keyPressed(key):
                            pass

                if len(switchConfigKey) == 2:
                    for numb, key in enumerate(switchConfigKey, start=1):
                        handleKeyPress(key, str(numb))
                else:
                    handleKeyPress(switchConfigKey[0], str("1" if varManager.configNumb == "2" else "2"))

                time.sleep(0.005)
            except:
                pass


class menuLoading(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_menuLoading()
        self.ui.setupUi(self)

        self.setWindowTitle(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16)))

        UIFunctions.visualDefinitions(self)
        UIFunctions.flagsLoading(self)

        self.show()

        QCoreApplication.processEvents()

        self.mainFunc()

    def mainFunc(self):
        global apiObj

        start = time.time()
        apiObj = api(version=versionNumb) if not objError else ""

        if time.time() - start < 1:
            time.sleep(random.randint(1, 2))

        self.licenseManager()

    def licenseManager(self):
        token = configManager.readFile("token")

        if token or objError:
            output = apiObj.license(token) if not objError else {"expiry": "Lifetime", "expiry_date": 0}

            if "expiry" in output:
                global expiry, expiryDate
                expiry = output["expiry"]
                expiryDate = output["expiry_date"]
                self.close()
                self.ui = menuMain()
            elif "hwid" in output:
                showErrorMessageBox("Error", "HWID doesn't match. Ask for key reset.")
            elif "keyauth" in output:
                showErrorMessageBox("Error", f"Unknown {output}")
            else:
                configManager.removeFile("token")

                self.switchToMenuLogin()
        else:
            self.switchToMenuLogin()

    def switchToMenuLogin(self):
        self.close()
        self.ui = menuLogin()


class menuLogin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_menuLogin()
        self.ui.setupUi(self)

        UIFunctions.defaultDefinitions(self)

        self.setWindowTitle(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16)))

        self.ui.signIn.clicked.connect(self.signIn)

        self.show()

    def signIn(self):
        token = self.ui.token.text()

        if token == "":
            return

        output = apiObj.license(token)

        if "invalid_token" in output:
            self.handleInvalid("invalid_token")
        elif "hwid" in output:
            self.handleInvalid("hwid")
        elif "expired" in output:
            self.handleInvalid("expired")
        elif "expiry" in output:
            self.handleValid(output)

    def handleInvalid(self, data):
        errorMessage = {
            "invalid_token": "Invalid token. Contact an admin if you believe it's an error.",
            "hwid": "HWID does not match. Request key reset.",
            "expired": "Renew your subscription to continue enjoying us!"
        }

        self.ui.token.clear()
        configManager.removeFile("token")
        showErrorMessageBox("Error", errorMessage[data], False)

    def handleValid(self, output):
        global expiry, expiryDate, window
        expiry = output["expiry"]
        expiryDate = output["expiry_date"]

        self.saveTokenToFile()

        self.close()
        self.ui = menuMain()

    def saveTokenToFile(self):
        token = self.ui.token.text()
        configManager.saveFile('token', token)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

        focused_widget = QApplication.focusWidget()
        if focused_widget:
            if isinstance(focused_widget, QLineEdit):
                if not focused_widget.geometry().contains(self.mapFromGlobal(event.globalPosition().toPoint())):
                    focused_widget.clearFocus()
        super().mousePressEvent(event)


class OverlayWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.oldWindow = ""
        self.streamproofstatus = ""

        self.timer = QTimer()
        self.timer.timeout.connect(self.checkActiveWindow)
        self.timer.start(100)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.screen_geometry = QGuiApplication.primaryScreen().geometry()
        self.setGeometry(self.screen_geometry)

    def checkActiveWindow(self):
        window_title = getWindowsTitle()
        if window_title != self.oldWindow:
            self.oldWindow = window_title
            self.update()

        streamproof_var = varManager.getVar("streamproof", "CONFIGS")
        if streamproof_var is not None:
            streamproof = json.loads(streamproof_var.lower())
            if self.streamproofstatus != streamproof:
                self.streamproofstatus = streamproof
                self.updateStreamProof(streamproof)

    def updateStreamProof(self, status):
        try:
            # Store current setup
            current_flags = self.windowFlags()
            current_attributes = self.testAttribute(Qt.WA_TranslucentBackground)

            # Reset flags and attributes
            self.setWindowFlags(Qt.Widget)
            self.setAttribute(Qt.WA_TranslucentBackground, False)

            # Call SetWindowDisplayAffinity
            if status:
                windll.user32.SetWindowDisplayAffinity(self.winId(), 0x11)
            else:
                windll.user32.SetWindowDisplayAffinity(self.winId(), 0x0)

            # Restore previous setup
            self.setWindowFlags(current_flags)
            self.setAttribute(Qt.WA_TranslucentBackground, current_attributes)

            self.update()
            self.show()
        except:
            pass

    def drawRectangle(self, painter, fovx, fovy, color):
        pen = QPen(QColor(*color))
        painter.setPen(pen)
        rect_top_left = QPoint((self.screen_geometry.width() - fovx) // 2,
                               (self.screen_geometry.height() - fovy) // 2)
        rect = QRect(rect_top_left, QSize(fovx, fovy))
        painter.drawRect(rect)

    def paintEvent(self, event):
        try:
            window_title = getWindowsTitle()
            if window_title.replace(" ", "") != "VALORANT":
                return

            painter = QPainter(self)
            pen = QPen()
            pen.setColor(QColor(255, 255, 255))
            painter.setPen(pen)
            painter.setFont(QFont('Arial', 10))

            baseX = int(varManager.getVar("menuposx", "VISUAL") or 0) + 30
            baseY = int(varManager.getVar("menuposy", "VISUAL") or 0) + 30
            vertical_spacing = 30

            # Draw Title
            painter.drawText(baseX, baseY, f"[LUX VALORANT] - CFG {varManager.configNumb}")
            baseY += vertical_spacing

            features = [
                {
                    "name": "Aim",
                    "drawfov": json.loads((varManager.getVar("drawfovaim", "VISUAL") or "False").lower()),
                    "key": varManager.getVar("key", "AIM" + varManager.configNumb) or "",
                    "fovx": int(varManager.getVar("fovx", "AIM" + varManager.configNumb) or 0) * 2,
                    "fovy": int(varManager.getVar("fovy", "AIM" + varManager.configNumb) or 0) * 2,
                    "color": (255, 255, 255),
                },
            ]

            for feature in features:
                if feature['drawfov']:
                    self.drawRectangle(painter, feature['fovx'], feature['fovy'], feature['color'])

                    if feature['key']:
                        painter.drawText(baseX, baseY, f"{feature['name']} Key: {feature['key']}")
                        baseY += vertical_spacing

            drawfovAim = json.loads((varManager.getVar("drawfovaim", "VISUAL") or "False").lower())
            if drawfovAim:
                statusRcs = json.loads(varManager.getVar("rcsenable", "AIM" + varManager.configNumb).lower())
                if statusRcs:
                    painter.drawText(baseX, baseY, f"RCS: {statusRcs}")
                    baseY += vertical_spacing

            drawfovFlick = json.loads((varManager.getVar("drawfovflick", "VISUAL") or "False").lower())
            if drawfovFlick:
                keyFlick = varManager.getVar("keyflick", "FLICKSILENT")
                if keyFlick != "":
                    painter.drawText(baseX, baseY, f"Flick & Silent Key: {keyFlick}")
                    baseY += vertical_spacing

                fovx = int(varManager.getVar("fovx", "FLICKSILENT")) * 2
                fovy = int(varManager.getVar("fovy", "FLICKSILENT")) * 2

                # Drawing the rectangle for drawfovFlick
                self.drawRectangle(painter, fovx, fovy, (0, 0, 50))  # Assuming color is (0, 0, 0)

            # Adding new code blocks here
            drawInstalock = json.loads((varManager.getVar("drawinstalock", "VISUAL") or "False").lower())
            if drawInstalock:
                statusInstalock = json.loads(varManager.getVar("status", "INSTALOCK").lower())
                agent = varManager.getVar("agent", "INSTALOCK").lower()
                if statusInstalock:
                    pen.setColor(QColor(255, 255, 255))
                    painter.setPen(pen)
                    painter.drawText(baseX, baseY, f"Instalock Agent: {agent.capitalize()}")
                    baseY += vertical_spacing

        except Exception as e:
            print(e)
            pass


class menuMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("Chrome_WidgetWin_1")

        #############
        # TRAY ICON #
        #############

        appIcon = os.path.join(sys._MEIPASS if getattr(sys, '_MEIPASS', None) else './data', 'icon.ico')
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(appIcon))

        self.tray_icon.activated.connect(self.on_tray_icon_activated)

        tray_menu = QMenu()
        quit_action = QAction("Exit", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        ###########
        ###########

        self.ui = Ui_menuMain()
        self.ui.setupUi(self)

        configManager.loadConfig()

        global widgets
        widgets = self.ui

        UIFunctions.defaultDefinitions(self)

        windowTitle = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(16))
        self.setWindowTitle(windowTitle)

        # DEFAULT PAGE
        widgets.stackedWidget.setCurrentWidget(widgets.aimPage)
        widgets.btn_aim.setStyleSheet(UIFunctions.selectMenu(widgets.btn_aim.styleSheet()))

        ###########
        # BUTTONS #
        ###########

        # EXTEND
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # PAGE
        widgets.btn_aim.clicked.connect(self.changePage)
        widgets.btn_trigger.clicked.connect(self.changePage)
        widgets.btn_flicksilent.clicked.connect(self.changePage)
        widgets.btn_instalock.clicked.connect(self.changePage)
        widgets.btn_shortcuts.clicked.connect(self.changePage)
        # widgets.btn_visual.clicked.connect(self.changePage)

        # SLIDEBARS
        widgets.smooth.valueChanged.connect(self.slideBarChanged)
        widgets.aimHeadpos.valueChanged.connect(self.slideBarChanged)
        widgets.downspeed.valueChanged.connect(self.slideBarChanged)
        widgets.downlimit.valueChanged.connect(self.slideBarChanged)
        widgets.triggerShootdelay.valueChanged.connect(self.slideBarChanged)
        widgets.flicksilentHeadpos.valueChanged.connect(self.slideBarChanged)
        widgets.menuposx.valueChanged.connect(self.slideBarChanged)
        widgets.menuposy.valueChanged.connect(self.slideBarChanged)

        # AIM
        widgets.aimKey.currentTextChanged.connect(self.updateSettings)
        widgets.configNumber.currentTextChanged.connect(self.changeConfig)
        widgets.smooth.valueChanged.connect(self.updateSettings)
        widgets.aimFovx.valueChanged.connect(self.updateSettings)
        widgets.aimFovy.valueChanged.connect(self.updateSettings)
        widgets.aimHeadpos.valueChanged.connect(self.updateSettings)
        # RCS
        widgets.rcsenable.clicked.connect(self.updateSettings)
        widgets.downspeed.valueChanged.connect(self.updateSettings)
        widgets.downlimit.valueChanged.connect(self.updateSettings)

        # TRIGGER
        widgets.triggerKey.currentTextChanged.connect(self.updateSettings)
        widgets.triggerFovx.valueChanged.connect(self.updateSettings)
        widgets.triggerFovy.valueChanged.connect(self.updateSettings)
        widgets.triggerShootdelay.valueChanged.connect(self.updateSettings)
        widgets.triggerMode.currentTextChanged.connect(self.updateSettings)

        # FLICKSILENT
        widgets.flicksilentKey.currentTextChanged.connect(self.updateSettings)
        widgets.flicksilentMode.currentTextChanged.connect(self.updateSettings)
        widgets.flicksilentFovx.valueChanged.connect(self.updateSettings)
        widgets.flicksilentFovy.valueChanged.connect(self.updateSettings)
        widgets.flicksilentHeadpos.valueChanged.connect(self.updateSettings)

        # INSTALOCK
        widgets.instalockStatus.clicked.connect(self.updateSettings)
        widgets.instalockAgent.currentTextChanged.connect(self.updateSettings)

        # SHORTCUTS
        widgets.streamproof.clicked.connect(self.updateSettings)
        widgets.switchconfig1.currentTextChanged.connect(self.updateSettings)
        widgets.switchconfig2.currentTextChanged.connect(self.updateSettings)
        widgets.spinbot.currentTextChanged.connect(self.updateSettings)
        widgets.disablercs.currentTextChanged.connect(self.updateSettings)
        widgets.color.currentTextChanged.connect(self.updateSettings)
        widgets.mousesens.valueChanged.connect(self.updateSettings)

        # VISUALS
        widgets.sproof.clicked.connect(self.updateSettings)
        widgets.drawinstalock.clicked.connect(self.updateSettings)
        widgets.drawfovflick.clicked.connect(self.updateSettings)
        widgets.drawfovaim.clicked.connect(self.updateSettings)
        widgets.menuposx.valueChanged.connect(self.updateSettings)
        widgets.menuposy.valueChanged.connect(self.updateSettings)

        ###########
        ###########

        self.setConfig()

        global lux
        lux = mainFunction()

        streamProof = 0x11 if eval(varManager.getVar('streamproof', 'CONFIGS')) else 0x0

        lux.streamproof(self.winId(), streamProof)

        self.show()

        w, h = getScreenResolution()
        widgets.menuposx.setMaximum(w * 0.715)
        widgets.menuposy.setMaximum(h * 0.7)

        # self.overlay = OverlayWindow()
        # self.overlay.show()

        self.funcstarter()

        # Spoof the window class name and flags
        self.spoof_window_class()

        ######################################

    def funcstarter(self):
        # self.funcstart = functionStarter(self.overlay)
        self.funcstart = functionStarter()
        self.funcstart.start()

    def spoof_window_class(self):
        # Get the window handle
        hwnd = self.winId()

        # Define the new class name
        new_class_name = "Chrome_WidgetWin_1"

        # Set the new class name to the window
        GCL_CLASSNAME = -32
        ctypes.windll.user32.SetClassLongPtrW.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.LPCWSTR]
        ctypes.windll.user32.SetClassLongPtrW.restype = wintypes.LPVOID

        result = ctypes.windll.user32.SetClassLongPtrW(hwnd, GCL_CLASSNAME, new_class_name)

        """
        if result == 0:
            print(f"Failed to set new class name. Error code: {ctypes.get_last_error()}")
        else:
            print(f"Set window class name to '{new_class_name}'")
        """

        # Set the class style
        GCL_STYLE = -26
        new_style = 8  # The style value you provided
        ctypes.windll.user32.SetClassLongPtrW.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.UINT]

        result = ctypes.windll.user32.SetClassLongPtrW(hwnd, GCL_STYLE, new_style)

        """
        if result == 0:
            print(f"Failed to set new class style. Error code: {ctypes.get_last_error()}")
        else:
            print(f"Set window class style to {new_style}")
    
        # Print the new window class information
        print(f"New window class name: {new_class_name}")
        print(f"New window class style: {new_style}")
        """

    def setConfig(self, changeConfig=False):
        varManager.settingConfig = True
        allVars = varManager.getAllVars()
        for varPages in allVars:
            varList = allVars[varPages]

            if "AIM" in varPages and "AIM" + str(
                    varManager.configNumb) != varPages or changeConfig and "AIM" not in varPages:
                continue
            elif "AIM" + str(varManager.configNumb) == varPages:
                varPages = "aim"
            elif varPages == "CONFIGS":
                varPages = ""
            else:
                varPages = varPages.lower()

            for varName in varList:
                widgetsObj = self.getWidgetsWithFallback(varName, varPages)

                if widgetsObj is None:
                    continue

                widgetsType = type(widgetsObj)

                value = varList[varName]
                if widgetsType in [QSpinBox, QSlider]:
                    widgetsObj.setValue(int(value))
                elif widgetsType == QDoubleSpinBox:
                    widgetsObj.setValue(float(value))
                elif widgetsType == QComboBox:
                    widgetsObj.setCurrentText(value)
                elif widgetsType == QRadioButton:
                    widgetsObj.setChecked(eval(value, {'__builtins__': None}, {}))

        varManager.settingConfig = False

    def changeConfig(self):
        varManager.configNumb = self.sender().currentText()
        for i in range(int(varManager.configNumb)):
            beepSound(700, 120)
        self.setConfig(True)

    def updateSettings(self, value):
        if varManager.settingConfig:
            return

        page = widgets.stackedWidget.currentWidget().objectName().upper().replace("PAGE", "")
        varName = self.sender().objectName().replace(page.lower(), "").lower()
        if page == "AIM":
            page += varManager.configNumb

        # WHEN STREAMODE IS CHANGE
        if varName == "streamproof":
            streamProof = 0x11 if value else 0x0
            lux.streamproof(self.winId(), streamProof)

        configManager.saveVariable(page, varName, value)

        # self.overlay.update()

    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:  # This handles single left-click
            if self.isVisible():
                self.hide()
            else:
                self.show()
                self.raise_()
                self.activateWindow()

    @staticmethod
    def getWidgets(name):
        if hasattr(widgets, name):
            return getattr(widgets, name)
        else:
            return None

    def getWidgetsWithFallback(self, varName, varPages):
        names_to_try = [varPages + varName.capitalize(), varName]
        for name in names_to_try:
            widgetsObj = self.getWidgets(name)
            if widgetsObj is not None:
                return widgetsObj
        return None

    def slideBarChanged(self, value):
        sliderValue = {
            "smooth": widgets.smoothValue,
            "aimHeadpos": widgets.aimHeadposValue,
            "downspeed": widgets.downspeedValue,
            "downlimit": widgets.downlimitValue,
            "triggerShootdelay": widgets.triggerShootdelayValue,
            "flicksilentHeadpos": widgets.flicksilentHeadposValue,
            "menuposx": widgets.menuPosXValue,
            "menuposy": widgets.menuPosYValue
        }

        slideBar = self.sender().objectName()
        sliderValue[slideBar].setText(str(value))

    def changePage(self):
        pages = {
            "btn_aim": widgets.aimPage,
            "btn_trigger": widgets.triggerPage,
            "btn_flicksilent": widgets.flicksilentPage,
            "btn_instalock": widgets.instalockPage,
            "btn_shortcuts": widgets.configsPage,
            "btn_visual": widgets.visualPage
        }

        btn = self.sender()
        btnName = btn.objectName()
        widgets.stackedWidget.setCurrentWidget(pages[btnName])
        UIFunctions.resetStyle(self, btnName)
        btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

        focused_widget = QApplication.focusWidget()
        if focused_widget:
            if isinstance(focused_widget, QLineEdit) or isinstance(focused_widget, QSpinBox):
                if not focused_widget.geometry().contains(self.mapFromGlobal(event.globalPosition().toPoint())):
                    focused_widget.clearFocus()
        super().mousePressEvent(event)


if __name__ == "__main__":
    if not isAdmin() and hasattr(sys, "_MEIPASS"):
        windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        os._exit(1)

    # if not checkInternetConnection():
    #     showErrorMessageBox("Error", "No internet connection.")

    global app
    app = QApplication(sys.argv)

    appIcon = os.path.join(sys._MEIPASS if getattr(sys, '_MEIPASS', None) else './data', 'icon.ico')
    app.setWindowIcon(QIcon(appIcon))

    menuLoading()

    sys.exit(app.exec())
