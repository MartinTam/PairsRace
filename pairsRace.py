import pygame
import os

pygame.init()


FPS = 60

WHITE = (255, 255, 255)

SIZE =  {
            'window' : (1000, 700),
            'play_button' : (100, 110),
            'next_button' : (200, 200),
            'success_icon' : (80,80),
            'fail_icon' : (80,80),
            'home_button' : (100,100)

        }


POSITION =  {   
                'background' : (0,0),
                'text_play' : (430,230),
                'play_button' : (445,295),
                'header' : (301,50),
                'text_time' : (15,15),
                'next_button' : (775,525),
                'success_icon' : (460,23),
                'fail_icon' : (460,23),

                'img1' : (270, 135),
                'img2' : (520, 135),
                'img3' : (270, 308),
                'img4' : (520, 308),
                'img5' : (270, 481),
                'img6' : (520, 481),

                'text_result' : (325,230),
                'home_button' : (445,395)
            }










WIN = pygame.display.set_mode(SIZE['window'])
pygame.display.set_caption('Pairs Race')

BG = pygame.image.load(os.path.join('images', 'background.jpeg'))

IMG1 = pygame.image.load(os.path.join('images', '01.jpeg'))
IMG2 = pygame.image.load(os.path.join('images', '02.jpeg'))
IMG3 = pygame.image.load(os.path.join('images', '03.jpeg'))

HEADER = pygame.image.load(os.path.join('images', 'header.png'))

PLAY_ORG = pygame.image.load(os.path.join('images', 'play.png'))
PLAY = pygame.transform.scale( PLAY_ORG, SIZE['play_button'] )

FONT = pygame.font.SysFont('comicsans', 70)
TEXT_PLAY = FONT.render('PLAY', True, WHITE)

TEXT_TIME = FONT.render('00:00:00', True, WHITE)

NEXT_ORG = pygame.image.load(os.path.join('images', 'next.png'))
NEXT = pygame.transform.scale(NEXT_ORG, SIZE['next_button'])

SUCCESS_ORG = pygame.image.load(os.path.join('images', 'success.png'))
SUCCESS = pygame.transform.scale(SUCCESS_ORG, SIZE['success_icon'])

FAIL_ORG = pygame.image.load(os.path.join('images', 'fail.png'))
FAIL = pygame.transform.scale(FAIL_ORG, SIZE['fail_icon'])

HOME_ORG = pygame.image.load(os.path.join('images', 'home.png'))
HOME = pygame.transform.scale(HOME_ORG, SIZE['home_button'])

TEXT_RESULT = FONT.render('Time: 00:00:00', True, WHITE)

def draw():
    
    WIN.fill(WHITE)
    WIN.blit(BG, POSITION['background'])
    
    WIN.blit(TEXT_PLAY, POSITION['text_play'])
    WIN.blit(PLAY, POSITION['play_button'])
    
    WIN.blit(HEADER, POSITION['header'])

    '''
    WIN.blit(TEXT_TIME, POSITION['text_time'])

    
    WIN.blit(NEXT, POSITION['next_button'])
    
    WIN.blit(SUCCESS, POSITION['success_icon'])
    WIN.blit(FAIL, POSITION['fail_icon'])

    WIN.blit(IMG1, POSITION['img1'])
    WIN.blit(IMG2, POSITION['img2'])

    WIN.blit(IMG2, POSITION['img3'])
    WIN.blit(IMG3, POSITION['img4'])

    WIN.blit(IMG3, POSITION['img5'])
    WIN.blit(IMG1, POSITION['img6'])
    
    WIN.blit(TEXT_RESULT, POSITION['text_result'])
    WIN.blit(HOME, POSITION['home_button'])
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