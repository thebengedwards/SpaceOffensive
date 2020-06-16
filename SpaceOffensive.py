#SpaceOffensive
import pygame, sys, os, time, random, pickle
from pygame.locals import *

pygame.init()
WindowWidth = 1028
WindowHeight = 768
P1 = WindowWidth * 0
P2 = WindowWidth * 0
gameDisplay = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption("Space Offensive")
pygame.mixer.music.load("acid.wav")

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (124,252,0)
blue = (0,0,255)
yellow = (255,255,0)
grey = (205,201,201)
purple = (160,32,240)
orange = (255,165,0)
green_light = ( 0, 255, 0)
red_light = (255, 0, 0)
blue_light = (0,191,255)

FPS = 60
clock = pygame.time.Clock()
pause = False

spaceship_width = 150
spaceship_height = 150
spaceship_centre_middle = 100
spaceship_centre = 75
spaceship_centre_side = 50

#Loading Images
spaceship = pygame.image.load("Spaceship.png")
comet = pygame.image.load("Comet.png")
Space_Background = pygame.image.load("Space_Background.jpg")
rocket = pygame.image.load("rocket.png")

def button(text,x,y,width,height,inactive_colour,active_colour, click_result = None):
    
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    if x+width > mouse_pos[0] > x and y+height > mouse_pos[1] > y:
        pygame.draw.rect(gameDisplay, active_colour,(x,y,width,height))
        if mouse_click[0] == 1 and click_result != None:
            if click_result =="Play":
                Sector001()
            elif click_result == "Quit":
                pygame.quit()
                sys.exit()
            elif click_result == "How to play":
                How_to_play()
            elif click_result == "Next":
                How_to_play2()
            elif click_result == "Main menu":
                Game_Intro()
            elif click_result == "Endless":
                Endless()
            elif click_result == "PlayEndless":
                Endless()

    else:
        pygame.draw.rect(gameDisplay, inactive_colour,(x,y,width,height))

    Font = pygame.font.Font("freesansbold.ttf",20)
    Text = Font.render(text, True, black)
    Rect = Text.get_rect()
    Rect.center = ( (x+(width/2)), (y+(height/2)) )
    gameDisplay.blit(Text, Rect)

def Sector_Space(text,x,y,width,height,inactive_colour,active_colour, click_result = None):

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if x+width > mouse_pos[0] > x and y+height > mouse_pos[1] > y:
        pygame.draw.rect(gameDisplay, active_colour,(x,y,width,height))
        if mouse_click[0] == 1 and click_result != None:
            if click_result =="S1":
                Sector001_Travel()
            elif click_result == "S2":
                Sector002_Travel()
            elif click_result == "S3":
                Sector003_Travel()
            elif click_result == "S4":
                Sector004_Travel()
            elif click_result == "S5":
                Sector005_Travel()
            elif click_result == "S6":
                Sector006_Travel()
            elif click_result == "S7":
                Sector007_Travel()
            elif click_result == "S8":
                Sector008_Travel()
            elif click_result == "S9":
                Sector009_Travel()
            elif click_result == "S10":
                Sector010_Travel()
            elif click_result == "S11":
                Sector011_Travel()
            elif click_result == "S12":
                Sector012_Travel()
            elif click_result == "S13":
                Sector013_Travel()
            elif click_result == "S14":
                Sector014_Travel()
            elif click_result == "S15":
                Sector015_Travel()
            elif click_result == "S16":
                Sector016_Travel()
            elif click_result == "S17":
                Sector017_Travel()
            elif click_result == "S18":
                Sector018_Travel()
            elif click_result == "S19":
                Sector019_Travel()
            elif click_result == "S20":
                Sector020_Travel()
            elif click_result == "S21":
                Sector021_Travel()
            elif click_result == "S22":
                Sector022_Travel()
            elif click_result == "S23":
                Sector023_Travel()
            elif click_result == "S24":
                Sector024_Travel()
            elif click_result == "S25":
                Sector025_Travel()
            elif click_result == "S26":
                Sector026_Travel()
            elif click_result == "S27":
                Sector027_Travel()
            elif click_result == "S28":
                Sector028_Travel()
            elif click_result == "S29":
                Sector029_Travel()
            elif click_result == "S30":
                Sector030_Travel()
            elif click_result == "S31":
                Sector031_Travel()
            elif click_result == "S32":
                Sector032_Travel()
            elif click_result == "S33":
                Sector033_Travel()
            elif click_result == "S34":
                Sector034_Travel()
            elif click_result == "S35":
                Sector035_Travel()
            elif click_result == "S36":
                Sector036_Travel()
            elif click_result == "S37":
                Sector037_Travel()
            elif click_result == "S38":
                Sector038_Travel()
            elif click_result == "S39":
                Sector039_Travel()
            elif click_result == "S40":
                Sector040_Travel()
            elif click_result == "S41":
                Sector041_Travel()
            elif click_result == "S42":
                Sector042_Travel()
            elif click_result == "S43":
                Sector043_Travel()
            elif click_result == "S44":
                Sector044_Travel()
            elif click_result == "S45":
                Sector045_Travel()
            elif click_result == "S46":
                Sector046_Travel()
            elif click_result == "S47":
                Sector047_Travel()
            elif click_result == "S48":
                Sector048_Travel()
    else:
        pygame.draw.rect(gameDisplay, inactive_colour,(x,y,width,height))

    Font = pygame.font.Font("freesansbold.ttf",20)
    Text = Font.render(text, True, black)
    Rect = Text.get_rect()
    Rect.center = ( (x+(width/2)), (y+(height/2)) )
    gameDisplay.blit(Text, Rect)

