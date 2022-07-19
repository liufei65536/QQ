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


pygame.init()  # 初始化pygame
size = width, height = 1024, 576
screen = pygame.display.set_mode(size)
pygame.display.set_caption("简单的弹球游戏")

bg = pygame.image.load("images/bg.jpeg")
bgrect = bg.get_rect()

speed1 = [5, 5]  # 小球的速度
speed2 = [10, 10]  # 小球的速度

#line = pygame.image.load("images/line_s.png")
line = Ball("images/line_s.png")

filename1 = "images/ball_1s.png"
ball1 = Ball(filename1)

filename2 = "images/ball_2s.png"
ball2 = Ball(filename2)


def update_all_pos():
    ball1.rect = ball1.rect.move(speed1)  # 移动小球
    ball2.rect = ball2.rect.move(speed2)  # 移动小球

crash_status = pygame.sprite.collide_rect(ball1, ball2)
clock = pygame.time.Clock()

# 执行死循环，确保窗口一直显示
while True:

    x, y = pygame.mouse.get_pos()  # 获取鼠标的x,y座标
    line.rect = pygame.mouse.get_pos()
    linerect = x, y
    clock.tick(60)  # 第秒执行1000次
    # 检查事件
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))  # 填充背景颜色,如果要填充数值，需要双小括号((0,0,0)) 后面有背景图片的,可以省略背景颜色。

    screen.blit(bg, bgrect)  # 将背景图片画到窗口上



    if ball1.rect.left < 0 or ball1.rect.right > width :
        speed1[0] = -speed1[0]
    if ball1.rect.top < 0 or ball1.rect.bottom > height :
        speed1[1] = -speed1[1]

    if ball2.rect.left < 0 or ball2.rect.right > width  :
        speed2[0] = -speed2[0]
    if ball2.rect.top < 0 or ball2.rect.bottom > height :
        speed2[1] = -speed2[1]

    update_all_pos()

    # 绘制精灵到屏幕上
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    screen.blit(line.image, line.rect)
    # 刷新显示屏幕
    pygame.display.update()
    crash_status = pygame.sprite.collide_rect(ball1, ball2)



    # print("x,y=",x,y)                #多一条输出语句会很影响整个画面的速度

    # pygame.display.flip()             #更新全部显示(可能是一层一层的更新)
"""
主要有两点区别：

一是：
pygame.display.flip() 更新整个待显示的Surface对象到屏幕上
pygame.display.update() 更新部分内容显示到屏幕上，如果没有参数，则与flip功能相同(上一条)
二是
当使用OpenGL的时候，不能使用pygame.display.update()来更新窗口，需要使用pygame.display.flip() 来更新
flip函数将重新绘制整个屏幕对应的窗口。

update函数仅仅重新绘制窗口中有变化的区域。
如果仅仅是几个物体在移动，那么他只重绘其中移动的部分，没有变化的部分，并不进行重绘。update比flip速度更快。
因此在一般的游戏中，如果不是场景变化非常频繁的时候，我们建议使用update函数，而不是flip函数。
"""
