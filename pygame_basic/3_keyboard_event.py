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

# move coord
to_x = 0
to_y = 0

# conf. screen titl
pygame.display.set_caption("Nado Game")

#event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        if event.type ==  pygame.KEYDOWN:
            if event.key ==  pygame.K_LEFT:
                to_x -=1
            elif event.key ==  pygame.K_RIGHT:    
                to_x +=1        
            elif event.key ==  pygame.K_UP:
                to_y -=1
            elif event.key ==  pygame.K_DOWN:
                to_y +=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos =  screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos =  screen_height - character_height

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))

    #screen.fill((0,0,255))
    pygame.display.update() # redraw screen
#pygame teminiation
pygame.quit()

