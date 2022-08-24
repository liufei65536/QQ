import pygame
from sys import  exit

# 初始化 引擎
pygame.init()
# 设置屏幕
screen = pygame.display.set_mode((800,400)) # 宽度800，高度400
pygame.display.set_caption('Runner') # 设置标题
# 时钟
clock = pygame.time.Clock()
# surface
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface  = pygame.image.load('graphics/ground.png')
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
text_surface = test_font.render("My game",False,'Black')


while True:
    # 获取用户输入
    for event in pygame.event.get():
        # 用户点击退出，关闭游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # 绘图,更新
    screen.blit(sky_surface, (0, 0))  # 将test_surface放到screen上。(0,0)：放置后test_surface的左上角位于screen的(0,0)处
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    pygame.display.update()
    clock.tick(60) # 不超过60 fps
