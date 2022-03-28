import numpy as np
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv2.VideoCapture(0) # 카메라 오픈 , 실시간 촬영 내용을 객체로 전달
detector = FaceMeshDetector(maxFaces=1)

print(cap.get(3), cap.get(4)) # 가로와 세로 픽셀 크기를 읽어옴

ret = cap.set(3,720) # 가로 길이 설정
ret = cap.set(4,480) # 세로 ""

while(True):
    ret, frame = cap.read() # cap(카메라 객체) 값을 읽어서

    # gray_ver = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # cv2.imshow("03win", gray_ver)
    cv2.imshow("03win", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()