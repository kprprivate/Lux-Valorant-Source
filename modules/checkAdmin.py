import os
from ctypes import windll

def isAdmin():
    try:
        isAdmin = (os.getuid() == 0)
    except AttributeError:
        isAdmin = windll.shell32.IsUserAnAdmin() != 0
    return isAdmin
