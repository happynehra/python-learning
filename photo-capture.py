import cv2
import time

cap = cv2.VideoCapture(1)
time.sleep(1)

stutus, photo = cap.read()
cv2.imshow("my phote", photo)
print(cv2.waitKey())

cap.release()
cv2.destroyAllWindows()
