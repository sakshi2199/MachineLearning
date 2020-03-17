import cv2
#now loading camera
cap = cv2.VideoCapture(0)
#loading face data
face_detect = cv2.CascadeClassifier('face.xml')
eye_detect = cv2.CascadeClassifier('eye1.xml')
while cap.isOpened():
    #taking pics
    status,frame=cap.read()
    #converting to gray
    grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #print(grayimg)
    #now we can detect face
    face = face_detect.detectMultiScale(grayimg)
    print(face)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y), (x+w, y+h),(0,0,255),4)
        onlyface = frame[y:y+h, x:x+w]
        eye = eye_detect.detectMultiScale(onlyface)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(onlyface, (ex,ey), (ex+ew, ey+eh), (255,0,0),2)
    cv2.imshow('face', frame)
    #cv2.imshow('face1', onlyface)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows() #closes the window which is opened by imshow
cap.release() #to stop the camera
    
#the output is of the following format
'''
x y w h
w = width
h = height
'''
