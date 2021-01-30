import pygame
import os
import graphicModule
import random

pygame.init()


WIN = pygame.display.set_mode(graphicModule.SIZE['window'])
pygame.display.set_caption('Pairs Race')


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


def showIMG(choice1 = 6, choice2 = 6,  choice3 = 6, choice4 = 6, choice5 = 6, choice6 = 6, success = False, wrong = False):

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


    if choice1 == 0 or choice2 == 0 or choice3 == 0 or choice4 == 0 or choice5 == 0 or choice6 == 0:
        
        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow1'])
        WIN.blit(graphicModule.RANDOM_IMG[0], graphicModule.POSITION['img1'])
    
    if choice1 == 1 or choice2 == 1 or choice3 == 1 or choice4 == 1 or choice5 == 1 or choice6 == 1:
    
        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow2'])
        WIN.blit(graphicModule.RANDOM_IMG[1], graphicModule.POSITION['img2'])
    
    if choice1 == 2 or choice2 == 2 or choice3 == 2 or choice4 == 2 or choice5 == 2 or choice6 == 2:

        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow3'])
        WIN.blit(graphicModule.RANDOM_IMG[2], graphicModule.POSITION['img3'])

    if choice1 == 3 or choice2 == 3 or choice3 == 3 or choice4 == 3 or choice5 == 3 or choice6 == 3:

        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow4'])
        WIN.blit(graphicModule.RANDOM_IMG[3], graphicModule.POSITION['img4'])

    if choice1 == 4 or choice2 == 4 or choice3 == 4 or choice4 == 4 or choice5 == 4 or choice6 == 4:

        pygame.draw.rect(WIN, graphicModule.COLORS['white'], graphicModule.IMAGE['shadow5'])
        WIN.blit(graphicModule.RANDOM_IMG[4], graphicModule.POSITION['img5'])

    if choice1 == 5 or choice2 == 5 or choice3 == 5 or choice4 == 5 or choice5 == 5 or choice6 == 5:
        
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


def showResult():

    WIN.fill(graphicModule.COLORS['white'])
    WIN.blit(graphicModule.IMAGE['background'], graphicModule.POSITION['background'])

    WIN.blit(graphicModule.TEXT['result'], graphicModule.POSITION['text_result'])
    WIN.blit(graphicModule.BUTTON['home'], graphicModule.POSITION['home_button'])
    WIN.blit(graphicModule.BUTTON['exit'], graphicModule.POSITION['exit_button'])
    pygame.display.update()


def clickHome(x,y):

    if (x >= 345) and (x <= 445) and (y >= 345) and (y <= 445):
        return True
    else:
        return False


def clickExit(x,y):

    if (x >= 545) and (x <= 645) and (y >= 345) and (y <= 445):
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
    third = 6
    forth = 6
    fifth = 6
    sixth = 6

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
            random.shuffle(graphicModule.RANDOM_IMG)
        
        if clickPlay(x,y) and (stage == 0):
            play()
            click = False
            stage = 1
        
        # ---------------------------------------------------------------------------------------------

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
            showIMG(first, second, 6, 6, 6, 6, success)
            stage = 4

        
        if stage == 3 and (graphicModule.RANDOM_IMG[first] != graphicModule.RANDOM_IMG[second]):
            wrong = True
            showIMG(first, second, 6, 6, 6, 6, success, wrong)
            stage = 4
        
        if stage == 4 and click and clickNext(x,y):

            if success == True:
                showIMG(first,second)
                success = False
                stage = 5
            
            if wrong == True:
                showIMG()
                wrong = False
                stage = 1

            click = False
        
        # -----------------------------------------------------------------------------------------------

        if stage == 5 and clickIMG(x,y):

            if (0 <= chooseIMG(x,y) <= 5):

                if chooseIMG(x,y) == first or chooseIMG(x,y) == second:
                    stage = 5
                else:
                    showIMG(first,second, chooseIMG(x,y))
                    third = chooseIMG(x,y)
                    click = False
                    stage = 6        
        
        if clickIMG(x,y) and click and (stage == 6):

            if (0 <= chooseIMG(x,y) <= 5):

                if chooseIMG(x,y) == first or chooseIMG(x,y) == second:
                    stage = 6
                else:
                    showIMG(first, second, third, chooseIMG(x,y))
                    forth = chooseIMG(x,y)
                    click = False
                    if third == forth:
                        stage = 6
                    else:
                        stage = 7
        

        if stage == 7 and (graphicModule.RANDOM_IMG[third] == graphicModule.RANDOM_IMG[forth]):
            success = True
            showIMG(first, second, third, forth, 6, 6, success)
            stage = 8

        
        if stage == 7 and (graphicModule.RANDOM_IMG[third] != graphicModule.RANDOM_IMG[forth]):
            wrong = True
            showIMG(first, second, third, forth, 6, 6, success, wrong)
            stage = 8
        
        if stage == 8 and click and clickNext(x,y):

            if success == True:
                showIMG(first,second, third, forth)
                success = False
                stage = 9
            
            if wrong == True:
                showIMG(first, second)
                wrong = False
                stage = 5


            click = False

        # -----------------------------------------------------------------------------------------------

        if stage == 9 and clickIMG(x,y):

            if (0 <= chooseIMG(x,y) <= 5):

                if chooseIMG(x,y) == first or chooseIMG(x,y) == second or chooseIMG(x,y) == third or chooseIMG(x,y) == forth:
                    stage = 9
                else:
                    showIMG(first,second, third, forth, chooseIMG(x,y))
                    fifth = chooseIMG(x,y)
                    click = False
                    stage = 10        
        
        if clickIMG(x,y) and click and (stage == 10):

            if (0 <= chooseIMG(x,y) <= 5):

                if chooseIMG(x,y) == first or chooseIMG(x,y) == second or chooseIMG(x,y) == third or chooseIMG(x,y) == forth:
                    stage = 10
                else:
                    showIMG(first, second, third, forth, fifth, chooseIMG(x,y))
                    sixth = chooseIMG(x,y)
                    click = False
                    if fifth == sixth:
                        stage = 10
                    else:
                        stage = 11
        

        if stage == 11 and (graphicModule.RANDOM_IMG[fifth] == graphicModule.RANDOM_IMG[sixth]):
            success = True
            showIMG(first, second, third, forth, fifth, sixth, success)
            stage = 12

        
        if stage == 11 and (graphicModule.RANDOM_IMG[fifth] != graphicModule.RANDOM_IMG[sixth]):
            wrong = True
            showIMG(first, second, third, forth, fifth, sixth, success, wrong)
            stage = 12
        
        if stage == 12 and click and clickNext(x,y):

            if success == True:
                showIMG(first,second, third, forth, fifth, sixth)
                success = False
                stage = 13
            
            if wrong == True:
                showIMG(first, second, third, forth)
                wrong = False
                stage = 9


            click = False

        # -----------------------------------------------------------------------------------------------

        if stage == 13 and clickNext(x,y):

            showResult()
            click = False
            stage = 14


        if (stage == 14) and click and clickHome(x,y):
            
            stage = 0
            first = 6
            second = 6
            third = 6
            forth = 6
            fifth = 6
            sixth = 6
            click = False

        if (stage == 14) and click and clickExit(x,y):
    
            break

    

        
        

    pygame.quit()

main()
