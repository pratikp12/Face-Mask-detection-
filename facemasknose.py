import sys
import cv2
# Get user supplied values

# Create the haar cascade
noseCascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
# Read the image
cap = cv2.VideoCapture(0)

while True:
    # Read the frameS
    _, img = cap.read()
    # Convert to grayscale
    font = cv2.FONT_HERSHEY_SIMPLEX
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    #faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    nose = noseCascade.detectMultiScale(gray)
    for (x, y, w, h) in nose:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img,'Person is not wearing mask', (x, y+100), font, 1, (0, 0, 0), 1,cv2.LINE_AA)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()