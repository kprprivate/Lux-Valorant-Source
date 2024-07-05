import subprocess


def checkInternetConnection():
    try:
        subprocess.check_output(["ping", "8.8.8.8", "-n", "1"])
        return True
    except subprocess.CalledProcessError:
        return False
