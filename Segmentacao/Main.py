import cv2

def contar_moedas(caminho_imagem):
    img = cv2.imread(caminho_imagem)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contagem = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            contagem += 1

    return contagem


def contar_moscas(caminho_imagem):
    img = cv2.imread(caminho_imagem)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contagem = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 150:
            contagem += 1

    return contagem


print(f"Quantidade de moedas: {contar_moedas('moedas.jpg')}")
print(f"Quantidade de moscas imagem 1: {contar_moscas('moscas1.jpg')}")
print(f"Quantidade de moscas imagem 2: {contar_moscas('moscas2.jpg')}")
print(f"Quantidade de moscas imagem 3: {contar_moscas('moscas3.jpg')}")