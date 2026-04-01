import cv2
import numpy as np

img_a = cv2.imread('satelite_a.png')
img_b = cv2.imread('satelite_b.png')

pts_b = np.float32([
    [204, 68],
    [364, 81],
    [569, 10],
    [174, 375],
    [163, 518],
    [569, 458]
])

pts_a = np.float32([
    [438, 65],
    [594, 77],
    [798, 6],
    [403, 371],
    [393, 515],
    [797, 454]
])

M, _ = cv2.findHomography(pts_b, pts_a, cv2.RANSAC)

h_a, w_a = img_a.shape[:2]
h_b, w_b = img_b.shape[:2]

w_nova = w_a + w_b
h_nova = h_a

mosaico = cv2.warpPerspective(img_b, M, (w_nova, h_nova))

mosaico[0:h_a, 0:w_a] = img_a

cv2.imshow('Mosaico Resultante', mosaico)
cv2.imwrite('mosaico_satelite.png', mosaico)
cv2.waitKey(0)
cv2.destroyAllWindows()