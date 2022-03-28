import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
# Import some Libraries


cap = cv2.VideoCapture("eyeblink.mp4")
detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640,360,[0,40],invert=True)

eyepointList = [22, 23, 24, 110, 157, 158, 159, 160, 161, 130, 243]
ratiolist = []
blink_count = 0
counter = 0
want_color = (100,250,0)

while True:

    if cap.get(cv2.CAP_PROP_FRAME_WIDTH) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    #
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw= False)

    if faces:
        face = faces[0]
        for id in eyepointList:
            cv2.circle(img,face[id],5, (255,0,255), cv2.FILLED)

        leftup = face[159]
        leftdown = face[23]
        leftRight = face[130]
        leftLeft = face[243]

        len_Ver, _ = detector.findDistance(leftup, leftdown)
        len_Hor, _ = detector.findDistance(leftLeft, leftRight)

        cv2.line(img,leftup,leftdown, want_color,3)
        cv2.line(img,leftLeft,leftRight, want_color,3)

        eye_ratio = int((len_Ver/len_Hor) * 100)
        ratiolist.append(eye_ratio)
        if len(ratiolist) > 3:
            ratiolist.pop(0)
        ratioAvg = sum(ratiolist)/len(ratiolist)

        if ratioAvg < 35 and counter ==0 :
            blink_count +=1
            counter = 1
        if counter != 0:
            counter +=1
            if counter > 10:
                counter = 0
        cvzone.putTextRect(img,f'Blink times : {blink_count}',(50,100))
        imgPlot = plotY.update(ratioAvg)

        img = cv2.resize(img, (640, 360))
        imgstack = cvzone.stackImages([img, imgPlot],1,1)

    else:
        img = cv2.resize(img, (640, 360))
        imgstack = cvzone.stackImages([img, imgPlot], 1, 1)

    cv2.imshow("eyeplot",imgstack)
    cv2.waitKey(25)