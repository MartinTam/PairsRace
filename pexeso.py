import pygame
import os

pygame.init()

WIDTH = 1000
HEIGHT = 700

FPS = 60

WHITE = (255, 255, 255)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pexeso')

BG = pygame.image.load(os.path.join('images', 'background.jpeg'))

IMG1 = pygame.image.load(os.path.join('images', '01.jpeg'))
IMG2 = pygame.image.load(os.path.join('images', '02.jpeg'))
IMG3 = pygame.image.load(os.path.join('images', '03.jpeg'))

HEADER = pygame.image.load(os.path.join('images', 'header.png'))

PLAY_ORG = pygame.image.load(os.path.join('images', 'play.png'))
PLAY = pygame.transform.scale( PLAY_ORG, (100, 110) )

FONT = pygame.font.SysFont('comicsans', 70)
TEXT_PLAY = FONT.render('PLAY', True, WHITE)

TEXT_TIME = FONT.render('00:00:00', True, WHITE)

NEXT_ORG = pygame.image.load(os.path.join('images', 'next.png'))
NEXT = pygame.transform.scale(NEXT_ORG, (200, 200))

SUCCESS_ORG = pygame.image.load(os.path.join('images', 'success.png'))
SUCCESS = pygame.transform.scale(SUCCESS_ORG, (80,80))

FAIL_ORG = pygame.image.load(os.path.join('images', 'fail.png'))
FAIL = pygame.transform.scale(FAIL_ORG, (80,80))

HOME_ORG = pygame.image.load(os.path.join('images', 'home.png'))
HOME = pygame.transform.scale(HOME_ORG, (100,100))

TEXT_RESULT = FONT.render('Time: 00:00:00', True, WHITE)

def draw():
    
    WIN.fill(WHITE)
    WIN.blit(BG, (0,0))
    
    WIN.blit(TEXT_PLAY, (430,230))
    WIN.blit(PLAY, (445,295))
    
    WIN.blit(HEADER, (301,50))

    '''
    WIN.blit(TEXT_TIME, (15,15))

    
    WIN.blit(NEXT, (775,525))
    
    WIN.blit(SUCCESS, (460,23))
    #WIN.blit(FAIL, (460,23))

    WIN.blit(IMG1, (270, 135))
    WIN.blit(IMG2, (520, 135))

    WIN.blit(IMG2, (270, 308))
    WIN.blit(IMG3, (520, 308))

    WIN.blit(IMG3, (270, 481))
    WIN.blit(IMG1, (520, 481))
    
    WIN.blit(TEXT_RESULT, (325,230))
    WIN.blit(HOME, (445,395))
    '''
    pygame.display.update()

def main():

    run = True
    clock = pygame.time.Clock()

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        draw()

    pygame.quit()

main()