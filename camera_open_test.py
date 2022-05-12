import numpy as np
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

detector = FaceMeshDetector(maxFaces=1) # ?

cap = cv2.VideoCapture(0) # 카메라 오픈
# print(cap.get(3), cap.get(4)) 기본으로 설정되는 세로 * 가로 길이

ret = cap.set(3,800) # height , 세로 길이
ret = cap.set(2,600) # width, 가로 길이

while(True):
    ret, frame = cap.read() # 비디오의 한 프레임씩 읽음. 제대로 프레임을 읽으면 ret값이 True, 실패하면 False가 나타납니다. frame에 읽은 프레임이 나옵니다
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) // 회백조 영상으로 변환
    cv2.imshow('frame', frame) # 비디오를 화면에 송출함
    if cv2.waitKey(1) & 0xFF == ord('q'): # q 키보드를 누르면 while 탈출 -> 화면 종료됨
        break

cap.release()
cv2.destroyAllWindows()