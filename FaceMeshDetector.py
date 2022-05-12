import time

from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
import cvzone
from cvzone.PlotModule import LivePlot

cap = cv2.VideoCapture(0)  # 웹캠 오픈
detector = FaceMeshDetector(maxFaces=5)  # para : maxFaces - 탐지할 최대 안면의 개수
eyepointList = [22, 23, 24, 110, 157, 158, 159, 160, 161, 130, 243]  # 오른쪽 눈의 랜드마크 포인트 (화면상 왼쪽)
want_color = (135, 254, 66)  # bright green
want_color2 = (242, 178, 200)  # pale pink
ratiolist = []  # 점간 거리를 저장할 리스트 자료
plotY = LivePlot(640,360,[0,40],invert=True) # 역할을 잘 모르겠음


while True:
    success, img = cap.read()
    # read 기능 == Grabs, decodes and returns the next video frame // return 값 == img(읽은 프레임), success(True 또는 False).
    img, faces = detector.findFaceMesh(img)#, draw=False)
    # findFaceMesh 기능 == Finds face landmarks in BGR Image //  return값 == 리스트 형태 Image와 faces를 반환함  faces는 빈 리스트로 초기화 된다.   drawings은 있을 수도, 없을 수도 있음
    # para 1 : img , Image to find the face landmarks in.
    # para 2 : draw: Flag to draw the output on the image. 이거 디폴트값이 True인데, 이대루 두면 흰색 메쉬 처리 합본이 그대로 뜬다. 없애고 싶으면 draw=False 설정
    # return : img, faces  →  페이스 메쉬 처리를 한 합성본 이미지와 상세 메타데이터를 faces라는 리스트 형태로 내보냄
    # print(faces) → 얼굴 인식 못하면 [] , 인식 하면 3차원 행렬 반환
    # faces의 타입은 list,  []로 초기화 되어있다.

    if faces:  # 리스트가 비어 있지 않다면 (얼굴 인식 O)
        face = faces[0]
        # face는 2차원 리스트
        # print(type(faces[0]), face)
        # time.sleep(100) 타임 슬립을 쓰면 확인하기 편하다 Delay execution for a given number of seconds.
        for id in eyepointList:
            cv2.circle(img, face[id], 2, (0, 0, 255), 3) # cv2.FILLED 를 사용하면 원을 채워넣을 수 있다.
            # circle 기능 ==　draws a simple or filled circle with a given center and radius　간단한　원을　그려낸다．　
            # para 1 : 　img　／　　원본 Image where the circle is drawn.
            # para 2 :　center．　Center of the circle.　
            # para 3 :　radius． Radius of the circle.
            # para 4 : thickness.

        leftup = face[159]
        leftdown = face[23]
        leftRight = face[130]
        leftLeft = face[243]

        len_Ver, _ = detector.findDistance(leftup, leftdown)  # 두 점간 길이를 구함
        #<<임시>># len_Hor, _ = detector.findDistance(leftLeft,leftRight)  # 반환 자료가 distance 말고도 여러개라서 무시하기 위해 (, _) 를 사용해 준 것으로 보임
        # findDistance 기능 == 두 점간 거리를 구한다.
        # para 1 : p1, Point1
        # para 2 : p2, Point2
        # return : Distance between the point(1. 두 점간 거리) , Image with output drawn(2. 결과를 반영한 이미지), Line information (각 점의 x,y 좌표와 축 상 좌표거리)

        #eye_ratio = int((len_Ver / len_Hor) * 100) #
        print(len_Ver) #16 ~ 50? 정도의 값이 찍힘

        #ratiolist.append(eye_ratio)

        cv2.line(img, leftup, leftdown, want_color, thickness=3)
        cv2.line(img, leftLeft, leftRight, want_color2, 3)
        # line 기능 == draws the line segment between pt1 and pt2 points in the image. 두 점 간에 선분을 그음 // return 값 == 선분이 그어진 이미지 (합성본)
        # para 1 : img
        # para 2 : pt1
        # para 3 : pt2
        # para 4 : color to set
        # para 5 : thickness

    # 측정된 값을 그래프로  보여주기 ===========================

        imgPlot = plotY.update(len_Ver)
        img = cv2.resize(img, (640, 360))
        imgstack = cvzone.stackImages([img, imgPlot], 1, 1)

    # 이 밑은 단순히 이미지를 띄우고, 종료하는 부분 ===================
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