def Game_Intro():
    GameIntro = True
    while GameIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))
        Font = pygame.font.Font("freesansbold.ttf", 100)
        Text = Font.render("Space Offensive", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),340)
        gameDisplay.blit(Text, Rect)

        button("Play",250,514,130,50,green,green_light,"Play")
        button("Quit",450,514,130,50,red, red_light, "Quit")
        button("How to play",650,514,130,50,green,green_light,"How to play")
        button("Endless",450,614,130,50,blue,blue_light,"Endless")

        mouse_pos = pygame.mouse.get_pos()
            
        pygame.display.update()
        
def How_to_play():
    How_to_play = True
    while How_to_play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(Space_Background,(P1,P2))
        
        Font = pygame.font.Font("freesansbold.ttf", 82)
        Text = Font.render("How to play", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),70)
        gameDisplay.blit(Text, Rect)
        
        Font = pygame.font.Font("freesansbold.ttf", 16)
        Text = Font.render("The aim of the game is to make it to sector 48.. the last sector.", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),300)
        gameDisplay.blit(Text, Rect)
        
        Font = pygame.font.Font("freesansbold.ttf", 16)
        Text = Font.render("In order to get to sector 48, you must travel through other sectors.", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),400)
        gameDisplay.blit(Text, Rect)

        Font = pygame.font.Font("freesansbold.ttf", 16)
        Text = Font.render("Make it to sector 48 and you beat the game!", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),500)
        gameDisplay.blit(Text, Rect)
        
        button("Main menu",254,600,130,50,green,green_light,"Main menu")
        button("Next",514,600,130,50,green,green_light,"Next")

        mouse_pos = pygame.mouse.get_pos()

        pygame.display.update()

def How_to_play2():
    How_to_play = True
    while How_to_play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(Space_Background,(P1,P2))

        Font = pygame.font.Font("freesansbold.ttf", 82)
        Text = Font.render("How to play", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),70)
        gameDisplay.blit(Text, Rect)
        
        Font = pygame.font.Font("freesansbold.ttf", 16)
        Text = Font.render("When Travelling from sector to sector, you must dodge asteroids.", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),300)
        gameDisplay.blit(Text, Rect)
        
        Font = pygame.font.Font("freesansbold.ttf", 16)
        Text = Font.render("Move your spaceship by using the left and right arrow keys.", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),400)
        gameDisplay.blit(Text, Rect)

        Font = pygame.font.Font("freesansbold.ttf", 16)
        Text = Font.render("Reach a certain score to make it through to the next sector!", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),500)
        gameDisplay.blit(Text, Rect)
        
        button("Main menu",254,600,130,50,green,green_light,"Main menu")
        
        mouse_pos = pygame.mouse.get_pos()

        pygame.display.update()

def player_score(count):
    Font = pygame.font.Font("freesansbold.ttf", 30)
    Text = Font.render("Score "+str(count), True, white)
    gameDisplay.blit(Text,(0, 0))

def vehicle(x, y):
    gameDisplay.blit(spaceship, (x, y))

def Blocks(block_x, block_y, block_width, block_height, colour):
    gameDisplay.blit(comet,(block_x, block_y, block_width, block_height))

def Rockets(rocket_x, rocket_y, rocket_width, rocket_height, colour):
    gameDisplay.blit(rocket,(rocket_x, rocket_y, rocket_width, rocket_height))

def Endless_crash():
    Endless_crash = True
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        Font = pygame.font.Font("freesansbold.ttf", 82)
        Text = Font.render("You Crashed!!!", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),70)
        gameDisplay.blit(Text, Rect)

        button("Play Again",450,600,130,50,green,green_light,"PlayEndless")
        button("Quit",650,600,130,50,red, red_light, "Quit")
        button("Main menu",250,600,130,50,green,green_light,"Main menu")

        pygame.display.update()

