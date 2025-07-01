import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW) # windows ke bole dicche direct show korte
#many types of video DIVX,XVID,MJPG,X264,WMV1,WMV2 
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter(r"C:\Users\sotez\OneDrive\Desktop\Open CV\output.avi",fourcc,20.0,(640,480),0)
while cap.isOpened():
  ret,frame=cap.read() 
  if ret==True:
    cv2.imshow("frame",frame)  
    frame = cv2.resize(frame, (640, 480))
    output.write(frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release() 
output.release()
cv2.destroyAllWindows()  

#cap = cv2.VideoCapture(r"C:\Users\sotez\OneDrive\Desktop\Open CV\Interstellar Movie - Official Trailer.mp4") eta hash er modde hbe
"""
import cv2

#

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (700, 450))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)
    k = cv2.waitKey(25)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
"""
