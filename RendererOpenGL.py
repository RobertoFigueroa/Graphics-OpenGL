import pygame
from pygame.locals import *
import pygame_menu
from time import sleep

from gl import Renderer, Model
import shaders

import glm

deltaTime = 0.0

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (1000, 500)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)
font = pygame.font.SysFont("Arial", 30)


# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.camPosition.z = 3
r.pointLight.x = 5
r.pointLight.y = 5

r.setShaders(shaders.vertex_shader4, shaders.fragment_shader)


r.modelList.append(Model('heli.obj', 'heli.bmp'))
r.modelList.append(Model('heli2.obj', 'heli2.bmp'))
r.modelList.append(Model('airplane.obj', 'airplane.bmp'))
r.modelList.append(Model('house.obj', 'house.bmp'))

for model in r.modelList:
    model.scale = glm.vec3(0.01,0.01,0.01)

isPlaying = True
while isPlaying:
    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()
    # Move cam
    if keys[K_d]:
        r.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        r.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        r.camPosition.z -= 1 * deltaTime
    if keys[K_s]:
        r.camPosition.z += 1 * deltaTime
    

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.setShaders(shaders.vertex_shader4, shaders.fragment_shader)
            elif ev.key == pygame.K_2:
                r.setShaders(shaders.vertex_shader2, shaders.fragment_shader)
            elif ev.key == pygame.K_3:
                r.setShaders(shaders.vertex_shader3, shaders.fragment_shader)
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
            elif ev.key == pygame.K_RIGHT:
                sleep(0.5)
                sound = pygame.mixer.Sound('./click.wav')
                pygame.mixer.Sound.play(sound)
                r.selected_model = (r.selected_model + 1) % len(r.modelList)
            elif ev.key == pygame.K_LEFT:
                sleep(0.5)
                sound = pygame.mixer.Sound('./click.wav')
                pygame.mixer.Sound.play(sound)
                r.selected_model = (r.selected_model - 1) % len(r.modelList)

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000


pygame.quit()
