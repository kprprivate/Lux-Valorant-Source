from . import *

import PIL.ImageGrab
import PIL.Image
import mss
import cv2
import numpy as np

class luxFunctions:
    @staticmethod
    def getScreen(width, height, fovX, fovY, rcsValue=0, numpy=True):
        with mss.mss() as sct:
            bbox = (
                int((width / 2) - fovX),
                int(((height - rcsValue) / 2) - fovY),
                int((width / 2) + fovX),
                int(((height - rcsValue) / 2) + fovY)
            )
            img = sct.grab(bbox)

            if numpy:
                return np.array(img)
            else:
                PIL.Image.frombytes('RGB', img.size, img.bgra, 'raw', 'BGRX')

    @staticmethod
    def findEnemyAim():
        fovx = int(varManager.getVar("fovx", "AIM" + varManager.configNumb))
        fovy = int(varManager.getVar("fovy", "AIM" + varManager.configNumb))
        smooth = float(varManager.getVar("smooth", "AIM" + varManager.configNumb))
        headpos = int(varManager.getVar("headpos", "AIM" + varManager.configNumb))
        mousesens = float(varManager.getVar("mousesens", "CONFIGS"))

        color = varManager.getVar("color", "CONFIGS")
        baseColor = varManager.baseColorCv

        width, height = getScreenResolution()

        image = luxFunctions.getScreen(width, height, fovx, fovy, varManager.rcs + headpos)

        try:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            lower = np.array(baseColor[color][0])
            upper = np.array(baseColor[color][1])

            mask = cv2.inRange(hsv, lower, upper)

            edged = cv2.Canny(mask, 30, 200)
            contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            if len(contours) != 0:
                ref_point = np.array([fovx, fovy])  # Reference point at the center of your FOV

                nearest_contour = None
                nearest_distance = float('inf')  # Initialize with a large value

                for contour in contours:
                    M = cv2.moments(contour)
                    if M["m00"] != 0:  # Avoid division by zero
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                    else:
                        cX, cY = 0, 0  # or whatever fallback you want

                    contour_center = np.array([cX, cY])
                    distance = np.linalg.norm(ref_point - contour_center)  # Euclidean distance

                    if distance < nearest_distance:
                        nearest_distance = distance
                        nearest_contour = contour

                # Assuming you want to use the top-most point of the nearest contour
                if nearest_contour is not None:
                    y = float('inf')  # Initialize with a large value
                    x = float('inf')  # Initialize with a large value

                    for point in nearest_contour:
                        posx, posy = point.ravel()  # Flattens the array before accessing its elements

                        if posy < y:
                            y = posy
                            x = posx

                sensitivityX = (1.07437623 * pow(mousesens, -0.9936827126)) * (1920 / width) * 6
                sensitivityY = (1.07437623 * pow(mousesens, -0.9936827126)) * (1080 / height) * 6

                return ((x - fovx) / smooth) * sensitivityX, \
                       (((y - fovy) / smooth) * sensitivityY) + headpos
        except:
            pass

        return None

    @staticmethod
    def findEnemyTrigger():
        fovx = int(varManager.getVar("fovx", "TRIGGER"))
        fovy = int(varManager.getVar("fovy", "TRIGGER"))

        color = varManager.getVar("color", "CONFIGS")
        baseColor = varManager.baseColorCv

        width, height = getScreenResolution()

        image = luxFunctions.getScreen(width, height, fovx, fovy)

        try:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            lower = np.array(baseColor[color][0])
            upper = np.array(baseColor[color][1])

            mask = cv2.inRange(hsv, lower, upper)

            if np.any(mask):
                return True
        except:
            pass

        return None

    @staticmethod
    def findEnemyFlick():
        fovx = int(varManager.getVar("fovx", "FLICKSILENT"))
        fovy = int(varManager.getVar("fovy", "FLICKSILENT"))
        headpos = int(varManager.getVar("headpos", "FLICKSILENT"))
        mousesens = float(varManager.getVar("mousesens", "CONFIGS"))

        color = varManager.getVar("color", "CONFIGS")
        baseColor = varManager.baseColorCv

        width, height = getScreenResolution()

        image = luxFunctions.getScreen(width, height, fovx, fovy, 2 + headpos)

        try:
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            lower = np.array(baseColor[color][0])
            upper = np.array(baseColor[color][1])

            mask = cv2.inRange(hsv, lower, upper)

            edged = cv2.Canny(mask, 30, 200)
            contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

            if len(contours) != 0:
                y = float('inf')  # Initialize with a large value
                x = float('inf')  # Initialize with a large value

                for contour in contours:
                    for point in contour:
                        posx, posy = point[0]

                        if posy < y:
                            y = posy
                            x = posx

                sensitivityX = (1.07437623 * pow(mousesens, -0.9936827126)) * (1920 / width)
                sensitivityY = (1.07437623 * pow(mousesens, -0.9936827126)) * (1080 / height)

                return (x - fovx) * sensitivityX, \
                       ((y - fovy) * sensitivityY) + 2 + headpos
        except:
            pass

        return None