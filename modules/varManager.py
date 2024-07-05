import secrets
import base64


class varManager:
    rcs = 0

    baseColor = {
        "Purple": [(250, 100, 250), (250, 100, 250)],
        "Yellow": [(250, 250, 50), (250, 250, 50)],
        "Red": [(250, 0, 0), (250, 0, 0)],
    }

    baseColorCv = {
        "Purple": [[130, 60, 200], [150, 255, 255], [140, 100, 130], [170, 190, 255]],
        "Yellow": [[20, 190, 240], [30, 255, 255], [20, 150, 240], [30, 255, 255]],
        "Red": [[0, 205, 170], [5, 255, 255], [0, 205, 120], [5, 255, 255]] ,
    }

    setttingConfig = False
    configNumb = "1"
    vars = {
        "GENERAL": {},
        "AIM1": {},
        "AIM2": {},
        "TRIGGER": {},
        "FLICKSILENT": {},
        "INSTALOCK": {},
        "CONFIGS": {},
        "VISUAL": {}
    }
    key = secrets.token_hex(16)

    @staticmethod
    def encrypt(data):
        keyBytes = bytes.fromhex(varManager.key)
        dataString = str(data)
        dataBytes = dataString.encode('utf-8')
        encryptedBytes = bytes(c ^ keyBytes[i % len(keyBytes)] for i, c in enumerate(dataBytes))
        encryptedData = base64.b64encode(encryptedBytes).decode('utf-8')
        return encryptedData

    @staticmethod
    def decrypt(encryptedData):
        keyBytes = bytes.fromhex(varManager.key)
        encryptedBytes = base64.b64decode(encryptedData)
        decryptedBytes = bytes(c ^ keyBytes[i % len(keyBytes)] for i, c in enumerate(encryptedBytes))
        decryptedData = decryptedBytes.decode('utf-8')
        return decryptedData

    @staticmethod
    def setVar(name, value, section=None):
        encrypted_value = varManager.encrypt(value)
        if section:
            varManager.vars[section][name] = encrypted_value
        else:
            varManager.vars[name] = encrypted_value

    @staticmethod
    def getVar(name, section=None):
        if section:
            encryptedValue = varManager.vars.get(section, {}).get(name)
        else:
            encryptedValue = varManager.vars.get(name)

        if encryptedValue is not None:
            return varManager.decrypt(encryptedValue)
        else:
            return None

    @staticmethod
    def getAllVars():
        decryptedVars = {}
        for name, encryptedValue in varManager.vars.items():
            if name == "GENERAL":
                continue
            if isinstance(encryptedValue, dict):
                decryptedVars[name] = {key: varManager.decrypt(value) if isinstance(value, str) else value for
                                       key, value in encryptedValue.items()}
            else:
                decryptedVars[name] = varManager.decrypt(encryptedValue) if isinstance(encryptedValue,
                                                                                       str) else encryptedValue
        return decryptedVars

    @staticmethod
    def delVar(name, section):
        if name in varManager.vars:
            if section:
                del varManager.vars[section][name]
            else:
                del varManager.vars[name]
