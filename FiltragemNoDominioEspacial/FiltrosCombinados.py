import cv2
from skimage.metrics import structural_similarity as ssim

orig = cv2.imread('lena_original.png', cv2.IMREAD_GRAYSCALE)
img_sp = cv2.imread('lena_sp.png', cv2.IMREAD_GRAYSCALE)

med_3 = cv2.medianBlur(img_sp, 3)
ssim_med = ssim(orig, med_3)

med_then_gauss = cv2.GaussianBlur(med_3, (3, 3), 0)
ssim_comb = ssim(orig, med_then_gauss)

print(f"SSIM Mediana 3x3: {ssim_med:.4f}")
print(f"SSIM Mediana 3x3 + Gauss 3x3: {ssim_comb:.4f}")

#Saida

    #SSIM Mediana 3x3: 0.9231
    #SSIM Mediana 3x3 + Gauss 3x3: 0.8997

#A filtragem combinada acaba trazendo uma carga dupla de borramento (fator passa-baixas),
#reduzindo a qualidade da estrutura original da imagem e diminuindo a pontuação no índice de similaridade,
#mesmo que a imagem pareça mais "lisa".