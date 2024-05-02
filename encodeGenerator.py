import cv2
import face_recognition
import pickle
import os

# Importing Student Images into a List
imgBackground = cv2.imread("Resources/background.png")

folderModepath = "Images"
pathList = os.listdir(folderModepath)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderModepath, path)))
    studentIds.append(path.split(".")[0])

print(len(imgList))
print(studentIds)

def findEncodings(imageList):
    encodeList = []

    for image in imageList:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(image)[0]
        encodeList.append(encode)
    
    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownDict = dict(zip(studentIds, encodeListKnown))
print(encodeListKnown)
print("Encoding Completed...")

file= open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownDict, file)
file.close()
print("Encoding File Saved...")