def Endless():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0
    y_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    
    rocket_width = 50
    rocket_height = 50
    rocket_x_start = random.randrange(0, (WindowWidth - rocket_width))
    rocket_y_start = -400
    rocket_speed = 4

    score=0
    Endless = True

    while Endless:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        if score <= 25:
            Blocks(block_x_start, block_y_start, block_width, block_height, white)
            block_y_start += block_speed
            vehicle(x, y)
            player_score(score)

        if score >= 25:
            Blocks(block_x_start, block_y_start, block_width, block_height, white)
            block_y_start += block_speed
            Rockets(rocket_x_start, rocket_y_start, rocket_width, rocket_height, white)
            rocket_y_start += rocket_speed
            vehicle(x, y)
            player_score(score)

        if y > WindowHeight - spaceship_height or y < 0:
            Endless_crash()

        if x > WindowWidth - spaceship_width or x < 0:
            Endless_crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if rocket_y_start > WindowHeight:
            rocket_y_start =0
            rocket_x_start = random.randrange(0, (WindowWidth - rocket_width))
            score += 1
            rocket_speed += 0.2
            if rocket_speed > 10:
                rocket_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                Endless_crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                Endless_crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                Endless_crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                Endless_crash()

        if y < rocket_y_start + rocket_height:
            if x > rocket_x_start and x < rocket_x_start + rocket_width or x + spaceship_width > rocket_x_start and x + spaceship_width < rocket_x_start + rocket_width:
                Endless_crash()
        if y < rocket_y_start + rocket_height:
            if x > rocket_x_start and x < rocket_x_start + rocket_width or x + spaceship_centre > rocket_x_start and x + spaceship_centre < rocket_x_start + rocket_width:
                Endless_crash()
        if y < rocket_y_start + rocket_height:
            if x > rocket_x_start and x < rocket_x_start + rocket_width or x + spaceship_centre_middle > rocket_x_start and x + spaceship_centre_middle < rocket_x_start + rocket_width:
                Endless_crash()
        if y < rocket_y_start + rocket_height:
            if x > rocket_x_start and x < rocket_x_start + rocket_width or x + spaceship_centre_side > rocket_x_start and x + spaceship_centre_side < rocket_x_start + rocket_width:
                Endless_crash()

        pygame.display.update()
        clock.tick(FPS)

def crash():
    crash = True
    while crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        Font = pygame.font.Font("freesansbold.ttf", 82)
        Text = Font.render("You Crashed!!!", True, white)
        Rect = Text.get_rect()
        Rect.center = ((WindowWidth/2),70)
        gameDisplay.blit(Text, Rect)

        button("Play Again",250,600,130,50,green,green_light,"Play")
        button("Quit",450,600,130,50,red, red_light, "Quit")

        pygame.display.update()
        
####Sector Travel; Asteroid Dodging Minigame
    
def Sector001_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 5:
            Sector001()

        pygame.display.update()
        clock.tick(FPS)

def Sector002_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 10:
            Sector002()

        pygame.display.update()
        clock.tick(FPS)

def Sector003_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 15:
            Sector003()

        pygame.display.update()
        clock.tick(FPS)

def Sector004_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 20:
            Sector004()

        pygame.display.update()
        clock.tick(FPS)

def Sector005_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10
                
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 25:
            Sector005()

        pygame.display.update()
        clock.tick(FPS)

def Sector006_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 30:
            Sector006()

        pygame.display.update()
        clock.tick(FPS)

def Sector007_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 35:
            Sector007()

        pygame.display.update()
        clock.tick(FPS)

def Sector008_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 40:
            Sector008()

        pygame.display.update()
        clock.tick(FPS)

def Sector009_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()
                
        if score == 45:
            Sector009()

        pygame.display.update()
        clock.tick(FPS)

def Sector010_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()
                
        if score == 50:
            Sector010()

        pygame.display.update()
        clock.tick(FPS)

def Sector011_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 55:
            Sector011()

        pygame.display.update()
        clock.tick(FPS)

def Sector012_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()
                
        if score == 60:
            Sector012()

        pygame.display.update()
        clock.tick(FPS)

def Sector013_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 65:
            Sector013()

        pygame.display.update()
        clock.tick(FPS)

def Sector014_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 70:
            Sector014()

        pygame.display.update()
        clock.tick(FPS)

def Sector015_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 75:
            Sector015()

        pygame.display.update()
        clock.tick(FPS)

def Sector016_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 80:
            Sector016()

        pygame.display.update()
        clock.tick(FPS)

def Sector017_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 85:
            Sector017()

        pygame.display.update()
        clock.tick(FPS)

def Sector018_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 90:
            Sector018()

        pygame.display.update()
        clock.tick(FPS)

def Sector019_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 95:
            Sector019()

        pygame.display.update()
        clock.tick(FPS)

def Sector020_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 100:
            Sector020()

        pygame.display.update()
        clock.tick(FPS)

def Sector021_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 105:
            Sector021()

        pygame.display.update()
        clock.tick(FPS)

def Sector022_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 110:
            Sector022()

        pygame.display.update()
        clock.tick(FPS)

def Sector023_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 115:
            Sector023()

        pygame.display.update()
        clock.tick(FPS)

def Sector024_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 120:
            Sector024()

        pygame.display.update()
        clock.tick(FPS)

def Sector025_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 125:
            Sector025()

        pygame.display.update()
        clock.tick(FPS)

