import cv2
import sys
import numpy as np

img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")
img3 = cv2.imread("3.jpg")
img4 = cv2.imread("4.jpg")
img = [img1,img2,img3,img4]

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

processed_images = []

for image in img:
  if image is None:
    sys.exit("Could not read image.")
  
  hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

  mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
  yellow_only = cv2.bitwise_and(image, image, mask=mask)

  img_resize = cv2.resize(yellow_only,(300,300))
  processed_images.append(img_resize)

top_row = np.hstack((processed_images[0], processed_images[1]))
bottom_row = np.hstack((processed_images[2], processed_images[3]))
combined_image = np.vstack((top_row, bottom_row))

cv2.imshow("line_tracer", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()