import pygame
from pygame.locals import *

from gl import Renderer
import shaders



deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)
r.createObjects()


cubeX = 0
cubeZ = 0
cubeY = 0
yCam = 0
pCam = 0

halfXScreen = screenSize[0] / 2
halfYScreen = screenSize[1] / 2


isPlaying = True
while isPlaying:

    mouse = pygame.mouse.get_pos()
    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()
    if mouse[0] < halfXScreen -50 :
        yCam += 2 * deltaTime
    if mouse[0] > halfXScreen + 50:
        yCam -= 2 * deltaTime
    if keys[pygame.K_a]:
        cubeX -= 2 * deltaTime
    if keys[pygame.K_d]:
        cubeX += 2 * deltaTime
    if keys[pygame.K_w]:
        cubeZ -= 2 * deltaTime
    if keys[pygame.K_s]:
        cubeZ += 2 * deltaTime
    if mouse[1] < halfYScreen -50 :
        pCam += 2 * deltaTime
    if mouse[1] > halfYScreen + 50:
        pCam -= 2 * deltaTime

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False


    r.translateCube(cubeX, cubeY, cubeZ)
    r.rotateCam(yCam, 0, pCam)  

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
