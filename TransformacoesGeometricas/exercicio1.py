import cv2
import numpy as np

img = cv2.imread('lena.png')
h, w = img.shape[:2]

M_rot = cv2.getRotationMatrix2D((w//2, h//2), 45, 0.7)
img_rot = cv2.warpAffine(img, M_rot, (w, h))

M_scale = cv2.getRotationMatrix2D((w//2, h//2), 0, 1.5)
img_scale = cv2.warpAffine(img, M_scale, (w, h))

M_shear = np.float32([[1, 0.2, -50], [0, 1, 0]])
img_shear = cv2.warpAffine(img, M_shear, (w, h))

linha1 = np.hstack((img, img_rot))
linha2 = np.hstack((img_scale, img_shear))
mosaico = np.vstack((linha1, linha2))

cv2.imshow('Mosaico Criativo', mosaico)
cv2.imwrite('mosaico_lena.jpg', mosaico)
cv2.waitKey(0)
cv2.destroyAllWindows()