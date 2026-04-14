import cv2 #Usando apenas para abrir e salvar a imagem, sem usar a logica para o filtro
import numpy as np

def manual_mean(img, k):
    pad = k // 2
    padded = np.pad(img, pad, mode='edge')
    out = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i, j] = np.mean(padded[i:i+k, j:j+k])
    return out

def manual_median(img, k):
    pad = k // 2
    padded = np.pad(img, pad, mode='edge')
    out = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            out[i, j] = np.median(padded[i:i+k, j:j+k])
    return out

img = cv2.imread('lena_sp.png', cv2.IMREAD_GRAYSCALE)

img_mean = manual_mean(img, 3)
cv2.imwrite('manual_mean_3.png', img_mean)

img_median = manual_median(img, 3)
cv2.imwrite('manual_median_3.png', img_median)