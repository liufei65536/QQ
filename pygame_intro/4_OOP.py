import random
import pygame
from sys import exit


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.walk = [walk_1, walk_2]
        self.index = 0
        self.jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

        self.image = self.walk[self.index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.5)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity -= 20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
            self.gravity = 0

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.jump
        else:
            self.index += 0.1
            if self.index >= len(self.walk):
                self.index = 0
            self.image = self.walk[int(self.index)]

    def update(self):
        self.input()
        self.apply_gravity()
        self.animation_state()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'fly':
            fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        elif type == 'snail':
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300
        self.index = 0
        self.image = self.frames[self.index]
        self.rect = self.image.get_rect(midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):
        self.index += 0.1
        if self.index >= len(self.frames):
            self.index = 0
        self.image = self.frames[int(self.index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    # 显示分数
    current = pygame.time.get_ticks() // 1000 - start_time
    score_surf = test_font.render(f"Score:{current}", False, (64, 64, 64))
    screen.blit(score_surf, score_surf.get_rect(center=(400, 50)))
    return current

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True


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
# 人物画
player_stand_surf = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_surf = pygame.transform.rotozoom(player_stand_surf, 0, 2)
player_stand_rect = player_stand_surf.get_rect(midbottom=(400, 300))


# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 800)


player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()


bg_music = pygame.mixer.Sound('audio/张震岳 - 迷途羔羊.mp3')
bg_music.set_volume(0.5)
bg_music.play(loops=-1)

start_time = 0
score = 0
game_activate = False
while True:
    # 获取用户输入
    for event in pygame.event.get():
        # 用户点击退出，关闭游戏
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_activate:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(random.choice(['fly', 'snail', 'snail', 'snail'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_activate = True
                start_time = pygame.time.get_ticks() // 1000
    # 游戏运行：绘图,更新
    if game_activate:
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        screen.blit(sky_surf, (0, 0))  # 将test_surface放到screen上。(0,0)：放置后test_surface的左上角位于screen的(0,0)处
        screen.blit(ground_surf, (0, 300))
        score = display_score()
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        game_activate = collision_sprite()
    # 游戏结束：
    else:
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
