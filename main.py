import cv2
import os
import pickle

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


# Importing Mode Images into a List
imgBackground = cv2.imread("Resources/background.png")

folderModepath = "Resources/Modes"
modePathList = os.listdir(folderModepath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModepath, path)))

print(len(imgModeList))



while True:
    success, img =cap.read()

    imgBackground[162:162+480,55:55+640] = img
    imgBackground[44:44 + 633, 808:808+414] = imgModeList[3]

    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
