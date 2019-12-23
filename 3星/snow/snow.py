import os
import time
import random
import pygame

# 定义三个参数，从时间上控制雪花数量，大小，速度
NUM = 50
SIZE_ = 3
SPEED = 3

t1 = time.time()

# 初始化pygame
pygame.init()
# 此处可让背景图片定位在左上角
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (5, 5)
# 根据背景图片的大小，设置屏幕长宽
SIZE = (1366, 768)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snow Animation")
bg = pygame.image.load('图片路径')


# def snow_num(num):
# 雪花列表
snow_list = []
snow_list1 = []
snow_list2 = []
snow_list3 = []
# 初始化雪花：[x坐标, y坐标, x轴速度, y轴速度]
for i in range(4):
    print(NUM)
    for j in range(NUM):  # 此处可控制雪花数量
        x = random.randrange(0, SIZE[0])
        y = random.randrange(0, SIZE[1])
        sx = random.randint(-1, 1)
        sy = random.randint(3, 6)
        if NUM == 50:
            snow_list.append([x, y, sx, sy])
        elif NUM == 125:
            snow_list1.append([x, y, sx, sy])
        elif NUM == 200:
            snow_list2.append([x, y, sx, sy])
        else:
            snow_list3.append([x, y, sx, sy])
    NUM += 75


clock = pygame.time.Clock()

# 游戏主循环
done = False
while not done:
    t2 = time.time()
    if 5 < t2 - t1 < 8:
        SIZE_ = 2
        SPEED = 1
        snow_list = snow_list1
    elif 8 < t2 - t1:
        SIZE_ = 0
        SPEED = 0
        snow_list = snow_list2
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 黑背景/图片背景
    # screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    # 雪花列表循环
    for i in range(len(snow_list)):
        # 绘制雪花，颜色、位置、大小
        pygame.draw.circle(screen, (255, 255, 255), snow_list[i][:2], snow_list[i][3] - SIZE_)  # 此处可通过减0-3来控制大小

        # 移动雪花位置（下一次循环起效）
        snow_list[i][0] += snow_list[i][2]
        snow_list[i][1] += snow_list[i][3] - SPEED  # 此处可通过减0-3来控制速度

        # 如果雪花落出屏幕，重设位置
        if snow_list[i][1] > SIZE[1]:
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(0, SIZE[0])

    # 刷新屏幕
    pygame.display.flip()
    clock.tick(20)

# 退出
pygame.quit()

