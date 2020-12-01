import pygame

pygame.init() #init
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# background
background = pygame.image.load("C:\\Documents\\dev\\pygame\\pygame_basic\\background.png")

# conf. screen titl
pygame.display.set_caption("Nado Game")

#event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    screen.blit(background,(0,0))
    #screen.fill((0,0,255))
    pygame.display.update() # redraw screen
#pygame teminiation
pygame.quit()

