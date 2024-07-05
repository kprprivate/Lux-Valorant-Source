from winsound import Beep


def beepSound(mhz, long):
    try:
        Beep(mhz, long)
    except:
        pass
