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
        elif event.type == pygame.KEYUP:
            key = event.key
            if key == pygame.K_ESCAPE:
                run = False








pygame.quit()