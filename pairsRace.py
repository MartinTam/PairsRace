import pygame
import os
import graphicModule
import random

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
    WIN.blit(graphicModule.BUTTON['fail'], graphicModule.POSITION['fail_icon'])


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



def home():

    WIN.fill(graphicModule.COLORS['white'])
    WIN.blit(graphicModule.IMAGE['background'], graphicModule.POSITION['background'])
    
    WIN.blit(graphicModule.TEXT['play'], graphicModule.POSITION['text_play'])
    WIN.blit(graphicModule.BUTTON['play'], graphicModule.POSITION['play_button'])
    
    WIN.blit(graphicModule.IMAGE['header'], graphicModule.POSITION['header'])
    
    pygame.display.update()


def clickPlay(x,y):

    if (x >= 445) and (x <= 545) and (y >= 295) and (y <= 405):
        return True
    else:
        return False


def play():

    WIN.fill(graphicModule.COLORS['white'])
    WIN.blit(graphicModule.IMAGE['background'], graphicModule.POSITION['background'])

    WIN.blit(graphicModule.TEXT['time'], graphicModule.POSITION['text_time'])

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

    pygame.display.update()


def clickIMG(x,y):
    if (x >= 265) and (x <= 475) and (y >= 130) and (y <= 273):
        return True
    
    elif (x >= 515) and (x <= 725) and (y >= 130) and (y <= 273):
        return True

    elif (x >= 265) and (x <= 475) and (y >= 303) and (y <= 446):
        return True

    elif (x >= 515) and (x <= 752) and (y >= 303) and (y <= 446):
        return True

    elif (x >= 265) and (x <= 475) and (y >= 476) and (y <= 619):
        return True

    elif (x >= 515) and (x <= 725) and (y >= 476) and (y <= 619):
        return True
    
    else:
        return False


def chooseIMG(x,y):

    if (x >= 265) and (x <= 475) and (y >= 130) and (y <= 273):
        return 0
    
    elif (x >= 515) and (x <= 725) and (y >= 130) and (y <= 273):
        return 1

    elif (x >= 265) and (x <= 475) and (y >= 303) and (y <= 446):
        return 2

    elif (x >= 515) and (x <= 752) and (y >= 303) and (y <= 446):
        return 3

    elif (x >= 265) and (x <= 475) and (y >= 476) and (y <= 619):
        return 4

    elif (x >= 515) and (x <= 725) and (y >= 476) and (y <= 619):
        return 5
    
    else:
        return 6


def showIMG(choice1 = 6, choice2 = 6, success = False, wrong = False):

    WIN.fill(graphicModule.COLORS['white'])
    WIN.blit(graphicModule.IMAGE['background'], graphicModule.POSITION['background'])

    WIN.blit(graphicModule.TEXT['time'], graphicModule.POSITION['text_time'])

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


    if choice1 == 0 or choice2 == 0:
        
        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow1'])
        WIN.blit(graphicModule.RANDOM_IMG[0], graphicModule.POSITION['img1'])
    
    if choice1 == 1 or choice2 == 1:
    
        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow2'])
        WIN.blit(graphicModule.RANDOM_IMG[1], graphicModule.POSITION['img2'])
    
    if choice1 == 2 or choice2 == 2:

        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow3'])
        WIN.blit(graphicModule.RANDOM_IMG[2], graphicModule.POSITION['img3'])

    if choice1 == 3 or choice2 == 3:

        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow4'])
        WIN.blit(graphicModule.RANDOM_IMG[3], graphicModule.POSITION['img4'])

    if choice1 == 4 or choice2 == 4:

        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow5'])
        WIN.blit(graphicModule.RANDOM_IMG[4], graphicModule.POSITION['img5'])

    if choice1 == 5 or choice2 == 5:
        
        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow6'])
        WIN.blit(graphicModule.RANDOM_IMG[5], graphicModule.POSITION['img6'])
    


    if success:
        WIN.blit(graphicModule.BUTTON['success'], graphicModule.POSITION['success_icon'])
        WIN.blit(graphicModule.BUTTON['next'], graphicModule.POSITION['next_button'])
    
    if wrong:
        WIN.blit(graphicModule.BUTTON['fail'], graphicModule.POSITION['fail_icon'])
        WIN.blit(graphicModule.BUTTON['next'], graphicModule.POSITION['next_button'])

    
    pygame.display.update()



def clickNext(x,y):

    if (x >= 775) and (x <= 975) and (y >= 525) and (y <= 725):
        return True
    else:
        return False


def main():

    run = True
    clock = pygame.time.Clock()

    x = 0
    y = 0

    stage = 0

    first = 6
    second = 6

    click = False

    success = False
    wrong = False

    while run:

        clock.tick(graphicModule.FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                x, y = pygame.mouse.get_pos()

                             

        if stage == 0:
            home()
            #random.shuffle(graphicModule.RANDOM_IMG)
        
        if clickPlay(x,y) and (stage == 0):
            play()
            stage = 1
        
        if clickIMG(x,y) and (stage == 1):

            showIMG(chooseIMG(x,y))
            first = chooseIMG(x,y)
            click = False
            stage = 2

        if clickIMG(x,y) and click and (stage == 2):

            showIMG(first, chooseIMG(x,y))
            second = chooseIMG(x,y)
            click = False
            if first == second:
                stage = 2
            else:
                stage = 3


        if stage == 3 and (graphicModule.RANDOM_IMG[first] == graphicModule.RANDOM_IMG[second]):
            success = True
            showIMG(first, second, success)
            stage = 4

        
        if stage == 3 and (graphicModule.RANDOM_IMG[first] != graphicModule.RANDOM_IMG[second]):
            wrong = True
            showIMG(first, second, success, wrong)
            stage = 4
        
        if stage == 4 and click and clickNext(x,y):

            if success == True:
                showIMG(first,second)
                stage = 5
            
            if wrong == True:
                showIMG()
                wrong = False
                stage = 1

            click = False
        
        if stage == 5:
            showIMG(first,second)
        
        

        

    pygame.quit()

main()