import pygame
from sys import  exit
import datetime
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('my Game')
clock = pygame.time.Clock()


font = pygame.font.SysFont("simsun",50)
text_surface = font.render("你好",True,"Green")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("Black")
    text_surface = font.render(str(datetime.datetime.now()),True,"Green")
    screen.blit(text_surface,(0,0))
    pygame.display.update()
    clock.tick(10)

