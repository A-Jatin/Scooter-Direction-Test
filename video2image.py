import cv2
import os
vidcap = cv2.VideoCapture('Scooter Ride through Pune City Roads.mp4')
success,image = vidcap.read()
count = 0
os.makedirs("C:/users/jatin/downloads/" + "video" )
while success:
  image=cv2.resize(image,(224,224))
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file   

  success,image = vidcap.read()
  k=cv2.waitKey(33)
  print('Read a new frame: ', success)
  count += 1