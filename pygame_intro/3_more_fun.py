import random
import pygame
from sys import exit


def display_score():
    # 显示分数
    current = pygame.time.get_ticks() // 1000 - start_time
    score_surf = test_font.render(f"Score:{current}", False, (64, 64, 64))
    screen.blit(score_surf, score_surf.get_rect(center=(400, 50)))
    return current


def player_animation():
    # 播放主角跑步和跳跃的动画
    global player_surf, player_index

    if player_rect.bottom < 300:
        # jump
        player_surf = player_jump
    else:
        player_index += 0.1  # 我们不想腿变换的频率太快
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]


# 初始化 引擎
pygame.init()
# 设置屏幕
screen = pygame.display.set_mode((800, 400))  # 宽度800，高度400
pygame.display.set_caption('Runner')  # 设置标题
# 时钟
clock = pygame.time.Clock()
# 字体
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
# 背景
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
# 得分
score_surf = test_font.render("My game", False, 'Black')
score_rect = score_surf.get_rect(center=(400, 50))
# 游戏简介
game_name_surf = test_font.render("Runner", False, 'Black')
game_name_rect = game_name_surf.get_rect(center=(400, 80))
game_message_surf = test_font.render("Press space to run", False, (111, 196, 169))
game_message_rect = game_message_surf.get_rect(center=(400, 320))

# Obstacles （障碍，有蜗牛和苍蝇）
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frames_index = 0
snail_surf = snail_frames[snail_frames_index]

fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frames_index = 0
fly_surf = fly_frames[fly_frames_index]

obstacle_rect_list = []

# 人物
player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))

player_stand_surf = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_surf = pygame.transform.rotozoom(player_stand_surf, 0, 2)
player_stand_rect = player_stand_surf.get_rect(midbottom=(400, 300))

player_gravity = 0
game_activate = False
start_time = 0
score = 0

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 800)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

player_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(player_animation_timer, 200)


def obstacle_movement(obstacle_rect_list):
    # 移动障碍
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)
        obstacle_rect_list = [obstacle_rect for obstacle_rect in obstacle_rect_list if obstacle_rect.x > 0]
    else:
        obstacle_rect_list = []
    return obstacle_rect_list


def collisions(player, obstacles):
    # 碰撞检测
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return True
    return False


while True:
    # 获取用户输入
    for event in pygame.event.get():
        # 用户点击退出，关闭游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_activate:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity -= 20
            if event.type == obstacle_timer:
                if random.randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright=(random.randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright=(random.randint(900, 1100), 210)))
            if event.type == snail_animation_timer:
                snail_frames_index = ~snail_frames_index
                snail_surf = snail_frames[snail_frames_index]
            if event.type == fly_animation_timer:
                fly_frames_index = ~fly_frames_index
                fly_surf = fly_frames[fly_frames_index]


        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_activate = True

                    start_time = pygame.time.get_ticks() // 1000
    # 游戏运行：绘图,更新
    if game_activate:
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(sky_surf, (0, 0))  # 将test_surface放到screen上。(0,0)：放置后test_surface的左上角位于screen的(0,0)处
        screen.blit(ground_surf, (0, 300))

        score = display_score()
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
            player_gravity = 0
        player_animation()
        screen.blit(player_surf, player_rect)

        if collisions(player_rect, obstacle_rect_list):
            game_activate = False
    # 游戏结束：
    else:
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        screen.fill((94, 129, 162))
        screen.blit(player_stand_surf, player_stand_rect)
        screen.blit(game_name_surf, game_name_rect)
        if score == 0:
            screen.blit(game_message_surf, game_message_rect)
        else:
            score_message = test_font.render(f'Your score:{score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center=(400, 320))
            screen.blit(score_message, score_message_rect)

    pygame.display.update()
    clock.tick(60)  # 不超过60 fps
