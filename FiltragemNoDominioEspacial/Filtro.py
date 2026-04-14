import cv2

img_sp = cv2.imread('lena_sp.png', cv2.IMREAD_GRAYSCALE)
img_gauss = cv2.imread('lena_gaussian_02.png', cv2.IMREAD_GRAYSCALE)

kernels = [3, 5, 9]

for k in kernels:
    cv2.imwrite(f'sp_media_{k}.png', cv2.blur(img_sp, (k, k)))
    cv2.imwrite(f'sp_mediana_{k}.png', cv2.medianBlur(img_sp, k))
    cv2.imwrite(f'sp_gauss_{k}.png', cv2.GaussianBlur(img_sp, (k, k), 0))

    cv2.imwrite(f'gauss_media_{k}.png', cv2.blur(img_gauss, (k, k)))
    cv2.imwrite(f'gauss_mediana_{k}.png', cv2.medianBlur(img_gauss, k))
    cv2.imwrite(f'gauss_gauss_{k}.png', cv2.GaussianBlur(img_gauss, (k, k), 0))

    # Ruído Sal-e-Pimenta: O filtro da mediana tem o melhor desempenho disparado.
    # Como ele pega o valor central de uma lista ordenada, os valores extremos
    # (os pontos brancos e pretos puros do ruído impulsivo) são completamente
    # descartados pelo filtro, preservando as bordas.

    # Ruído Gaussiano: Os filtros da média e gaussiano (lineares) apresentam
    # resultados melhores. Como o ruído gaussiano é uma variação contínua e
    # aleatória nos valores dos pixels, fazer uma média ponderada ou aritmética
    # (suavização) dilui essas variações entre os vizinhos, "limpando" a imagem
    # de forma mais natural.