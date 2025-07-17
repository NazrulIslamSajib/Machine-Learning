import cv2
import datetime
cap=cv2.VideoCapture(0) 
cnt=0
while(cap.isOpened()):
    ret,frame=cap.read() 
    cnt+=1
    if ret==True:  
        font=cv2.FONT_HERSHEY_COMPLEX
        #text = 'Width: ' + str(int(cap.get(3))) + ' Height: ' + str(int(cap.get(4))) 
        text="sajib"
        det = str(datetime.datetime.now())
        frame = cv2.putText(frame, det, (10, 50), font, 0.7, (0, 255, 0), 2) 
        frame = cv2.putText(frame,str(cnt), (10, 90), font, 0.7, (255, 0, 0), 2)
        cv2.imshow("sajib",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

        
