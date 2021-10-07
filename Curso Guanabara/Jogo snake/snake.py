import pygame
import random

def desenhaCobra(cor):
    tela.fill(corFundo)
    for unidade in listaCobra:
        pygame.draw.rect(tela,cor,[unidade[0],unidade[1],d,d])

def moverCobra(dx, dy):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d


    x_novo = listaCobra[-1][0] + dx
    y_novo = listaCobra[-1][1] + dy
    listaCobra.append([x_novo, y_novo])
    del listaCobra[0]
    # if x + delta_x <= dimensoesTela[0] - d and x + delta_x >= 0:
    #     x = x + delta_x
    # if y + delta_y <= dimensoesTela[1] - d and y + delta_y >= 0:
    #     y = y + delta_y
    return dx,dy



#VALORES INICIAIS
corFundo = (0,0,0)
corCobra = (255,255,255)
dimensoesTela = (600, 600)
x, y = dimensoesTela[0] // 2, dimensoesTela[1] // 2

dx = 0
dy = 0

listaCobra = [[x, y]]
print(listaCobra[0])
d = 20

tela = pygame.display.set_mode((dimensoesTela))
pygame.display.set_caption('Snake Andssuuu')

tela.fill(corFundo)

clock = pygame.time.Clock()

while True:
    pygame.display.update()
    desenhaCobra((random.randint(100,255), random.randint(100,255), random.randint(100,255)))
    #desenhaCobra(corCobra)
    dx, dy = moverCobra(dx,dy)# recebe nova posicao da cobra pela tupla
    print(listaCobra)
    clock.tick(6)