import os
import pygame
#####################################################
# basic initialize
pygame.init() #init
screen_width = 640  
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Nado Pang")
clock = pygame.time.Clock()
#############################################################
# User Initialize 
# background

current_path =  os.path.dirname(__file__)  # return current postion
image_path = os.path.join(current_path,"images")


background = pygame.image.load(os.path.join(image_path,"background.png"))
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height =  stage_size[1]   # put the character on stage


# read sprit(character)
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size  #get image size
character_width = character_size[0]  #hor
character_height = character_size[1] #veri
character_x_pos = screen_width / 2 - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# move coord
character_to_x = 0
character_to_y = 0
character_speed = 0.3


#weapon
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size  #get image size
weapon_width = weapon_size[0]  #hor

# multi shot
weapons = []
weapon_speed = 10

#ball 

ball_images = [
    pygame.image.load(os.path.join(image_path,"ballon1.png")),
    pygame.image.load(os.path.join(image_path,"ballon2.png")),
    pygame.image.load(os.path.join(image_path,"ballon3.png")),
    pygame.image.load(os.path.join(image_path,"ballon4.png"))
]

ball_speedn_y = [ -18,-15,-12,-9] #0,1,2,3

#balls
balls =[]

balls.append({
    "pos_x": 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,   # x direction
    "to_y" : -6,  # y direction
    "init_speed_y" : ball_speedn_y[0] 
})

#display text
game_font = pygame.font.Font(None,40)
total_time = 10
start_ticks = pygame.time.get_ticks()

#event loop
running = True
while running:
    dt = clock.tick(30)  #FPS setting
    #character to move 100
    # 10 fps :   10 * 10  100
    # 20 fps :    5 * 20 =  100
    print("fps : " + str(clock.get_fps()))

    # event handler 
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        if event.type ==  pygame.KEYDOWN:
            if event.key ==  pygame.K_LEFT:
                character_to_x -=character_speed
            elif event.key ==  pygame.K_RIGHT:    
                character_to_x +=character_speed        
            # elif event.key ==  pygame.K_UP:
            #     character_to_y -=character_speed
            # elif event.key ==  pygame.K_DOWN:
                # character_to_y +=character_speed
            elif event.key ==  pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                character_to_y = 0

    #3. game character position update
    character_x_pos += character_to_x * dt
    character_y_pos += character_to_y * dt

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos =  screen_width - character_width

    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos =  screen_height - character_height

#4 collision info
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top =  character_y_pos

# weapons position change 100,200  -> 100, 180,16
    weapons = [[w[0],w[1]-weapon_speed ] for w in weapons]

# delect weapon on top
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0 ]

# collision check
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx  = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width =  ball_size[0]
        ball_height = ball_size[1]

        # refect from wall
        if  ball_pos_x <= 0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] =  ball_val["to_x"] * -1

        # ver. postion
        if  ball_pos_y >= screen_height -  stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_speed_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

#5 render screen

    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx,ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y =  ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))

    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))



    #add timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # sec
    timer = game_font.render(str(int(total_time - elapsed_time)), True,(255,255,255))
    screen.blit(timer,(10,10))

    if ( total_time -  elapsed_time <= 0 ):
        print("time out")
        running = False
    #screen.fill((0,0,255))
    pygame.display.update() # redraw screen


pygame.time.delay(2000)
#pygame teminiation
pygame.quit()