def Sector026_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 130:
            Sector026()

        pygame.display.update()
        clock.tick(FPS)

def Sector027_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 135:
            Sector027()

        pygame.display.update()
        clock.tick(FPS)

def Sector028_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 140:
            Sector028()

        pygame.display.update()
        clock.tick(FPS)

def Sector029_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 145:
            Sector029()

        pygame.display.update()
        clock.tick(FPS)

def Sector030_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 150:
            Sector030()

        pygame.display.update()
        clock.tick(FPS)

def Sector031_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 155:
            Sector031()

        pygame.display.update()
        clock.tick(FPS)

def Sector032_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 160:
            Sector032()

        pygame.display.update()
        clock.tick(FPS)

def Sector033_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 165:
            Sector033()

        pygame.display.update()
        clock.tick(FPS)

def Sector034_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 170:
            Sector034()

        pygame.display.update()
        clock.tick(FPS)

def Sector035_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 175:
            Sector035()

        pygame.display.update()
        clock.tick(FPS)

def Sector036_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 180:
            Sector036()

        pygame.display.update()
        clock.tick(FPS)

def Sector037_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 185:
            Sector037()

        pygame.display.update()
        clock.tick(FPS)

def Sector038_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 190:
            Sector038()

        pygame.display.update()
        clock.tick(FPS)

def Sector039_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 195:
            Sector039()

        pygame.display.update()
        clock.tick(FPS)

def Sector040_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 200:
            Sector040()

        pygame.display.update()
        clock.tick(FPS)

def Sector041_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 205:
            Sector041()

        pygame.display.update()
        clock.tick(FPS)

def Sector042_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 210:
            Sector042()

        pygame.display.update()
        clock.tick(FPS)

def Sector043_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 215:
            Sector043()

        pygame.display.update()
        clock.tick(FPS)

def Sector044_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 220:
            Sector044()

        pygame.display.update()
        clock.tick(FPS)

def Sector045_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 225:
            Sector045()

        pygame.display.update()
        clock.tick(FPS)

def Sector046_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 230:
            Sector046()

        pygame.display.update()
        clock.tick(FPS)

def Sector047_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.2
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 235:
            Sector047()

        pygame.display.update()
        clock.tick(FPS)

def Sector048_Travel():
    global pause
    x = (WindowWidth * 0.4)
    y = (WindowHeight * 0.8)
    x_change = 0

    block_width = 50
    block_height = 50
    block_x_start = random.randrange(0, (WindowWidth - block_width))
    block_y_start = -400
    block_speed = 4
    score=0

    Sector_Travel = True

    while Sector_Travel:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        x_change = -10
                elif event.key == pygame.K_RIGHT:
                        x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

        x += x_change
        gameDisplay.blit(Space_Background,(P1,P2))

        Blocks(block_x_start, block_y_start, block_width, block_height, white)
        block_y_start += block_speed
        vehicle(x, y)
        player_score(score)

        if x > WindowWidth - spaceship_width or x < 0:
            crash()
            
        if block_y_start > WindowHeight:
            block_y_start =0
            block_x_start = random.randrange(0, (WindowWidth - block_width))
            score += 1
            block_speed += 0.1
            if block_speed > 10:
                block_speed = 10

        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_width > block_x_start and x + spaceship_width < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre > block_x_start and x + spaceship_centre < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_middle > block_x_start and x + spaceship_centre_middle < block_x_start + block_width:
                crash()
        if y < block_y_start + block_height:
            if x > block_x_start and x < block_x_start + block_width or x + spaceship_centre_side > block_x_start and x + spaceship_centre_side < block_x_start + block_width:
                crash()

        if score == 240:
            Sector048()

        pygame.display.update()
        clock.tick(FPS)

####Sector Space      

