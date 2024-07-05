import wmi
import getpass
import win32api
import base64


def getHWID():
    # initialize WMI object
    c = wmi.WMI()

    motherboard_id,cpu_id, username, volume_id = "", "", "", ""

    try:
        # retrieve motherboard serial number
        for board in c.Win32_BaseBoard():
            motherboard_id = board.SerialNumber.strip()
    except:
        pass

    # retrieve processor ID
    try:
        for proc in c.Win32_Processor():
            cpu_id = proc.ProcessorId.strip()
    except:
        pass

    try:
        # retrieve current username
        username = getpass.getuser()
    except:
        pass

    try:
        # retrieve volume ID of C:/ drive
        volume_id = win32api.GetVolumeInformation("C:\\")[1]
    except:
        pass

    # concatenate and return IDs
    ids = f"{motherboard_id}{cpu_id}{username}{volume_id}"

    # encode IDs using Base64 encoding
    encoded = base64.b64encode(ids.encode("utf-8")).decode("utf-8")
    return encoded
