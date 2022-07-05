import cv2
import pyautogui
mouse_infomation = list(pyautogui.position())
print(mouse_infomation)

face_cascade_db = cv2.CascadeClassifier("hand.xml")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1080)
primary_stats = [0, 0, 0, 0]
while True:
    success, img = cap.read()
    #img = cv2.imread("IMG_20191012_145410_3.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
        pyautogui.moveTo(x, y)
        #if primary_stats[0] - 10 > y < primary_stats[0] + 10:
        #    print('зміщення по осі X')
        #    print(x)
        #if primary_stats[1] - 10 > y < primary_stats[1] + 10:
        #    print('зміщення по осі Y')
        #    print(y)
        primary_stats[0], primary_stats[1], primary_stats[2], primary_stats[3] = x, y, w, h

    cv2.imshow('rez', img)
    #cv2.waitKey()
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()