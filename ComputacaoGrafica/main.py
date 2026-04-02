import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def matriz_translacao(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])


def matriz_rotacao(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])


def aplicar_transformacao(matriz, pontos):
    return matriz @ pontos


def criar_retangulo(largura, altura):
    x = [0, largura, largura, 0, 0]
    y = [0, 0, altura, altura, 0]
    ones = np.ones(5)
    return np.array([x, y, ones])


def criar_triangulo(base, altura):
    x = [0, base, base / 2, 0]
    y = [0, 0, altura, 0]
    ones = np.ones(4)
    return np.array([x, y, ones])


def criar_circulo(raio, num_segmentos=50):
    angulos = np.linspace(0, 2 * np.pi, num_segmentos)
    x = raio * np.cos(angulos)
    y = raio * np.sin(angulos)
    ones = np.ones(num_segmentos)
    return np.array([x, y, ones])


def criar_raios_roda(raio):
    x = [-raio, raio, 0, 0, 0]
    y = [0, 0, 0, -raio, raio]
    ones = np.ones(5)
    return np.array([x, y, ones])


fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(-10, 10)
ax.set_ylim(-3, 8)
ax.set_aspect('equal')
ax.set_title("Trabalho 1 - Transformações 2D (Animação)")

rua = aplicar_transformacao(matriz_translacao(-10, -3), criar_retangulo(20, 2))
ax.fill(rua[0], rua[1], facecolor='gray', edgecolor='black', zorder=1)

predio1 = aplicar_transformacao(matriz_translacao(-9, -1), criar_retangulo(1.5, 4))
predio2 = aplicar_transformacao(matriz_translacao(-6.5, -1), criar_retangulo(1.5, 3))
predio3 = aplicar_transformacao(matriz_translacao(1.5, -1), criar_retangulo(2, 5))
predio4 = aplicar_transformacao(matriz_translacao(4.5, -1), criar_retangulo(1.5, 6))
predio5 = aplicar_transformacao(matriz_translacao(7.5, -1), criar_retangulo(1.5, 2.5))

for p in [predio1, predio2, predio3, predio4, predio5]:
    ax.fill(p[0], p[1], facecolor='blue', edgecolor='black', zorder=2)

casa1_base = aplicar_transformacao(matriz_translacao(-3, -1), criar_retangulo(1.5, 1.5))
casa1_teto = aplicar_transformacao(matriz_translacao(-3.2, 0.5), criar_triangulo(1.9, 1))
casa2_base = aplicar_transformacao(matriz_translacao(-0.5, -1), criar_retangulo(1.2, 1.2))
casa2_teto = aplicar_transformacao(matriz_translacao(-0.7, 0.2), criar_triangulo(1.6, 0.8))

for c in [casa1_base, casa1_teto, casa2_base, casa2_teto]:
    ax.fill(c[0], c[1], facecolor='yellow', edgecolor='black', zorder=2)

sol = aplicar_transformacao(matriz_translacao(-7, 6), criar_circulo(0.8))
ax.fill(sol[0], sol[1], facecolor='orange', zorder=0)

raio_roda = 0.4
largura_carro = 2.5
altura_carro = 1.0

corpo_original = aplicar_transformacao(matriz_translacao(-largura_carro / 2, 0),
                                       criar_retangulo(largura_carro, altura_carro))
roda_original = criar_circulo(raio_roda)
raios_originais = criar_raios_roda(raio_roda)

corpo_patch = plt.Polygon(np.column_stack((corpo_original[0], corpo_original[1])), facecolor='green', edgecolor='black',
                          zorder=3)
roda1_patch = plt.Polygon(np.column_stack((roda_original[0], roda_original[1])), facecolor='black', edgecolor='black',
                          zorder=4)
roda2_patch = plt.Polygon(np.column_stack((roda_original[0], roda_original[1])), facecolor='black', edgecolor='black',
                          zorder=4)

ax.add_patch(corpo_patch)
ax.add_patch(roda1_patch)
ax.add_patch(roda2_patch)

linha_raio1, = ax.plot([], [], color='white', linewidth=2, zorder=5)
linha_raio2, = ax.plot([], [], color='white', linewidth=2, zorder=5)


def init():
    linha_raio1.set_data([], [])
    linha_raio2.set_data([], [])
    return corpo_patch, roda1_patch, roda2_patch, linha_raio1, linha_raio2


def animate(frame):
    x_inicial = -8
    x_final = 8
    total_frames = 100

    progresso = frame / total_frames
    pos_x_carro = x_inicial + (x_final - x_inicial) * progresso
    pos_y_carro = -0.6

    T_carro = matriz_translacao(pos_x_carro, pos_y_carro)
    corpo_transformado = aplicar_transformacao(T_carro, corpo_original)

    distancia = pos_x_carro - x_inicial
    theta = -distancia / raio_roda

    R_roda = matriz_rotacao(theta)

    T_local_roda1 = matriz_translacao(-0.8, 0)
    M_roda1 = T_carro @ T_local_roda1 @ R_roda
    roda1_transformada = aplicar_transformacao(M_roda1, roda_original)
    raio1_transformado = aplicar_transformacao(M_roda1, raios_originais)

    T_local_roda2 = matriz_translacao(0.8, 0)
    M_roda2 = T_carro @ T_local_roda2 @ R_roda
    roda2_transformada = aplicar_transformacao(M_roda2, roda_original)
    raio2_transformado = aplicar_transformacao(M_roda2, raios_originais)

    corpo_patch.set_xy(np.column_stack((corpo_transformado[0], corpo_transformado[1])))
    roda1_patch.set_xy(np.column_stack((roda1_transformada[0], roda1_transformada[1])))
    roda2_patch.set_xy(np.column_stack((roda2_transformada[0], roda2_transformada[1])))

    linha_raio1.set_data(raio1_transformado[0], raio1_transformado[1])
    linha_raio2.set_data(raio2_transformado[0], raio2_transformado[1])

    return corpo_patch, roda1_patch, roda2_patch, linha_raio1, linha_raio2


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

anim.save('cena_transformacoes_2d.gif', writer='pillow', fps=20)