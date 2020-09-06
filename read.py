import numpy as np
import pygame, sys

data = np.load(sys.argv[1] + r'.npz') if len(sys.argv) >= 2 else np.load(r'Gravdata.npz')

posxarr, posyarr = np.array(data['posxarr']), np.array(data['posyarr'])
width, height = 1500, 1000
screen, keys_pressed = pygame.display.set_mode((width, height)), pygame.key.get_pressed()
xoffset, yoffset, scale = int(width/2), int(height/2), 8000000
totaltime, numofplan = posxarr.shape

def refresh():
    global posxarr, posyarr
    screen.fill((0,0,0))
    for i in range(10):
        for j in range(numofplan):
            k = i*10
            draw(posxarr[k,j], posyarr[k,j], posxarr[k+10,j], posyarr[k+10,j],j)

def draw(pointx, pointy, pointx_2, pointy_2, col):
    global xoffset, yoffset, scale
    posx = (int(pointx//int(scale)))+xoffset
    posy = (int(pointy//int(scale)))+yoffset
    posx2 = (int(pointx_2//int(scale)))+xoffset
    posy2 = (int(pointy_2//int(scale)))+yoffset
    if posx <= width and posy <= height and posx2 <= width and posy2 <= height and posx >= 0 and posy >= 0 and posx2 >= 0 and posy2 >= 0:
        pygame.draw.line(screen, (200//(col+1), 255, 100//(col+1)), (posx, posy), (posx2, posy2))
        pygame.display.flip()

def drawAll(totaltime, numofplan):
    global posxarr, posyarr
    screen.fill((0,0,0))
    for i in range(int(totaltime/10)):
        for j in range(numofplan):
            k = i*10
            draw(posxarr[k,j], posyarr[k,j], posxarr[k+9,j], posyarr[k+9,j], j)

gameloop = True
refresh()
while gameloop == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xoffset -= 20
                refresh()
            if event.key == pygame.K_RIGHT:
                xoffset += 20
                refresh()
            if event.key == pygame.K_UP:
                yoffset -= 20
                refresh()
            if event.key == pygame.K_DOWN:
                yoffset += 20
                refresh()
            if event.key == pygame.K_a:
                scale -= scale/5
                refresh()
            if event.key == pygame.K_d:
                scale += scale/5
                refresh()
            if event.key == pygame.K_w:
                gameloop = False

drawAll(totaltime, numofplan)