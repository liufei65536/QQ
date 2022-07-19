import sys
import pygame


class Ball(pygame.sprite.Sprite):
    # 定义构造函数
    def __init__(self, filename):
        # 调父类来初始化子类
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        self.image = pygame.image.load(filename)
        # 获取图片rect区域
        self.rect = self.image.get_rect()


def update_all_pos(bars, speeds):
    for bar, speed in zip(bars, speeds):
        bar.rect = bar.rect.move(speed)  # 移动小球


if __name__ == '__main__':
    pygame.init()  # 初始化pygame
    size = width, height = 1024, 576
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("简单的弹球游戏")

    bg = pygame.image.load("images/bg.jpeg")
    bgrect = bg.get_rect()

    speed1 = [5, 5]  # 小球的速度

    ball1 = Ball("images/ball_1s.png")

    line = Ball("images/line_s.png")
    clock = pygame.time.Clock()
    crash_status = False

    while True:
        x, y = pygame.mouse.get_pos()  # 获取鼠标的x,y座标
        line.rect.center = pygame.mouse.get_pos()
        clock.tick(60)  # 第秒执行1000次
        # 检查事件
        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # 填充背景颜色,如果要填充数值，需要双小括号((0,0,0)) 后面有背景图片的,可以省略背景颜色。
        screen.blit(bg, bgrect)  # 将背景图片画到窗口上

        if ball1.rect.left < 0 or ball1.rect.right > width or crash_status:
            speed1[0] = -speed1[0]
        if ball1.rect.top < 0 or ball1.rect.bottom > height or crash_status:
            speed1[1] = -speed1[1]
        update_all_pos([ball1], [speed1])

        # 绘制精灵到屏幕上
        screen.blit(ball1.image, ball1.rect)
        screen.blit(line.image, line.rect)
        # 刷新显示屏幕
        pygame.display.update()

        crash_status = pygame.sprite.collide_rect(ball1, line)
        print(f'crash_status={crash_status}')