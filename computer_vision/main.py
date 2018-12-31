import cv2
import sys
import numpy as np
import requests

fist_cascade = cv2.CascadeClassifier('classifiers/fist.xml')
palm_cascade = cv2.CascadeClassifier('classifiers/palm.xml')

write_endpoint = "http://asteria-app.herokuapp.com/write"
erase_endpoint = "http://asteria-app.herokuapp.com/erase"

cap = cv2.VideoCapture(0)

while True:
    ret, img=cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
    palms = palm_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in fists:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        req_x = ( ( img.shape[1]-((2*x+w)/2) )/img.shape[1])
        req_y = ( ( img.shape[0]-((2*y+h)/2) )/img.shape[0])

        r = requests.post(write_endpoint, data={'x': req_x, 'y': req_y})

    for (x,y,w,h) in palms:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        req_x = ( ( img.shape[1]-((2*x+w)/2) )/img.shape[1])
        req_y = ( ( img.shape[0]-((2*y+h)/2) )/img.shape[0])

        r = requests.post(erase_endpoint, data={'x': req_x, 'y': req_y})

    display_img = cv2.flip(img, 1)
    cv2.imshow("Frame", display_img)

    if cv2.waitKey(30) & 0xFF == 32:
        break

cap.release()
cv2.destroyAllWindows()
