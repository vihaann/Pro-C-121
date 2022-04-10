# import required libraries from python
import cv2
import numpy as np
import time
import random
import glob

# Select the image from the required path and select any image randomly and save it to a variable
file_path = ["buddha.jpeg", "falls.jpeg", "gp.jpg"]
images = glob.glob(random.choice(file_path))
random_image = random.choice(images)

# start the video capture and read the random image
image = cv2.imread(random_image)

# use the while loop(true) for applying mask 
while True: 
    # read the ret and frame from read() function
    ret, frame = video.read() 
    
    # resize the random image and frame to specified width and height
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 

    # selecting the colors for masking - black
    upper_black = np.array([103, 153, 70]) 
    lower_black = np.array([30, 30, 0]) 
    
    # apply the mask when black color is detected
    mask = cv2.inRange(frame, lower_black, upper_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    # Use the where function
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    # show the output
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    # stop the video when pressed q in keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 

# show the video and destroy all windows
video.release() 
cv2.destroyAllWindows() 