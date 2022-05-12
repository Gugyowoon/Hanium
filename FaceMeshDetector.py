from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2) # para : maxFaces - 탐지할 최대 안면의 개수
eyepointList = [22, 23, 24, 110, 157, 158, 159, 160, 161, 130, 243] # Left-side eye landmark point
want_color = (135, 254, 66) # bright green
want_color2 = (242, 178, 200) # pale pink

while True:
    success, img = cap.read()
    # read 기능 == Grabs, decodes and returns the next video frame // return 값 == img(읽은 프레임), success(True 또는 False).
    img, faces = detector.findFaceMesh(img, draw=False)
    # findFaceMesh 기능 == Finds face landmarks in BGR Image //  return값 == 리스트 형태 Image와 faces를 반환함  faces는 빈 리스트로 초기화 된다.   drawings은 있을 수도, 없을 수도 있음
    # para 1 : img , Image to find the face landmarks in.
    # para 2 : draw: Flag to draw the output on the image.
    # return : img, faces / 페이스 메쉬 처리를 한 합성본 이미지와 상세 메타데이터를 faces라는 리스트 형태로 내보냄
    # print(faces) → 인식 못하면 [] , 인식 하면 3차원 행렬

    # 기본적으로 faces의 타입은 list,  []로 초기화 되어있는듯

    if faces:
        face = faces[0]
        for id in eyepointList:
            cv2.circle(img,face[id],5, (255,0,255), cv2.FILLED)

        leftup = face[159]
        leftdown = face[23]
        leftRight = face[130]
        leftLeft = face[243]

        len_Ver, _ = detector.findDistance(leftup, leftdown) # 두 점간 길이를 구함
        len_Hor, _ = detector.findDistance(leftLeft, leftRight)
        # findDistance 기능 == 두 점간 거리를 구한다.
        # para 1 : p1, Point1
        # para 2 : p2, Point2
        # return : Distance between the point(1. 두 점간 거리) , Image with output drawn(2. 결과를 반영한 이미지), Line information (각 점의 x,y 좌표와 축 상 좌표거리)

        cv2.line(img,leftup,leftdown, want_color,thickness=5)
        # line 기능 == draws the line segment between pt1 and pt2 points in the image. 두 점 간에 선분을 그음 // return 값 == 선분이 그어진 이미지 (합성본)
        # para 1 : img
        # para 2 : pt1
        # para 3 : pt2
        # para 4 : color to set
        # para 5 : thickness
        cv2.line(img,leftLeft,leftRight, want_color2,3)



    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()