from . import *
import configparser


class configManager:
    def __init__(self, configFile):
        self.configFile = configFile

    @staticmethod
    def configPath():
        path = os.path.join(os.path.expanduser('~'), "my3isthebest", "config")

        if not os.path.isfile(path):
            configManager.defaultConfig()

        return path

    @staticmethod
    def readConfig():
        config = configparser.ConfigParser()
        config.read(configManager.configPath())
        return config

    @staticmethod
    def loadConfig():
        config = configManager.readConfig()

        try:
            for section in config.sections():
                for name, value in config[section].items():
                    varManager.setVar(name, value, section)
        except configparser.Error:
            configManager.defaultConfig()

    @staticmethod
    def saveVariable(section, name, value):
        value = str(value)
        config = configManager.readConfig()
        try:
            config.set(section, name, value)
        except:
            config.add_section(section)
            config.set(section, name, value)
        config.write(open(configManager.configPath(), "w+"))
        varManager.setVar(name, value, section)

    @staticmethod
    def defaultConfig():
        ip = varManager.getVar("ip", "GENERAL") or 0

        configFile = f"""
            [GENERAL]
            ip = {ip}
            
            [AIM1]
            key = Left Click
            rcsenable = True
            downspeed = 20
            downlimit = 100
            smooth = 24
            fovx = 40
            fovy = 30
            headpos = 2
            
            [AIM2]
            key = Mouse 4
            smooth = 24
            fovx = 40
            fovy = 30
            headpos = 1
            rcsenable = False
            downspeed = 20
            downlimit = 100
            
            [TRIGGER]
            key = ALT
            fovx = 6
            fovy = 4
            shootdelay = 1
            mode = Holding
            
            [FLICKSILENT]
            key = Middle Click
            mode = Silentbot
            fovx = 50
            fovy = 30
            headpos = 1
            
            [INSTALOCK]
            status = True
            agent = Phoenix
            
            [CONFIGS]
            streamproof = False
            switchconfig1 = F1
            switchconfig2 = F1
            spinbot = Arrow Up
            disablercs = 
            color = Purple
            mousesens = 0.6
            
            [VISUAL]
            sproof = False
            drawfovaim = True
            drawfovflick = False
            drawinstalock = True
            menuposy = 0
            menuposx = 0
            """

        configManager.saveFile('config', configFile)
        configManager.loadConfig()
        return

    @staticmethod
    def saveFile(file, content):
        dirPath = os.path.join(os.path.expanduser('~'), "my3isthebest")
        os.makedirs(dirPath, exist_ok=True)
        open(os.path.join(dirPath, file), 'w+', encoding="utf-8").write(content)
        return

    @staticmethod
    def removeFile(file):
        dirPath = os.path.join(os.path.expanduser('~'), "my3isthebest", file)
        if os.path.isfile(dirPath):
            os.remove(os.path.join(dirPath))
        return

    @staticmethod
    def readFile(file):
        dirPath = os.path.join(os.path.expanduser('~'), "my3isthebest", file)
        if os.path.isfile(dirPath):
            return open(dirPath, "r").read()
        return None
