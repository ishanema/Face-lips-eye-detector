#Importing libraries
import cv2

#Loading cascades
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('SmileCascade.xml')

#Defining function that detect face and eye
def detect(gray,frame):
    faces=face_cascade.detectMultiScale(gray,1.3,22);
    for(x,y,w,h) in faces:
        #Drawing face rectangle
        cv2.rectangle(frame,(x,y), (x+w,y+h),(255,0,0),2)
        #Detection of eyes
        #region of intrest in gray image
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,3)
        smile=smile_cascade.detectMultiScale(roi_gray,1.7,22)
        for(ex,ey,ew,eh) in eyes:
            #Drawing eye rectangle
            cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh),(0,255,0),2)
        #Drawing Smile Rectangle
        for(sx,sy,sw,sh) in smile:
            #Drawing eye rectangle
            cv2.rectangle(roi_color,(sx,sy), (sx+sw,sy+sh),(0,0,255),2)
    return frame

#Input from webcam. 0 if internal webcam 1 for external webcam 
video_capture=cv2.VideoCapture(0)
while True:
    #we are only interested in one parameter thus _
    _,frame=video_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
