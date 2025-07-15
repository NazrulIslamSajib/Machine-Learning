from __future__ import print_function
import cv2 as cv
import argparse 
import cv2

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h, x:x+w]

        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0), 4)

    cv.imshow('Capture - Face detection', frame)

# --- Argument parser
parser = argparse.ArgumentParser(description='Haar Cascade Face and Eye Detection')
parser.add_argument('--face_cascade', help='Path to face cascade.',
                    default=cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.',
                    default=cv.data.haarcascades + 'haarcascade_eye.xml')
parser.add_argument('--camera', help='Camera device number.', type=int, default=0)
args = parser.parse_args()

# --- Load cascades
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()

if not face_cascade.load(cv.samples.findFile(args.face_cascade)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(args.eyes_cascade)):
    print('--(!)Error loading eyes cascade')
    exit(0)

# --- Open camera
cap = cv.VideoCapture(args.camera)
if not cap.isOpened():
    print('--(!)Error opening video capture')
    exit(0)

while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break 
    cv2.imwrite('output_frame1.jpg', frame)
    detectAndDisplay(frame) 
    if cv.waitKey(10) == 27:  # ESC key 
        break

cap.release()
cv.destroyAllWindows()