def Sector001():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        #Planets
        ##Green
        pygame.draw.circle(gameDisplay, green, (200, 25), 20, 0)
        ##Yellow
        pygame.draw.circle(gameDisplay, yellow, (100, 35), 7, 0)
        #Space Stations
        pygame.draw.rect(gameDisplay, grey, (50,25,10,10))

        Sector_Space("S2",256,0,256,64,green,green_light,"S2")
        Sector_Space("S5",0,64,256,64,green,green_light,"S5")
        
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector002():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, red,(360, 25), 10, 0)

        Sector_Space("S1",0,0,256,64,green,green_light,"S1")
        Sector_Space("S6",256,64,256,64,green,green_light,"S6")
        Sector_Space("S3",512,0,256,64,green,green_light,"S3")
        
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector003():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S2",256,0,256,64,green,green_light,"S2")
        Sector_Space("S7",512,64,256,64,green,green_light,"S7")
        Sector_Space("S4",768,0,256,64,green,green_light,"S4")
        
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector004():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (860,25,10,10))

        Sector_Space("S3",512,0,256,64,green,green_light,"S3")
        Sector_Space("S8",768,64,256,64,green,green_light,"S8")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector005():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S1",0,0,256,64,green,green_light,"S1")
        Sector_Space("S6",256,64,256,64,green,green_light,"S6")
        Sector_Space("S9",0,128,256,64,green,green_light,"S9")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector006():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S2",256,0,256,64,green,green_light,"S2")
        Sector_Space("S5",0,64,256,64,green,green_light,"S5")
        Sector_Space("S7",512,64,256,64,green,green_light,"S7")
        Sector_Space("S10",256,128,256,64,green,green_light,"S10")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector007():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, yellow, (720, 100), 7, 0)

        Sector_Space("S3",512,0,256,64,green,green_light,"S3")
        Sector_Space("S6",256,64,256,64,green,green_light,"S6")
        Sector_Space("S11",512,128,256,64,green,green_light,"S11")
        Sector_Space("S8",768,64,256,64,green,green_light,"S8")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector008():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S4",768,0,256,64,green,green_light,"S4")
        Sector_Space("S7",512,64,256,64,green,green_light,"S7")
        Sector_Space("S12",768,128,256,64,green,green_light,"S12")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector009():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S5",0,64,256,64,green,green_light,"S5")
        Sector_Space("S10",256,128,256,64,green,green_light,"S10")
        Sector_Space("S13",0,192,256,64,green,green_light,"S13")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector010():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (470,150,10,10))

        Sector_Space("S9",0,128,256,64,green,green_light,"S9")
        Sector_Space("S11",512,128,256,64,green,green_light,"S11")
        Sector_Space("S14",256,192,256,64,green,green_light,"S14")
        Sector_Space("S6",256,64,256,64,green,green_light,"S6")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector011():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, red,(700, 160), 20, 0)

        Sector_Space("S10",256,128,256,64,green,green_light,"S10")
        Sector_Space("S7",512,64,256,64,green,green_light,"S7")
        Sector_Space("S12",768,128,256,64,green,green_light,"S12")
        Sector_Space("S15",512,192,256,64,green,green_light,"S15")
        
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector012():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, green, (900, 160), 15, 0)

        Sector_Space("S11",512,128,256,64,green,green_light,"S11")
        Sector_Space("S8",768,64,256,64,green,green_light,"S8")
        Sector_Space("S16",768,192,256,64,green,green_light,"S16")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector013():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S9",0,128,256,64,green,green_light,"S9")
        Sector_Space("S14",256,192,256,64,green,green_light,"S14")
        Sector_Space("S17",0,256,256,64,green,green_light,"S17")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector014():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, yellow, (350, 220), 7, 0)
        pygame.draw.circle(gameDisplay, green, (400, 220), 10, 0)

        Sector_Space("S13",0,192,256,64,green,green_light,"S13")
        Sector_Space("S10",256,128,256,64,green,green_light,"S10")
        Sector_Space("S15",512,192,256,64,green,green_light,"S15")
        Sector_Space("S18",256,256,256,64,green,green_light,"S18")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector015():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S11",512,128,256,64,green,green_light,"S11")
        Sector_Space("S14",256,192,256,64,green,green_light,"S14")
        Sector_Space("S19",512,256,256,64,green,green_light,"S19")
        Sector_Space("S16",768,192,256,64,green,green_light,"S16")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector016():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S12",768,128,256,64,green,green_light,"S12")
        Sector_Space("S15",512,192,256,64,green,green_light,"S15")
        Sector_Space("S20",768,256,256,64,green,green_light,"S20")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector017():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S13",0,192,256,64,green,green_light,"S13")
        Sector_Space("S18",256,256,256,64,green,green_light,"S18")
        Sector_Space("S21",0,320,256,64,green,green_light,"S21")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector018():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S17",0,256,256,64,green,green_light,"S17")
        Sector_Space("S14",256,192,256,64,green,green_light,"S14")
        Sector_Space("S19",512,256,256,64,green,green_light,"S19")
        Sector_Space("S22",256,320,256,64,green,green_light,"S22")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector019():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S15",512,192,256,64,green,green_light,"S15")
        Sector_Space("S18",256,256,256,64,green,green_light,"S18")
        Sector_Space("S23",512,320,256,64,green,green_light,"S23")
        Sector_Space("S20",768,256,256,64,green,green_light,"S20")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector020():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S16",768,192,256,64,green,green_light,"S16")
        Sector_Space("S19",512,256,256,64,green,green_light,"S19")
        Sector_Space("S24",768,320,256,64,green,green_light,"S24")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector021():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S17",0,256,256,64,green,green_light,"S17")
        Sector_Space("S22",256,320,256,64,green,green_light,"S22")
        Sector_Space("S25",0,384,256,64,green,green_light,"S25")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector022():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S21",0,320,256,64,green,green_light,"S21")
        Sector_Space("S18",256,256,256,64,green,green_light,"S18")
        Sector_Space("S23",512,320,256,64,green,green_light,"S23")
        Sector_Space("S26",256,384,256,64,green,green_light,"S26")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector023():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (650,340,10,10))

        Sector_Space("S22",256,320,256,64,green,green_light,"S22")
        Sector_Space("S19",512,256,256,64,green,green_light,"S19")
        Sector_Space("S24",768,320,256,64,green,green_light,"S24")
        Sector_Space("S27",512,384,256,64,green,green_light,"S27")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector024():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S20",768,256,256,64,green,green_light,"S20")
        Sector_Space("S23",512,320,256,64,green,green_light,"S23")
        Sector_Space("S28",768,384,256,64,green,green_light,"S28")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector025():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (50,400,10,10))

        Sector_Space("S21",0,320,256,64,green,green_light,"S21")
        Sector_Space("S26",256,384,256,64,green,green_light,"S26")
        Sector_Space("S29",0,448,256,64,green,green_light,"S29")
        
        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector026():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S22",256,320,256,64,green,green_light,"S22")
        Sector_Space("S25",0,384,256,64,green,green_light,"S25")
        Sector_Space("S27",512,384,256,64,green,green_light,"S27")
        Sector_Space("S30",256,448,256,64,green,green_light,"S30")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector027():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S26",256,384,256,64,green,green_light,"S26")
        Sector_Space("S23",512,320,256,64,green,green_light,"S23")
        Sector_Space("S28",768,384,256,64,green,green_light,"S28")
        Sector_Space("S31",512,448,256,64,green,green_light,"S31")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector028():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, yellow, (900, 430), 7, 0)
        pygame.draw.rect(gameDisplay, grey, (900,400,10,10))

        Sector_Space("S27",512,384,256,64,green,green_light,"S27")
        Sector_Space("S24",768,320,256,64,green,green_light,"S24")
        Sector_Space("S32",768,448,256,64,green,green_light,"S32")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector029():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S25",0,384,256,64,green,green_light,"S25")
        Sector_Space("S30",256,448,256,64,green,green_light,"S30")
        Sector_Space("S33",0,512,256,64,green,green_light,"S33")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector030():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (360,475,10,10))

        Sector_Space("S26",256,384,256,64,green,green_light,"S26")
        Sector_Space("S29",0,448,256,64,green,green_light,"S29")
        Sector_Space("S31",512,448,256,64,green,green_light,"S31")
        Sector_Space("S34",256,512,256,64,green,green_light,"S34")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector031():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S30",256,448,256,64,green,green_light,"S30")
        Sector_Space("S27",512,384,256,64,green,green_light,"S27")
        Sector_Space("S32",768,448,256,64,green,green_light,"S32")
        Sector_Space("S35",512,512,256,64,green,green_light,"S35")
        

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector032():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S31",512,448,256,64,green,green_light,"S31")
        Sector_Space("S28",768,384,256,64,green,green_light,"S28")
        Sector_Space("S36",768,512,256,64,green,green_light,"S36")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector033():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, green, (100, 550), 5, 0)
        pygame.draw.circle(gameDisplay, red,(200, 550), 10, 0)

        Sector_Space("S34",256,512,256,64,green,green_light,"S34")
        Sector_Space("S29",0,448,256,64,green,green_light,"S29")
        Sector_Space("S37",0,576,256,64,green,green_light,"S37")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector034():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        

        Sector_Space("S33",0,512,256,64,green,green_light,"S33")
        Sector_Space("S30",256,448,256,64,green,green_light,"S30")
        Sector_Space("S35",512,512,256,64,green,green_light,"S35")
        Sector_Space("S38",256,576,256,64,green,green_light,"S38")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector035():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S34",256,512,256,64,green,green_light,"S34")
        Sector_Space("S31",512,448,256,64,green,green_light,"S31")
        Sector_Space("S36",768,512,256,64,green,green_light,"S36")
        Sector_Space("S39",512,576,256,64,green,green_light,"S39")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector036():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S35",512,512,256,64,green,green_light,"S35")
        Sector_Space("S32",768,448,256,64,green,green_light,"S32")
        Sector_Space("S40",768,576,256,64,green,green_light,"S40")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector037():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S33",0,512,256,64,green,green_light,"S33")
        Sector_Space("S38",256,576,256,64,green,green_light,"S38")
        Sector_Space("S41",0,640,256,64,green,green_light,"S41")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector038():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (360,600,10,10))

        Sector_Space("S37",0,576,256,64,green,green_light,"S37")
        Sector_Space("S34",256,512,256,64,green,green_light,"S34")
        Sector_Space("S39",512,576,256,64,green,green_light,"S39")
        Sector_Space("S42",256,640,256,64,green,green_light,"S42")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector039():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, green, (720, 610), 25, 0)

        Sector_Space("S38",256,576,256,64,green,green_light,"S38")
        Sector_Space("S35",512,512,256,64,green,green_light,"S35")
        Sector_Space("S40",768,576,256,64,green,green_light,"S40")
        Sector_Space("S43",512,640,256,64,green,green_light,"S43")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector040():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, red,(900, 610), 5, 0)

        Sector_Space("S39",512,576,256,64,green,green_light,"S39")
        Sector_Space("S36",768,512,256,64,green,green_light,"S36")
        Sector_Space("S44",768,640,256,64,green,green_light,"S44")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector041():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (50,660,10,10))

        Sector_Space("S37",0,576,256,64,green,green_light,"S37")
        Sector_Space("S42",256,640,256,64,green,green_light,"S42")
        Sector_Space("S45",0,704,256,64,green,green_light,"S45")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector042():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S41",0,640,256,64,green,green_light,"S41")
        Sector_Space("S38",256,576,256,64,green,green_light,"S38")
        Sector_Space("S43",512,640,256,64,green,green_light,"S43")
        Sector_Space("S46",256,704,256,64,green,green_light,"S46")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector043():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (650,680,10,10))
        pygame.draw.circle(gameDisplay, yellow, (700, 680), 7, 0)

        Sector_Space("S42",256,640,256,64,green,green_light,"S42")
        Sector_Space("S39",512,576,256,64,green,green_light,"S39")
        Sector_Space("S44",768,640,256,64,green,green_light,"S44")
        Sector_Space("S47",512,704,256,64,green,green_light,"S47")
        

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector044():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.rect(gameDisplay, grey, (900,660,10,10))

        Sector_Space("S43",512,640,256,64,green,green_light,"S43")
        Sector_Space("S40",768,576,256,64,green,green_light,"S40")
        Sector_Space("S48",768,704,256,64,green,green_light,"S48")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector045():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S41",0,640,256,64,green,green_light,"S41")
        Sector_Space("S46",256,704,256,64,green,green_light,"S46")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector046():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        pygame.draw.circle(gameDisplay, red,(300, 735), 25, 0)

        Sector_Space("S45",0,704,256,64,green,green_light,"S45")
        Sector_Space("S42",256,640,256,64,green,green_light,"S42")
        Sector_Space("S47",512,704,256,64,green,green_light,"S47")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector047():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

        Sector_Space("S46",256,704,256,64,green,green_light,"S46")
        Sector_Space("S43",512,640,256,64,green,green_light,"S43")
        Sector_Space("S48",768,704,256,64,green,green_light,"S48")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

