import cv2
from matplotlib import pyplot as plt

img_v = cv2.imread('vela.jpg', cv2.IMREAD_GRAYSCALE)
img_m = cv2.imread('mandrill.jpg', cv2.IMREAD_GRAYSCALE)

v_50 = cv2.resize(img_v, (0, 0), fx=0.5, fy=0.5)
v_200 = cv2.resize(img_v, (0, 0), fx=2.0, fy=2.0)
m_50 = cv2.resize(img_m, (0, 0), fx=0.5, fy=0.5)
m_200 = cv2.resize(img_m, (0, 0), fx=2.0, fy=2.0)

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs[0, 0].hist(img_v.ravel(), 256, range=[0, 256])
axs[0, 1].hist(v_50.ravel(), 256, range=[0, 256])
axs[0, 2].hist(v_200.ravel(), 256, range=[0, 256])
axs[1, 0].hist(img_m.ravel(), 256, range=[0, 256])
axs[1, 1].hist(m_50.ravel(), 256, range=[0, 256])
axs[1, 2].hist(m_200.ravel(), 256, range=[0, 256])
plt.savefig('ex1_histogramas_escala.png')
plt.close()

# A transformação de escala altera a frequência absoluta (o eixo Y do gráfico),
# pois o número total de pixels da imagem aumenta ou diminui. No entanto, a
# distribuição relativa (o formato geral do histograma) permanece praticamente
# a mesma. A proporção de tons escuros e claros não muda, preservando as
# características de contraste originais.