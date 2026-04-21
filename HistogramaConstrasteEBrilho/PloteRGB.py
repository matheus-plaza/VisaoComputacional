import cv2
from matplotlib import pyplot as plt

img_v = cv2.imread('vela.jpg')
img_m = cv2.imread('mandrill.jpg')
cores = ('b', 'g', 'r')

plt.figure()
for i, col in enumerate(cores):
    histr = cv2.calcHist([img_v], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
plt.savefig('ex5_vela_rgb.png')
plt.close()

plt.figure()
for i, col in enumerate(cores):
    histr = cv2.calcHist([img_m], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
plt.savefig('ex5_mandrill_rgb.png')
plt.close()

# O canal dominante é aquele cujo histograma possui os maiores picos ou
# cuja curva está mais deslocada para a direita (valores de intensidade
# mais altos, próximos a 255).