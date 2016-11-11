import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 1024)

while True:
    ret, img = cap.read()
    cv2.imshow("imput", img)
    key = cv2.waitKey(10)
    if key == 27:
        break

cv2.destoryAllWindows()
cv2.VideoCapture(0).release()

