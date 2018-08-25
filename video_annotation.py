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

# Start with the beginning state as 10 to indicate that the procedure has not started
current_state = 0
saveAnnotations = True
annotation_list = []
# We can check wether the video capture has been opened
cap.isOpened()
colCirc = (255,0,0)
# Iterate while the capture is open, i.e. while we still get new frames.
while(cap.isOpened()):
    # Read one frame.
    ret, frame = cap.read()
    # Break the loop if we don't get a new frame.
    if not ret:
        break
    # Add the colored circle on the image to know the state
    cv2.circle(frame,(50,50), 50, colCirc, -1)
    # Show one frame.
    cv2.imshow('frame', frame)
    # Wait for a keypress and act on it
    k = cv2.waitKey(speed)
    if k == ord('1'):
        current_state = 1
        colCirc = (0,0,255)
    if k == ord('2'):
        current_state = 0
        colCirc = (0,255,0)
    if k == ord('3'):
        current_state = 2
        colCirc = (255,0,0)

    # Press q to quit
    if k == ord('q'):
        print ("You quit! Restart the annotations by running this script again!")
        saveAnnotations = False
        break

    annotation_list.append(current_state)

# Release the capture and close window
cap.release()
cv2.destroyAllWindows()

# Only save if you did not quit
if saveAnnotations:
    f = open('Label.txt', 'w')
    for item in annotation_list:
        f.write(str(item))
    f.close()