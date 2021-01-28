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

def draw():
    
    WIN.fill(WHITE)
    WIN.blit(BG, (0,0))
    
    WIN.blit(IMG1, (270, 135))
    WIN.blit(IMG2, (520, 135))

    WIN.blit(IMG2, (270, 308))
    WIN.blit(IMG3, (520, 308))

    WIN.blit(IMG3, (270, 481))
    WIN.blit(IMG1, (520, 481))
    
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