def Sector048():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(Space_Background,(P1,P2))

        #Lines Across
        pygame.draw.line(gameDisplay, white, (0,0), (1024,0), 5)
        pygame.draw.line(gameDisplay, white, (0,64), (1024,64), 5)
        pygame.draw.line(gameDisplay, white, (0,128), (1024,128), 5)
        pygame.draw.line(gameDisplay, white, (0,192), (1024,192), 5)
        pygame.draw.line(gameDisplay, white, (0,256), (1024,256), 5)
        pygame.draw.line(gameDisplay, white, (0,320), (1024,320), 5)
        pygame.draw.line(gameDisplay, white, (0,384), (1024,384), 5)
        pygame.draw.line(gameDisplay, white, (0,448), (1024,448), 5)
        pygame.draw.line(gameDisplay, white, (0,512), (1024,512), 5)
        pygame.draw.line(gameDisplay, white, (0,576), (1024,576), 5)
        pygame.draw.line(gameDisplay, white, (0,640), (1024,640), 5)
        pygame.draw.line(gameDisplay, white, (0,704), (1024,704), 5)
        pygame.draw.line(gameDisplay, white, (0,768), (1024,768), 5)
        #Lines Down
        pygame.draw.line(gameDisplay, white, (0,0), (0,768), 5)
        pygame.draw.line(gameDisplay, white, (256,0), (256,768), 5)
        pygame.draw.line(gameDisplay, white, (512,0), (512,768), 5)
        pygame.draw.line(gameDisplay, white, (768,0), (768,768), 5)
        pygame.draw.line(gameDisplay, white, (1024,0), (1024,768), 5)

         #Planets
        ##Green
        pygame.draw.circle(gameDisplay, green, (200, 25), 20, 0)
        pygame.draw.circle(gameDisplay, green, (900, 160), 15, 0)
        pygame.draw.circle(gameDisplay, green, (400, 220), 10, 0)
        pygame.draw.circle(gameDisplay, green, (100, 550), 5, 0)
        pygame.draw.circle(gameDisplay, green, (720, 610), 25, 0)
        ##Yellow
        pygame.draw.circle(gameDisplay, yellow, (100, 35), 7, 0)
        pygame.draw.circle(gameDisplay, yellow, (720, 100), 7, 0)
        pygame.draw.circle(gameDisplay, yellow, (350, 220), 7, 0)
        pygame.draw.circle(gameDisplay, yellow, (900, 430), 7, 0)
        pygame.draw.circle(gameDisplay, yellow, (700, 680), 7, 0)
        ##Red
        pygame.draw.circle(gameDisplay, red,(360, 25), 15, 0)
        pygame.draw.circle(gameDisplay, red,(700, 160), 20, 0)
        pygame.draw.circle(gameDisplay, red,(200, 550), 10, 0)
        pygame.draw.circle(gameDisplay, red,(900, 610), 5, 0)
        pygame.draw.circle(gameDisplay, red,(300, 735), 25, 0)
        ##Purple
        pygame.draw.circle(gameDisplay, purple,(900,735), 25, 0)

        #Space Stations
        pygame.draw.rect(gameDisplay, grey, (50,25,10,10))
        pygame.draw.rect(gameDisplay, grey, (860,25,10,10))
        pygame.draw.rect(gameDisplay, grey, (470,150,10,10))
        pygame.draw.rect(gameDisplay, grey, (650,340,10,10))
        pygame.draw.rect(gameDisplay, grey, (50,400,10,10))
        pygame.draw.rect(gameDisplay, grey, (900,400,10,10))
        pygame.draw.rect(gameDisplay, grey, (360,475,10,10))
        pygame.draw.rect(gameDisplay, grey, (360,600,10,10))
        pygame.draw.rect(gameDisplay, grey, (50,660,10,10))
        pygame.draw.rect(gameDisplay, grey, (650,680,10,10))
        pygame.draw.rect(gameDisplay, grey, (900,660,10,10))

        Sector_Space("S1",0,0,256,64,green,green_light,"S1")
        Sector_Space("S2",256,0,256,64,green,green_light,"S2")
        Sector_Space("S3",512,0,256,64,green,green_light,"S3")
        Sector_Space("S4",768,0,256,64,green,green_light,"S4")
        Sector_Space("S5",0,64,256,64,green,green_light,"S5")
        Sector_Space("S6",256,64,256,64,green,green_light,"S6")
        Sector_Space("S7",512,64,256,64,green,green_light,"S7")
        Sector_Space("S8",768,64,256,64,green,green_light,"S8")
        Sector_Space("S9",0,128,256,64,green,green_light,"S9")
        Sector_Space("S10",256,128,256,64,green,green_light,"S10")
        Sector_Space("S11",512,128,256,64,green,green_light,"S11")
        Sector_Space("S12",768,128,256,64,green,green_light,"S12")
        Sector_Space("S13",0,192,256,64,green,green_light,"S13")
        Sector_Space("S14",256,192,256,64,green,green_light,"S14")
        Sector_Space("S15",512,192,256,64,green,green_light,"S15")
        Sector_Space("S16",768,192,256,64,green,green_light,"S16")
        Sector_Space("S17",0,256,256,64,green,green_light,"S17")
        Sector_Space("S18",256,256,256,64,green,green_light,"S18")
        Sector_Space("S19",512,256,256,64,green,green_light,"S19")
        Sector_Space("S20",768,256,256,64,green,green_light,"20")
        Sector_Space("S21",0,320,256,64,green,green_light,"21")
        Sector_Space("S22",256,320,256,64,green,green_light,"S22")
        Sector_Space("S23",512,320,256,64,green,green_light,"S23")
        Sector_Space("S24",768,320,256,64,green,green_light,"S24")
        Sector_Space("S25",0,384,256,64,green,green_light,"S25")
        Sector_Space("S26",256,384,256,64,green,green_light,"S26")
        Sector_Space("S27",512,384,256,64,green,green_light,"S27")
        Sector_Space("S28",768,384,256,64,green,green_light,"S28")
        Sector_Space("S29",0,448,256,64,green,green_light,"S29")
        Sector_Space("S30",256,448,256,64,green,green_light,"S30")
        Sector_Space("S31",512,448,256,64,green,green_light,"S31")
        Sector_Space("S32",768,448,256,64,green,green_light,"S32")
        Sector_Space("S33",0,512,256,64,green,green_light,"S33")
        Sector_Space("S34",256,512,256,64,green,green_light,"S34")
        Sector_Space("S35",512,512,256,64,green,green_light,"S35")
        Sector_Space("S36",768,512,256,64,green,green_light,"S36")
        Sector_Space("S37",0,576,256,64,green,green_light,"S37")
        Sector_Space("S38",256,576,256,64,green,green_light,"S38")
        Sector_Space("S39",512,576,256,64,green,green_light,"S39")
        Sector_Space("S40",768,576,256,64,green,green_light,"S40")
        Sector_Space("S41",0,640,256,64,green,green_light,"S41")
        Sector_Space("S42",256,640,256,64,green,green_light,"S42")
        Sector_Space("S43",512,640,256,64,green,green_light,"S43")
        Sector_Space("S44",768,640,256,64,green,green_light,"S44")
        Sector_Space("S45",0,704,256,64,green,green_light,"S45")
        Sector_Space("S46",256,704,256,64,green,green_light,"S46")
        Sector_Space("S47",512,704,256,64,green,green_light,"S47")
##        Sector_Space("S48",768,704,256,64,green,green_light,"S48")

        mouse_pos = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(60)

pygame.mixer.music.play(-1,0.0)
Game_Intro()
clock.tick(FPS)
