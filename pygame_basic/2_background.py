import pygame

pygame.init() #init
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# background
background = pygame.image.load("C:\\Documents\\dev\\pygame\\pygame_basic\\background.png")

# read sprit(character)
character = pygame.image.load("C:\\Documents\\dev\\pygame\\pygame_basic\\character.png")
character_size = character.get_rect().size  #get image size
character_width = character_size[0]  #hor
character_height = character_size[1] #veri

character_x_pos = screen_width / 2 - (character_height / 2)
character_y_pos = screen_height - character_height


# conf. screen titl
pygame.display.set_caption("Nado Game")

#event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))

    #screen.fill((0,0,255))
    pygame.display.update() # redraw screen
#pygame teminiation
pygame.quit()

