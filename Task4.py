#Import Library
import cv2

#Read Image
image = cv2.imread("Downloads\dog.jpg")

#To show or display image
cv2.imshow("Original Image",image)
cv2.waitKey(0)

#Read the image in RGB format
import matplotlib.pyplot as plt
%matplotlib inline
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(img_rgb)

#Create a new image by converting the original image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image

plt.imshow(gray_image)

#Inverting Image
inverted_image = 255 - gray_image
plt.imshow(inverted_image)

#Blur the image by using the Gaussian Function
blurred =cv2.GaussianBlur(inverted_image,(21,21),0)
plt.imshow(blurred)

#Invert the blurred image for final image(pencil sketch)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
plt.imshow(pencil_sketch)

#Final Sketch
cv2.imshow("Sketch Image", pencil_sketch)
cv2.waitKey(0)

#Original Image and Pencil Sketch
cv2.imshow("Sketch Image",image)
cv2.imshow("Pencil Sketch",pencil_sketch)
cv2.waitKey(0)

