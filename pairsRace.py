import pygame
import os
import graphicModule

pygame.init()


WIN = pygame.display.set_mode(graphicModule.SIZE['window'])
pygame.display.set_caption('Pairs Race')


def draw():
    
    WIN.fill(graphicModule.WHITE)
    WIN.blit(graphicModule.IMAGE['background'], graphicModule.POSITION['background'])
    
    WIN.blit(graphicModule.TEXT['play'], graphicModule.POSITION['text_play'])
    WIN.blit(graphicModule.BUTTON['play'], graphicModule.POSITION['play_button'])
    
    WIN.blit(graphicModule.IMAGE['header'], graphicModule.POSITION['header'])
    
    
    WIN.blit(graphicModule.TEXT['time'], graphicModule.POSITION['text_time'])

    
    WIN.blit(graphicModule.BUTTON['next'], graphicModule.POSITION['next_button'])
    
    WIN.blit(graphicModule.BUTTON['success'], graphicModule.POSITION['success_icon'])
    WIN.blit(graphicModule.BUTTON['fail'], graphicModule.POSITION['fail_icon'])

    WIN.blit(graphicModule.IMAGE['img1'], graphicModule.POSITION['img1'])
    WIN.blit(graphicModule.IMAGE['img2'], graphicModule.POSITION['img2'])

    WIN.blit(graphicModule.IMAGE['img2'], graphicModule.POSITION['img3'])
    WIN.blit(graphicModule.IMAGE['img3'], graphicModule.POSITION['img4'])

    WIN.blit(graphicModule.IMAGE['img3'], graphicModule.POSITION['img5'])
    WIN.blit(graphicModule.IMAGE['img1'], graphicModule.POSITION['img6'])
    
    WIN.blit(graphicModule.TEXT['result'], graphicModule.POSITION['text_result'])
    WIN.blit(graphicModule.BUTTON['home'], graphicModule.POSITION['home_button'])
    
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