from win32api import EnumDisplaySettings, EnumDisplayMonitors


def getScreenResolution():
    mode = EnumDisplaySettings(None, -1)
    return mode.PelsWidth, mode.PelsHeight