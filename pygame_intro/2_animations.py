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
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface  = pygame.image.load('graphics/ground.png').convert()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
score_surf = test_font.render("My game", False, 'Black')
score_rect = score_surf.get_rect(center=(400,50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80,300))
player_gravity = 0

while True:
    # 获取用户输入
    for event in pygame.event.get():
        # 用户点击退出，关闭游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom>=300:
                player_gravity -= 20
    # 绘图,更新
    screen.blit(sky_surface, (0, 0))  # 将test_surface放到screen上。(0,0)：放置后test_surface的左上角位于screen的(0,0)处
    screen.blit(ground_surface,(0,300))

    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)

    screen.blit(score_surf, score_rect)

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)

    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
        player_rect.bottom = 300
        player_gravity = 0
    screen.blit(player_surf,player_rect)


    pygame.display.update()
    clock.tick(60) # 不超过60 fps
