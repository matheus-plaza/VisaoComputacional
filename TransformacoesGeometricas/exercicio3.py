import cv2
import numpy as np

lena = cv2.imread('lena.png')
moldura = cv2.imread('moldura.jpg')

h_l, w_l = lena.shape[:2]
h_m, w_m = moldura.shape[:2]

pts_src = np.float32([[0, 0], [w_l, 0], [w_l, h_l], [0, h_l]])
pts_dst = np.float32([[191, 79], [472, 141], [419, 419], [142, 341]])

M = cv2.getPerspectiveTransform(pts_src, pts_dst)
lena_warped = cv2.warpPerspective(lena, M, (w_m, h_m))

mask = np.zeros((h_m, w_m), dtype=np.uint8)
cv2.fillConvexPoly(mask, pts_dst.astype(np.int32), 255)

mask_inv = cv2.bitwise_not(mask)
moldura_bg = cv2.bitwise_and(moldura, moldura, mask=mask_inv)
resultado = cv2.add(moldura_bg, lena_warped)

cv2.imshow('Lena na Moldura', resultado)
cv2.imwrite('lena_moldura.jpg', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()