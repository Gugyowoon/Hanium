import cv2
import time
import threading

class Camera:

    def __init__(self, mirror=False):
        self.data = None
        self.cam = cv2.VideoCapture(1)

        self.WIDTH = 640
        self.HEIGHT = 480

        self.center_x = self.WIDTH / 2
        self.center_y = self.HEIGHT / 2
        self.touched_zoom = False

        self.scale = 1
        self.__setup()

        self.recording = False

        self.mirror = mirror

    def __setup(self):
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)
        time.sleep(2)

    def stream(self): # streaming thread 함수
        def streaming(): # 실제 thread 되는 함수
            self.ret = True
            while self.ret:
                self.ret, np_image = self.cam.read()
                if np_image is None:
                    continue
                if self.mirror: # 거울 모드 시 좌우 반전
                    np_image = cv2.flip(np_image, 1)
                self.data = np_image
                k = cv2.waitKey(1)

                if k == ord('q'):
                    self.release()
                    break
        threading.Thread(target=streaming).start()

    def show(self):
        while True:
            frame = self.data
            if frame is not None:
                cv2.imshow('Davinci AI', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                self.release()
                cv2.destroyAllWindows()
                break

    def release(self):
        self.cam.release()
        cv2.destroyAllWindows()

    ''' Zoom 기능 추가 '''

    def __zoom(self, img, center = None):
        # Zoom 기능
        height , width = img.shape[:2]
        if center is None:
            # 중심값이 None일때 (초기)
            center_x =int (width/2)
            center_y = int (height/2)
            radius_x, radius_y = int(width/2), int(height/2)

        else: # 특정 위치를 전달받은 경우엔
            center_x , center_y = center
            center_x = int(center_x)
            center_y = int(center_y) # 정수형으로 변환해주고

            left_x , right_x = center_x, int(width-center_x)
            top_x , btm_x = int(height-center_y) , center_y
            radius_x = min(left_x, right_x)
            radius_y = min(top)

    
if __name__ == '__main__':
    cam = Camera(mirror=True)
    cam.stream()
    cam.show()

# 출처: https://davinci-ai.tistory.com/8 [DAVINCI - AI]