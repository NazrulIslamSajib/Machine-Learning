import cv2
import numpy as pd

img1=cv2.imread(r"C:\Users\sotez\Desktop\Open CV/girl.png") 
img2=cv2.imread(r"C:\Users\sotez\Desktop\Open CV/mayeen.png")  
if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

if img1.dtype != img2.dtype:
    img2 = img2.astype(img1.dtype) 

    
img=cv2.bitwise_xor(img1,img2,mask=None) #xor,and,or,not
cv2.imshow("mayengirl",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
