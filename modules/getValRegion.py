import os
import time


def getValorantRegion():
    logFilePath = os.path.expandvars("%LocalAppData%\\VALORANT\\Saved\\Logs\\ShooterGame.log")
    regionLineStart = "/config/"

    while not os.path.isfile(logFilePath) or not os.access(logFilePath, os.R_OK):
        # Wait for the log file to be found and readable
        time.sleep(1)

    with open(logFilePath, "r", encoding="utf8") as logFile:
        return next((line[line.find(regionLineStart) + len(regionLineStart):].split("/")[0].split("]")[0] for line in logFile if regionLineStart in line), None)


print(getValorantRegion())