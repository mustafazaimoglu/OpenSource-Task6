import cv2
import numpy as np

img = cv2.imread("src/lena.png")
cv2.imshow("original",img)

# img_gamma = np.array(255 * (img / 255) ** 1.50, dtype="uint8")
# cv2.imshow("gamma",img_gamma)

median_filtered = cv2.medianBlur(img, 9)
cv2.imshow("median_filtered",median_filtered)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",img_gray)

# Crop
# Histogram

_, binary_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("thresh",binary_thresh)

img_rotated = cv2.rotate(binary_thresh, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotated_image",img_rotated)

cv2.waitKey(0)

#If you wanna apply gamma call gamaConverter function :)
def gamaConverter(original):
    for gamma in [1, 0.1, 0.5, 1.2, 2.2, 4, 10]:
        gamma_corrected = np.array(255 * ((original / 255) ** gamma), dtype='uint8')
        cv2.imshow("Gamma " + str(gamma), gamma_corrected)
        cv2.waitKey()
