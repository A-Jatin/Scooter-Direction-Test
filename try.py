import numpy as np
import cv2
import os
os.chdir('C:/Users/JATIN/Downloads')

# Blue cicle means that the annotation haven't started
# Green circle is a good pose
# Red is a bad pose
# White circle means we are done, press d for that

# Instructions on how to use!
# Press space to swap between states, you have to press space when the person
# starts doing poses. 
# Press d when the person finishes.
# press q to quit early, then the annotations are not saved, you should only 
# use this if you made a mistake and need to start over.

cap = cv2.VideoCapture('Scooter Ride through Pune City Roads.mp4')

# You can INCREASE the value of speed to make the video SLOWER
speed = 33
while(cap.isOpened()):
    # Read one frame.
    ret, frame = cap.read()
    # Break the loop if we don't get a new frame.
    if not ret:
        break
    # Add the colored circle on the image to know the state
    # Show one frame.
    cv2.putText(frame, str(frame.shape),(50, 50),cv2.FONT_HERSHEY_COMPLEX_SMALL,.7,(0,0,255))
    cv2.imshow('frame', frame[180:,:,:])
    #print(frame.shape)
    
    k = cv2.waitKey(speed)
# Release the capture and close window
cap.release()
cv2.destroyAllWindows()
