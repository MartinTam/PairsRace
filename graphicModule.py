import pygame
import os

pygame.init()

FPS = 60

COLORS =    {
                'white' : (255, 255, 255),
                'black' : (0, 0, 0),
                'grey' : (92, 92, 92)           
            }


IMAGE = {
            'background' : pygame.image.load(os.path.join('images', 'background.jpeg')),
            
            'img1' : pygame.image.load(os.path.join('images', '01.jpeg')),
            'img2' : pygame.image.load(os.path.join('images', '02.jpeg')),
            'img3' : pygame.image.load(os.path.join('images', '03.jpeg')),

            'shadow1' : pygame.Rect(265, 130, 210, 143),
            'shadow2' : pygame.Rect(515, 130, 210, 143),                    
            'shadow3' : pygame.Rect(265, 303, 210, 143),
            'shadow4' : pygame.Rect(515, 303, 210, 143),
            'shadow5' : pygame.Rect(265, 476, 210, 143),                    
            'shadow6' : pygame.Rect(515, 476, 210, 143),

            'backside1' : pygame.Rect(270, 135, 200, 133),
            'backside2' : pygame.Rect(520, 135, 200, 133),
            'backside3' : pygame.Rect(270, 308, 200, 133),
            'backside4' : pygame.Rect(520, 308, 200, 133),
            'backside5' : pygame.Rect(270, 481, 200, 133),
            'backside6' : pygame.Rect(520, 481, 200, 133),
            
            'tire' : pygame.image.load(os.path.join('images', 'tire.jpeg')),

            'header' : pygame.image.load(os.path.join('images', 'header.png'))
        }



LOAD_BUTTON_ORG =   {
                        'play' : pygame.image.load(os.path.join('images', 'play.png')),
                        'next' : pygame.image.load(os.path.join('images', 'next.png')),
                        'success' : pygame.image.load(os.path.join('images', 'success.png')),
                        'fail' : pygame.image.load(os.path.join('images', 'fail.png')),
                        'home' : pygame.image.load(os.path.join('images', 'home.png'))
                    }



SIZE =  {
            'window' : (1000, 700),
            'play_button' : (100, 110),
            'next_button' : (200, 200),
            'success_icon' : (80,80),
            'fail_icon' : (80,80),
            'home_button' : (100,100),
            'img' : (200, 133)
        }



BUTTON =    {
                'play' : pygame.transform.scale( LOAD_BUTTON_ORG['play'], SIZE['play_button'] ),
                'next' : pygame.transform.scale( LOAD_BUTTON_ORG['next'], SIZE['next_button'] ),
                'success' : pygame.transform.scale( LOAD_BUTTON_ORG['success'], SIZE['success_icon'] ),
                'fail' : pygame.transform.scale( LOAD_BUTTON_ORG['fail'], SIZE['fail_icon'] ),
                'home' : pygame.transform.scale( LOAD_BUTTON_ORG['home'], SIZE['home_button'] )
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

                'tire1' : (318, 152),
                'tire2' : (568, 152),
                'tire3' : (318, 325),
                'tire4' : (568, 325),
                'tire5' : (318, 498),
                'tire6' : (568, 498),

                'img1' : (270, 135),
                'img2' : (520, 135),
                'img3' : (270, 308),
                'img4' : (520, 308),
                'img5' : (270, 481),
                'img6' : (520, 481),

                'text_result' : (325,230),
                'home_button' : (445,395)
            }

FONT = pygame.font.SysFont('comicsans', 70)

TEXT =  {
            'play' : FONT.render('PLAY', True, COLORS['white']),
            'time' : FONT.render('00:00:00', True, COLORS['white']),
            'result' : FONT.render('Time: 00:00:00', True, COLORS['white'])
        }

pygame.quit()