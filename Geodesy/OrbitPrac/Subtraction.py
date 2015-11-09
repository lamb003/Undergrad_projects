import cv2
import cv




image1 = cv2.imread("closedErrosion.png")
image2 = cv2.imread("Invert.png")
image3 = image1 - image2
cv2.imwrite("sub.png", image3)