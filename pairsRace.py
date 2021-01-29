import pygame
import os
import graphicModule

pygame.init()


WIN = pygame.display.set_mode(graphicModule.SIZE['window'])
pygame.display.set_caption('Pairs Race')




def draw():
    
    WIN.fill(graphicModule.COLORS['white'])
    WIN.blit(graphicModule.IMAGE['background'], graphicModule.POSITION['background'])
    '''
    WIN.blit(graphicModule.TEXT['play'], graphicModule.POSITION['text_play'])
    WIN.blit(graphicModule.BUTTON['play'], graphicModule.POSITION['play_button'])
    
    WIN.blit(graphicModule.IMAGE['header'], graphicModule.POSITION['header'])
    '''
    
    WIN.blit(graphicModule.TEXT['time'], graphicModule.POSITION['text_time'])

    
    WIN.blit(graphicModule.BUTTON['next'], graphicModule.POSITION['next_button'])
    
    WIN.blit(graphicModule.BUTTON['success'], graphicModule.POSITION['success_icon'])
    #WIN.blit(graphicModule.BUTTON['fail'], graphicModule.POSITION['fail_icon'])


    '''
    pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow1'])
    WIN.blit(graphicModule.IMAGE['img1'], graphicModule.POSITION['img1'])
    pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow2'])
    WIN.blit(graphicModule.IMAGE['img2'], graphicModule.POSITION['img2'])

    pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow3'])
    WIN.blit(graphicModule.IMAGE['img2'], graphicModule.POSITION['img3'])
    pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow4'])
    WIN.blit(graphicModule.IMAGE['img3'], graphicModule.POSITION['img4'])

    pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow5'])
    WIN.blit(graphicModule.IMAGE['img3'], graphicModule.POSITION['img5'])
    pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow6'])
    WIN.blit(graphicModule.IMAGE['img1'], graphicModule.POSITION['img6'])
    '''


    pygame.draw.rect(WIN, graphicModule.COLORS['black'], graphicModule.IMAGE['shadow1'])
    pygame.draw.rect(WIN, graphicModule.COLORS['grey'], graphicModule.IMAGE['backside1'])
    WIN.blit(graphicModule.IMAGE['tire'], graphicModule.POSITION['tire1'])

    pygame.draw.rect(WIN, graphicModule.COLORS['black'], graphicModule.IMAGE['shadow2'])
    pygame.draw.rect(WIN, graphicModule.COLORS['grey'], graphicModule.IMAGE['backside2'])
    WIN.blit(graphicModule.IMAGE['tire'], graphicModule.POSITION['tire2'])

    pygame.draw.rect(WIN, graphicModule.COLORS['black'], graphicModule.IMAGE['shadow3'])
    pygame.draw.rect(WIN, graphicModule.COLORS['grey'], graphicModule.IMAGE['backside3'])
    WIN.blit(graphicModule.IMAGE['tire'], graphicModule.POSITION['tire3'])

    pygame.draw.rect(WIN, graphicModule.COLORS['black'], graphicModule.IMAGE['shadow4'])
    pygame.draw.rect(WIN, graphicModule.COLORS['grey'], graphicModule.IMAGE['backside4'])
    WIN.blit(graphicModule.IMAGE['tire'], graphicModule.POSITION['tire4'])

    pygame.draw.rect(WIN, graphicModule.COLORS['black'], graphicModule.IMAGE['shadow5'])
    pygame.draw.rect(WIN, graphicModule.COLORS['grey'], graphicModule.IMAGE['backside5'])
    WIN.blit(graphicModule.IMAGE['tire'], graphicModule.POSITION['tire5'])

    pygame.draw.rect(WIN, graphicModule.COLORS['black'], graphicModule.IMAGE['shadow6'])
    pygame.draw.rect(WIN, graphicModule.COLORS['grey'], graphicModule.IMAGE['backside6'])
    WIN.blit(graphicModule.IMAGE['tire'], graphicModule.POSITION['tire6'])


    '''
    WIN.blit(graphicModule.TEXT['result'], graphicModule.POSITION['text_result'])
    WIN.blit(graphicModule.BUTTON['home'], graphicModule.POSITION['home_button'])
    '''
    pygame.display.update()

def main():

    run = True
    clock = pygame.time.Clock()

    while run:

        clock.tick(graphicModule.FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

        draw()

    pygame.quit()

main()