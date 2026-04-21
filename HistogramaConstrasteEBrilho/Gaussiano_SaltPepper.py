import cv2
import numpy as np
from matplotlib import pyplot as plt

img_v = cv2.imread('vela.jpg', cv2.IMREAD_GRAYSCALE)
img_m = cv2.imread('mandrill.jpg', cv2.IMREAD_GRAYSCALE)

def aplicar_gauss(img):
    gauss = np.random.normal(0, 25, img.shape).astype(np.float32)
    noisy = cv2.add(img.astype(np.float32), gauss)
    return np.clip(noisy, 0, 255).astype(np.uint8)

def aplicar_sp(img):
    noisy = np.copy(img)
    prob = 0.05
    rnd = np.random.rand(*img.shape)
    noisy[rnd < prob/2] = 0
    noisy[rnd > 1 - prob/2] = 255
    return noisy

v_gauss = aplicar_gauss(img_v)
v_sp = aplicar_sp(img_v)
m_gauss = aplicar_gauss(img_m)
m_sp = aplicar_sp(img_m)

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs[0, 0].hist(img_v.ravel(), 256, range=[0, 256])
axs[0, 1].hist(v_gauss.ravel(), 256, range=[0, 256])
axs[0, 2].hist(v_sp.ravel(), 256, range=[0, 256])
axs[1, 0].hist(img_m.ravel(), 256, range=[0, 256])
axs[1, 1].hist(m_gauss.ravel(), 256, range=[0, 256])
axs[1, 2].hist(m_sp.ravel(), 256, range=[0, 256])
plt.savefig('ex7_histogramas_ruidos.png')
plt.close()


# O ruído Gaussiano afeta a imagem inteira com variações matemáticas contínuas.
# No histograma, isso faz com que os picos originais fiquem mais "largos" e
# borrados. Já o ruído Salt & Pepper não alarga os picos centrais; em vez disso,
# ele rouba alguns pixels aleatórios da imagem e cria dois picos pontuais e
# extremos exatamente nas intensidades 0 (pimenta) e 255 (sal).