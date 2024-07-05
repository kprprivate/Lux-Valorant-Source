import win32api
import os


def showErrorMessageBox(title, message, exit=True):
    win32api.MessageBox(0, message, title, 0x00000010)
    if exit:
        os._exit(1)
