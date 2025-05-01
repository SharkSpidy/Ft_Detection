import cv2
import numpy as np

img1 = cv2.imread("Images/qoc.jpg")
img2 = cv2.imread("Train/queen.jpg")

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)