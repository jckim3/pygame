import pygame

pygame.init() #init
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# conf. screen titl
pygame.display.set_caption("Nado Game")

#event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

#pygame teminiation
pygame.quit()

