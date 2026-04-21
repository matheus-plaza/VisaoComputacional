import cv2
from matplotlib import pyplot as plt

img_v = cv2.imread('vela.jpg', cv2.IMREAD_GRAYSCALE)
img_m = cv2.imread('mandrill.jpg', cv2.IMREAD_GRAYSCALE)

eq_v = cv2.equalizeHist(img_v)
eq_m = cv2.equalizeHist(img_m)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].hist(img_v.ravel(), 256, range=[0, 256])
axs[0, 1].hist(eq_v.ravel(), 256, range=[0, 256])
axs[1, 0].hist(img_m.ravel(), 256, range=[0, 256])
axs[1, 1].hist(eq_m.ravel(), 256, range=[0, 256])
plt.savefig('ex2_histogramas_equalizados.png')
plt.close()

cv2.imwrite('vela_equalizada.jpg', eq_v)
cv2.imwrite('mandrill_equalizada.jpg', eq_m)

# A equalização estica o histograma para cobrir todo o espectro de
# intensidades (de 0 a 255). O histograma original, que geralmente possui picos
# concentrados em certas faixas de cor, passa a ser mais bem distribuído.
# Visualmente, isso resulta em um aumento drástico do contraste global da imagem.