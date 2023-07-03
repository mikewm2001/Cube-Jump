import pygame
import os
pygame.font.init()
import random


WIDTH = 1280
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My GeoDash")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

FPS = 60
VEL = 5

END_FONT = pygame.font.SysFont('comicsans', 60)

GROUND = pygame.Rect(0, (HEIGHT//2 + 50), WIDTH, 10)
CUBE = pygame.Rect(100, (HEIGHT//2), 50, 50)





def draw_window(obstacles):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, GROUND)
    pygame.draw.rect(WIN, BLUE, CUBE)
    for OBJECT in obstacles:
        pygame.draw.rect(WIN, RED, OBJECT)
    pygame.display.update()

def handle_jump(upCount, downCount, isJump):
    if isJump:
        if upCount > 0 and upCount <= 22:
            #print(upCount)
            CUBE.y -= int(upCount * 0.5)
            #print(CUBE.y)
            upCount -= 1
            print(upCount)
        elif downCount > 0 and downCount <= 22:
            CUBE.y += int(downCount * 0.5)
            downCount += 1
        else:
            #print(upCount)
            #print(downCount)
            isJump = False
            upCount = 22
            downCount = 1


def handle_obstacles(obstacles):
    for OBJECT in obstacles:
        OBJECT.x -= 5
    
#def handle_end(obstacles):
    #global finished
    #for OBJECT in obstacles:
        #if CUBE.colliderect(OBJECT):
            #finished = True
            #winner_text = "YOU LOSE"
            #end_text = END_FONT.render(winner_text, 1, RED)
            #WIN.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, 150))
            #pygame.display.update()
            #pygame.time.delay(5000)

def main():
    finished = False
    upCount = 22
    downCount = 1
    isJump = False
    obstacles = []
    spawnCounter = 2000

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isJump = True
        if pygame.time.get_ticks() > spawnCounter and pygame.time.get_ticks() < spawnCounter + 100: # THIS IS WHERE THE PROBLEM IS
            OBJECT = pygame.Rect(1230, (HEIGHT//2), 50, 50)
            obstacles.append(OBJECT)
            spawnCounter += 2000 
            #print(obstacles)
        handle_obstacles(obstacles)
        #handle_jump(upCount, downCount, isJump)
        if isJump:
            if upCount > 0 and upCount <= 22:
                #print(upCount)
                CUBE.y -= int(upCount * 0.5)
                #print(CUBE.y)
                upCount -= 1
                #print(upCount)
            elif downCount > 0 and downCount <= 22:
                CUBE.y += int(downCount * 0.5)
                downCount += 1
            else:
                #print(upCount)
                #print(downCount)
                isJump = False
                upCount = 22
                downCount = 1
        draw_window(obstacles)
        #handle_end(obstacles)
        for OBJECT in obstacles:
            if CUBE.colliderect(OBJECT):
                finished = True
                winner_text = "YOU LOSE"
                end_text = END_FONT.render(winner_text, 1, RED)
                WIN.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, 150))
                pygame.display.update()
                spawnCounter += 5000
                pygame.time.delay(5000)
        if finished == True:
            break
        print(pygame.time.get_ticks())
    #isJump = False
    #global upCount, downCount
    #upCount = 22
    #downCount = 1
    main()


if __name__ == "__main__":
    main()