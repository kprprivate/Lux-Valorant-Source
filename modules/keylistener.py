from ctypes import windll
import win32api
import win32con

vkKey = {"leftclick": "VK_LBUTTON",
         "rightclick": "VK_RBUTTON",
         "middleclick": "VK_MBUTTON",
         "mouse4": "VK_XBUTTON2",
         "mouse5": "VK_XBUTTON1",
         "esc": "VK_ESCAPE",
         "capslock": "0x14",
         "tab": "0x09",
         "shift": "0x10",
         "ctrl": "0x11",
         "alt": "0x12",
         "space": "0x20",
         "arrowleft": "0x25",
         "arrowup": "0x26",
         "arrowright": "0x27",
         "arrowdown": "0x28",
         "f12": "0x7B",
         "f11": "0x7A",
         "f10": "0x79",
         "f1": "0x70",
         "f2": "0x71",
         "f3": "0x72",
         "f4": "0x73",
         "f5": "0x74",
         "f6": "0x75",
         "f7": "0x76",
         "f8": "0x77",
         "f9": "0x78"}


def vkCode(c):
    return windll.User32.VkKeyScanW(ord(c)) & 0xFF


def keyPressed(keys):
    try:
        if keys == "":
            return False

        # Pre-process keys
        keys = list(set(keys.replace(' ', '').lower().split('+')))

        # Count of pressed keys
        pressedCount = 0

        for key in keys:
            key = vkCode(key) if len(key) == 1 else key

            if key in vkKey:
                key = vkKey[key]

            # Convert hex to decimal
            if isinstance(key, str) and '0x' in key.lower():
                key = int(key, 16)
            # Convert win32con constant string to value
            elif isinstance(key, str) and hasattr(win32con, key):
                key = getattr(win32con, key)

            # Validate key is now an integer
            if not isinstance(key, int):
                raise ValueError(f"Invalid key: {key}")

            if win32api.GetKeyState(key) < 0:
                pressedCount += 1

        return pressedCount == len(keys)

    except Exception as e:
        #print(f"Exception in keyPressed: {e}")
        return False
