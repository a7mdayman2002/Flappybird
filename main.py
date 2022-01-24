import pygame


pygame.init()

Width , Height = 800,800
Screen = pygame.display.set_mode((Width,Height))
clock = pygame.time.Clock()
fps = 30
run = True

while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False








pygame.quit()