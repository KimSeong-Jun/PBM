import cv2
import numpy as np

def auto_canny(image, sigma=0.33):
    image = cv2.GaussianBlur(image, (3, 3), 0)
 	# compute the median of the single channel pixel intensities
    v=np.median(image)
 	# apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
 	# return the edged image
    return edged

cap = cv2.VideoCapture(0)

cap.set(3, 600)
cap.set(4, 2400) # 동영상의 크기 조절

while True: # 무한 루프

    ret, frame = cap.read() # 두 개의 값을 반환하므로 두 변수 지정

    if not ret: # 새로운 프레임을 못받아 왔을 때 braek
        break  
    
    

    edge_framgaus = auto_canny(frame, sigma=0.33)
    cv2.imshow('real_camera', frame)
    cv2.imshow('gaussian', edge_framgaus)
    

    # 10ms 기다리고 다음 프레임으로 전환, Esc누르면 while 강제 종료
    if cv2.waitKey(10) == 27:
        break

cap.release() # 사용한 자원 해제
cv2.destroyAllWindows()

