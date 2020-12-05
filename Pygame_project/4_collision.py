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

#ball 1,2,3,4  이미지 로딩하기

ball_images = [
    pygame.image.load(os.path.join(image_path,"ballon1.png")),
    pygame.image.load(os.path.join(image_path,"ballon2.png")),
    pygame.image.load(os.path.join(image_path,"ballon3.png")),
    pygame.image.load(os.path.join(image_path,"ballon4.png"))
]

#각 볼의 스피드 설정
ball_speedn_y = [ -18,-15,-12,-9] #0,1,2,3

#balls
balls =[]

# Dictoory 를 사용 한다. 
balls.append({
    "pos_x": 50,    #현재볼의 x 위치
    "pos_y" : 50,   #현재볼의 y 위치 
    "img_idx" : 0,  #현재의 image index
    "to_x" : 3,   # x direction   #현재볼의 X 방향
    "to_y" : -6,  # y direction
    "init_speed_y" : ball_speedn_y[0] 
})

# 사라질 무기, 공정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

#display text
game_font = pygame.font.Font(None,40)
total_time = 100
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

#볼 튀는것 그리기
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx  = ball_val["img_idx"]
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width =  ball_size[0]
        ball_height = ball_size[1]

        # refect from wall
        if  ball_pos_x <= 0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] =  ball_val["to_x"] * -1       #반대 방향으로  -3이면 왼쪽으로, +3 이면 오른쪽으로 

        # ver. postion
        if  ball_pos_y >= screen_height -  stage_height - ball_height:      #스테이지가 닿았을때,올가가는 속도
            ball_val["to_y"] = ball_val["init_speed_y"]
        else:
            ball_val["to_y"] += 0.5     # -6, -5.5 로 바닥으로 내려오는 효과

        #볼 속도에 따른 볼 위치 변경
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

#4  collision check  충돌처리는 여기서 넣는다
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx  = ball_val["img_idx"]

        #공rect 정보 업데이트
        ball_rect =  ball_images[ball_img_idx].get_rect()
        ball_rect.left= ball_pos_x
        ball_rect.top = ball_pos_y

        #공과 케렉터 충돌 처리
        if character_rect.colliderect(ball_rect):
            running =False
            break

        #공과무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x =  weapon_val[0]
            weapon_pos_y =  weapon_val[1]
            weapon_rect= weapon.get_rect()
            weapon_rect.left= weapon_pos_x
            weapon_rect.top=weapon_pos_y        #bug 수정, Left, Top 임. 

            #충돌 쳇크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx
                break

    if ball_to_remove > -1:
       del balls[ball_to_remove]
       ball_to_remove = -1
    
    if weapon_to_remove > -1:  
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

#####################################################
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

