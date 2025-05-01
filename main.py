import cv2
import numpy as np

img1 = cv2.imread("Images/qoc.jpg")
img2 = cv2.imread("Train/queen.jpg")

img2_resized = cv2.resize(img2, (0, 0), fx=0.2, fy=0.2)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2_resized)
cv2.waitKey(0)