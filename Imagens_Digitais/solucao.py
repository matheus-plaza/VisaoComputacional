import cv2
import numpy as np
import os

if not os.path.exists('VisaoComputacional'):
    os.makedirs('VisaoComputacional')

img_v = cv2.imread('vermelho.jpg')
h, w, _ = img_v.shape
img_p = np.zeros((h, w, 3), dtype=np.uint8)
cv2.imwrite('VisaoComputacional/preta.jpg', img_p)

img_50 = img_p.copy()
cv2.rectangle(img_50, (w//2 - 25, h//2 - 25), (w//2 + 25, h//2 + 25), (255,     255, 255), -1)
cv2.imwrite('VisaoComputacional/quadradobranco50.jpg', img_50)

img_25 = img_p.copy()
cv2.rectangle(img_25, (w//2 - 12, h//2 - 12), (w//2 + 13, h//2 + 13), (255, 255, 255), -1)
cv2.imwrite('VisaoComputacional/quadradobranco25.jpg', img_25)

img_sub = cv2.subtract(img_50, img_25)
cv2.imwrite('VisaoComputacional/subtracao.jpg', img_sub)

img_inv = cv2.bitwise_not(img_sub)
img_xor = cv2.bitwise_xor(img_inv, img_50)
cv2.imwrite('VisaoComputacional/exercicio5.jpg', img_xor)

img_tv = cv2.imread('televisao.jpg')
tv_recortada = img_tv[75:265, 80:348]
tv_flip = cv2.flip(tv_recortada, 1)
cv2.imwrite('VisaoComputacional/tv_recortada.jpg', tv_flip)

img_gato = cv2.imread('gato.jpg')
gato_redim = cv2.resize(img_gato, (268, 190))
mascara = np.zeros((190, 268), dtype=np.uint8)
cv2.rectangle(mascara, (20, 20), (240, 155), 255, -1)
gato_mascara = cv2.bitwise_and(gato_redim, gato_redim, mask=mascara)
resultado_final = cv2.addWeighted(tv_flip, 0.5, gato_mascara, 0.5, 0)
cv2.imwrite('VisaoComputacional/gato_na_tv.jpg', resultado_final)