import cv2

imagem = 'satelite_b.png'


def clique_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"[{x}, {y}],")

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        cv2.imshow('Capturador de Coordenadas', img)


img = cv2.imread(imagem)

if img is None:
    print(f"Erro: Não consegui abrir a imagem {imagem}.")
else:
    print("Clique nos pontos da imagem. Pressione qualquer tecla ou feche a janela para sair.")
    cv2.imshow('Capturador de Coordenadas', img)
    cv2.setMouseCallback('Capturador de Coordenadas', clique_mouse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()