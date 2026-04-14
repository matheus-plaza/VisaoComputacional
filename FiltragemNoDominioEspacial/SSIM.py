import cv2
from skimage.metrics import structural_similarity as ssim

orig = cv2.imread('lena_original.png', cv2.IMREAD_GRAYSCALE)
img_sp = cv2.imread('lena_sp.png', cv2.IMREAD_GRAYSCALE)
img_gauss = cv2.imread('lena_gaussian_02.png', cv2.IMREAD_GRAYSCALE)

kernels = [3, 5, 9]

for k in kernels:
    m_sp = cv2.blur(img_sp, (k, k))
    med_sp = cv2.medianBlur(img_sp, k)
    g_sp = cv2.GaussianBlur(img_sp, (k, k), 0)

    m_g = cv2.blur(img_gauss, (k, k))
    med_g = cv2.medianBlur(img_gauss, k)
    g_g = cv2.GaussianBlur(img_gauss, (k, k), 0)

    print(f"K={k} SP - Media: {ssim(orig, m_sp):.4f}, Mediana: {ssim(orig, med_sp):.4f}, Gauss: {ssim(orig, g_sp):.4f}")
    print(f"K={k} Gauss - Media: {ssim(orig, m_g):.4f}, Mediana: {ssim(orig, med_g):.4f}, Gauss: {ssim(orig, g_g):.4f}")

#Saida:

    #K=3 SP - Media: 0.5934, Mediana: 0.9231, Gauss: 0.5823
    #K=5 SP - Media: 0.6635, Mediana: 0.8441, Gauss: 0.6506
    #K=9 SP - Media: 0.6506, Mediana: 0.7512, Gauss: 0.7068
    #K=3 Gauss - Media: 0.4222, Mediana: 0.3540, Gauss: 0.3966
    #K=5 Gauss - Media: 0.5450, Mediana: 0.4824, Gauss: 0.4907
    #K=9 Gauss - Media: 0.5968, Mediana: 0.5884, Gauss: 0.6060

#Para a imagem lena_sp, a Mediana 3x3 atinge a pontuação mais alta.
#Para a imagem lena_gaussian, o filtro Gaussiano 9x9 atinge as melhores pontuações.