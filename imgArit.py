# import cv2
# import numpy as np

# image_origin = cv2.imread("cat.jpg")
# height, width, dimen= image_origin.shape;
# copy_image=np.zeros((height, width), dtype=int);

# #merubah RGB menjadi greyscale secara manual
# for i in range(1,height):
#     for j in range (1, width):
#         copy_image[i, j] = (image_origin[i,j,0] * 0.299) + (image_origin[i,j,1]* 587) + ()
        
# cv2.imshow("greyscale", np.uint8(copy_image))

# #Cara melakukan resize image
# img_resize = cv2.resize(image_origin, (400, 500))

# cv2.imshow("Original", image_origin);
# cv2.imshow("img_resize", img_resize);

# #Cara melakukan proses Adddition and Subtraction
# incr_matrix = np.ones(image_origin.shape,dtype="uint8") + 60;

# brightened_image = cv2.add(image_origin, incr_matrix)
# cv2.imshow("Brightenes",brightened_image);

# darkened_image = cv2.add(image_origin, incr_matrix)
# cv2.imshow("Darkened", darkened_image)

# cv2.waitKey(0);

import cv2
import numpy as np

image_origin = cv2.imread("cat.jpg")
height, width, dimen = image_origin.shape
copy_image = np.zeros((height, width), dtype=np.uint8)

# Convert RGB to grayscale manually
for i in range(height):
    for j in range(width):
        copy_image[i, j] = (image_origin[i, j, 0] * 0.299) + (image_origin[i, j, 1] * 0.587) + (image_origin[i, j, 2] * 0.114)

cv2.imshow("grayscale", copy_image)

# Resize image
img_resize = cv2.resize(image_origin, (400, 500))

cv2.imshow("Original", image_origin)
cv2.imshow("img_resize", img_resize)

# Addition and Subtraction
incr_matrix = np.ones(image_origin.shape, dtype="uint8") * 60

brightened_image = cv2.add(image_origin, incr_matrix)
cv2.imshow("Brightened", brightened_image)

darkened_image = cv2.subtract(image_origin, incr_matrix)
cv2.imshow("Darkened", darkened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()