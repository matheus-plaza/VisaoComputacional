import cv2

img_v = cv2.imread('vela.jpg', cv2.IMREAD_GRAYSCALE)
img_m = cv2.imread('mandrill.jpg', cv2.IMREAD_GRAYSCALE)

mean_v, std_v = cv2.meanStdDev(img_v)
mean_m, std_m = cv2.meanStdDev(img_m)

print(f"Vela - Media: {mean_v[0][0]:.2f}, Desvio Padrao: {std_v[0][0]:.2f}")
print(f"Mandrill - Media: {mean_m[0][0]:.2f}, Desvio Padrao: {std_m[0][0]:.2f}")

# Vela - Media: 7.09, Desvio Padrao: 33.08
# Mandrill - Media: 60.21, Desvio Padrao: 40.24
# A "Média" revela o brilho global da imagem. Uma média alta significa que a
# imagem é majoritariamente clara; uma média baixa indica uma imagem escura.
# O "Desvio Padrão" revela o contraste. Um desvio padrão alto significa que os
# pixels estão espalhados por muitos tons diferentes (alto contraste), enquanto
# um desvio baixo indica que os pixels estão concentrados em um tom muito
# parecido (baixo contraste, imagem "lavada").