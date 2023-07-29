import cv2
import time

cap = cv2.VideoCapture(1)
time.sleep(1)

while True:
    stutus, photo = cap.read()
    cv2.imshow("my phote", photo)
    if cv2.waitKey(50) == 13:
        break

cap.release()
cv2.destroyAllWindows()
