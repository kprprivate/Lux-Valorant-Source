from . import *

import time
import ctypes
import os
import sys

import win32file
import win32con

import shutil
import subprocess


class MOUSE_MOVE_DATA(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long),
                ("button_flags", ctypes.c_ushort)]


class STREAMODE(ctypes.Structure):
    _fields_ = [("hwnd", ctypes.c_uint32),
                ("value", ctypes.c_uint64)]

class mainFunction:
    def __init__(self):
        self.hardware = None

        # Define the IOCTL code. Adjust the values according to your driver's definition.
        self.CTL_CODE = lambda DeviceType, Func, Meth, Access: ((DeviceType) << 16) | ((Access) << 14) | (
                (Func) << 2) | (
                                                                   Meth)
        self.IOCTL_MOVE_MOUSE = self.CTL_CODE(0x00000022, 0x1, 0, 0)
        self.IOCTL_STREAM_MODE = self.CTL_CODE(0x00000022, 0x2, 0, 0)

        self.findHardware()

    def deactivate(self):
        self.hardware = None
        return

    def run_command(self, command):
        return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)

    def findHardware(self):
        service_name = 'mydriver'
        driver_path = rf'C:\Windows\System32\drivers\{service_name}.sys'

        if not os.path.exists(driver_path):
            currentDir = sys._MEIPASS if getattr(sys, '_MEIPASS', None) else 'data'
            driver = os.path.join(currentDir, 'mydriver.sys')

            try:
                shutil.move(driver, driver_path)
            except Exception:
                showErrorMessageBox("Driver", "Error loading the driver #1")

        query_result = self.run_command(f"sc query {service_name}")

        # Checking if the service exists
        if "1060" in query_result.stdout:
            self.run_command(f"sc create {service_name} binPath= {driver_path} type= kernel")
            self.run_command(f"sc start {service_name}")

        # Checking if the service is not running
        elif "STOPPED" in query_result.stdout:
            self.run_command(f"sc start {service_name}")

        try:
            self.hardware = win32file.CreateFile(f"\\\\.\\{service_name}",
                                                 win32con.GENERIC_READ | win32con.GENERIC_WRITE,
                                                 0,
                                                 None,
                                                 win32con.OPEN_EXISTING,
                                                 0,
                                                 None)
        except:
            showErrorMessageBox("Driver", "Error loading the driver")

        beepSound(400, 75)

    def streamproof(self, hwnd, value):
        streamModeData = STREAMODE(hwnd, value)

        win32file.DeviceIoControl(self.hardware, self.IOCTL_STREAM_MODE, streamModeData, None, None)

    def move(self, x, y, click=0):
        x, y, click = int(x), int(y), int(click)
        try:
            mouseData = MOUSE_MOVE_DATA(x, y, click)

            win32file.DeviceIoControl(self.hardware, self.IOCTL_MOVE_MOUSE, mouseData, None, None)

            if click != 0:
                self.shoot()

        except Exception as e:
            print(f"Error in move method: {e}")

    def shoot(self):
        win32file.DeviceIoControl(self.hardware,
                                  self.IOCTL_MOVE_MOUSE,
                                  MOUSE_MOVE_DATA(0, 0, 0x1),
                                  None,
                                  None)

        time.sleep(0.001)

        win32file.DeviceIoControl(self.hardware,
                                  self.IOCTL_MOVE_MOUSE,
                                  MOUSE_MOVE_DATA(0, 0, 0x2),
                                  None,
                                  None)
