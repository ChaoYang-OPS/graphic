"""我方飞机"""

import pygame


class MyPlane:
    """我方飞机类"""

    def __init__(self, window, pos):
        """初始化我方飞机"""

        # 获得窗口对象
        self.window = window
        # 获得我方飞机的位置
        self.pos_x, self.pos_y = pos
        # 加载我方飞机图片
        self.image = pygame.image.load("images/my_plane.png")

    def update(self):
        """更新我方飞机的位置"""

        # 减少我方飞机的y坐标以向上移动
        self.pos_y -= 20

    def draw(self):
        """再窗口中绘制我方飞机"""

        # 在窗口的指定位置绘制一架我方飞机
        self.window.blit(self.image, (self.pos_x, self.pos_y))



"""下面为主代码"""

"""游戏的入口"""

import pygame
import sys

from my_plane import MyPlane


class PlaneWar:
    """管理游戏的总体类"""

    def __init__(self):
        """初始化游戏"""
        pygame.init()

        # 创建指定尺寸的窗口(游戏画面的所有元素都将在创建的这个窗口中绘制)
        self.windows = pygame.display.set_mode((700, 900))

        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载窗口图标
        windows_icon = pygame.image.load("images/my_plane.png")
        # 设置窗口图标
        pygame.display.set_icon(windows_icon)

        # 创建一架我方飞机
        self.my_plane = MyPlane(self.windows, (299, 774))

        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()

    def run_game(self):
        """运行游戏"""
        # 初始化pygame库

        # 让创建窗口一直显示
        while True:
            # 从事件队列中将所有事件全部取出并逐个进行处理
            for event in pygame.event.get():
                # 如果某个事件是退出程序

                # 退出程序
                if event.type == pygame.QUIT:
                    # 卸载pygame库
                    pygame.quit()
                    # 退出程序
                    sys.exit()
            # 设置窗口的背景色
            self.windows.fill(pygame.Color("lightskyblue"))

            # 在窗口中绘制我方飞机
            self.my_plane.draw()
            # 将内存中的窗口对象绘制到屏幕上以更新屏幕

            pygame.display.flip()

            # 设置while循环体在一秒内执行的最大次数(设置动画的最大帧率)
            self.clock.tick(30)

            # 更新我方飞机的位置
            self.my_plane.update()


# 只有当直接运行main.py时
if __name__ == '__main__':
    # 运行游戏
    PlaneWar().run_game()
