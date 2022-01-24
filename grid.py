import pygame

Width , Height = 500,800
screen = pygame.display.set_mode((Width,Height))



bg1 = pygame.transform.scale2x(pygame.image.load("assets/background-day.png"))
bg2 = pygame.image.load("assets/background-night.png")
base = pygame.transform.scale2x(pygame.image.load("assets/base.png"))
bird_up= pygame.image.load("assets/bluebird-upflap.png")
bird_mid= pygame.image.load("assets/bluebird-midflap.png")
bird_down= pygame.image.load("assets/bluebird-downflap.png")

bird_rect = bird_mid.get_rect(center = (100,400))

gravity = 0.25
bird_movement = 0

