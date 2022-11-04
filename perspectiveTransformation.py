#Geometrical Transformation
import cv2
import numpy as np

vidcap = cv2.VideoCapture("Drone.mp4") #inside "" will be the video name
success, image = vidcap.read()

while success:
    success, image = vidcap.read()
    frame = cv2.resize(image, (640, 480))
    
    #Selecting Coordinates
    tl = (222, 387)
    bl = (70, 472)
    tr = (400, 380)
    br = (538, 472)
    
    cv2.circle(frame, tl, 5, (0,0,225), -1)
    cv2.circle(frame, bl, 5, (0,0,225), -1)
    cv2.circle(frame, tr, 5, (0,0,225), -1)
    cv2.circle(frame, br, 5, (0,0,225), -1)
    
    #Apply Geometrical Transformation
    pts1 = [tl, bl, tr, br]
    pts2 = [[0,0], [0,480], [640,0], [640,48]]
    
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed_frame = cv2.warpPerspective(frame, matrix, (640, 480))
    
    cv2.imshow("Frame", frame)
    cv2.imshow("transformed_frame Bird's Eye View", transformed_frame)
    
    if cv2.waitKey(1) == 27:
        break