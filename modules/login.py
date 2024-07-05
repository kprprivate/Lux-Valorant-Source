import os
from PySide6.QtWidgets import QApplication
from MainWindow import MainWindow
from LoginWindow import LoginWindow


class LicenseManager:
    def __init__(self):
        try:
            window, hwnd = self.processLicense()
        except ValueError as error:
            print(f"Error: {str(error)}")
            return

        self.app.window = window
        self.app.exec()

    def readLicenseFile(self):
        if os.path.isfile('license.ini'):
            with open("license.ini", "r") as file:
                return file.read()
        return None

    def processLicense(self):
        token = self.readLicenseFile()

        if token:
            output = apiObj.license(token) if not objError else {"expiry": "Lifetime", "expiry_date": 0}

            if "expiry" in output:
                VENCIMENTO = output["expiry"]
                VENCIMENTO_DATE = output["expiry_date"]

                window = MainWindow()
                hwnd = int(window.winId())
                return hwnd,

            elif "hwid" in output:
                raise ValueError("HWID doesn't match. Ask for key reset.")
            elif "keyauth" in output:
                raise ValueError(f"Unknown error: {output}")
            else:
                os.remove('license.ini')
                return LoginWindow(), None
        else:
            return LoginWindow(), None


if __name__ == "__main__":
    manager = LicenseManager()
