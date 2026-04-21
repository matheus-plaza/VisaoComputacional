import cv2

img_v = cv2.imread('vela.jpg')
img_m = cv2.imread('mandrill.jpg')
canais = ['B', 'G', 'R']

for i, nome in enumerate(canais):
    v_copy = img_v.copy()
    v_copy[:, :, i] = cv2.equalizeHist(v_copy[:, :, i])
    cv2.imwrite(f'vela_eq_{nome}.jpg', v_copy)

    m_copy = img_m.copy()
    m_copy[:, :, i] = cv2.equalizeHist(m_copy[:, :, i])
    cv2.imwrite(f'mandrill_eq_{nome}.jpg', m_copy)


# Ao equalizar apenas um canal de cor por vez, o balanço de branco da
# imagem é completamente destruído. O canal equalizado terá suas intensidades
# esticadas até o máximo (255), sobrepondo-se aos outros dois canais de forma
# desproporcional. Isso gera anomalias visuais e cores super saturadas (ex:
# equalizar só o Red deixa a imagem com um forte tom avermelhado ou ciano).