import cv2
import numpy as np

cap = cv2.VideoCapture('bolt_test_pothole.mp4')

if (cap.isOpened()== False):

  print("Error opening video stream or file")
while(cap.isOpened()):

  ret, frame = cap.read()
  frame_color = frame

  if ret == True:

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(frame, 170, 255, cv2.THRESH_BINARY)
    threshold = cv2.rectangle(threshold, (0,0), (1960,400), (0,0,0), -1)
    threshold = cv2.rectangle(threshold, (1080,530), (1400,570), (0,0,0), -1)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_COMPLEX

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(frame_color, [approx], 0, (0), 1)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if 6 < len(approx):

            x,y,h,w = cv2.boundingRect(cnt)
            h_new = int(h/2)

            if(w<80):
                cv2.rectangle(frame_color,(x,y),(x+5*w,y+h_new),(0,255,0),5)

    cv2.imshow("frame", frame_color)
    if cv2.waitKey(25) & 0xFF == ord('q'): #press q to close video

      break
  else:

    break
cap.release()
cv2.destroyAllWindows()
cap = cv2.VideoCapture('virat_test_pothole.mp4')

if (cap.isOpened()== False):

  print("Error opening video stream or file")
while(cap.isOpened()):

  ret, frame = cap.read()
  frame_color = frame

  if ret == True:

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(frame, 170, 255, cv2.THRESH_BINARY)
    threshold = cv2.rectangle(threshold, (0,0), (1960,400), (0,0,0), -1)
    threshold = cv2.rectangle(threshold, (1080,530), (1400,570), (0,0,0), -1)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    font = cv2.FONT_HERSHEY_COMPLEX

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(frame_color, [approx], 0, (0), 1)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if 6 < len(approx):

            x,y,h,w = cv2.boundingRect(cnt)
            h_new = int(h/2)

            if(w<80):
                cv2.rectangle(frame_color,(x,y),(x+5*w,y+h_new),(0,255,0),5)

    cv2.imshow("frame", frame_color)
    if cv2.waitKey(25) & 0xFF == ord('q'):

      break
  else:

    break
cap.release()
cv2.destroyAllWindows()
