import cv2
import numpy as np

img1 = cv2.imread('sudoku_1.jpg')
img2 = cv2.imread('sudoku_2.jpg')

pts_src_1 = np.float32([[82, 104], [404, 91], [438, 391], [54, 403]])
pts_dst = np.float32([[0, 0], [500, 0], [500, 500], [0, 500]])

M1 = cv2.getPerspectiveTransform(pts_src_1, pts_dst)
warp1 = cv2.warpPerspective(img1, M1, (500, 500))

pts_src_2 = np.float32([[48, 72], [504, 72], [537, 523], [36, 537]])

M2 = cv2.getPerspectiveTransform(pts_src_2, pts_dst)
warp2 = cv2.warpPerspective(img2, M2, (500, 500))

cv2.imshow('Sudoku 1 Retificado', warp1)
cv2.imshow('Sudoku 2 Retificado', warp2)
cv2.imwrite('sudoku_1_retificado.jpg', warp1)
cv2.imwrite('sudoku_2_retificado.jpg', warp2)
cv2.waitKey(0)
cv2.destroyAllWindows()