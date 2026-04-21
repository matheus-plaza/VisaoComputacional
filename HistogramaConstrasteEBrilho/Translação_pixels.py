import cv2
import numpy as np
from matplotlib import pyplot as plt

img_v = cv2.imread('vela.jpg', cv2.IMREAD_GRAYSCALE)
h, w = img_v.shape

M = np.float32([[1, 0, 150], [0, 1, 150]])
trans_v = cv2.warpAffine(img_v, M, (w, h))

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].hist(img_v.ravel(), 256, range=[0, 256])
axs[1].hist(trans_v.ravel(), 256, range=[0, 256])
plt.savefig('ex3_histograma_translacao.png')
plt.close()

resultado = np.hstack((img_v, trans_v))
cv2.imwrite('vela_translacao_comparacao.jpg', resultado)

# A translação em si não altera os valores dos pixels que foram movidos.
# Porém, como a área vazia deixada pelo deslocamento foi preenchida com pixels
# pretos, o novo histograma apresentará um pico gigantesco exatamente na
# intensidade 0 (preto absoluto). Esse novo pico distorce a escala do gráfico,
# fazendo com que a distribuição original pareça comprimida, embora a contagem
# dos pixels da vela continue a mesma.