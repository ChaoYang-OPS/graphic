"""我方飞机"""

import pygame


class MyPlane:
    """我方飞机类"""

    def __init__(self, window, pos):
        """初始化我方飞机"""

        # 获得窗口对象
        self.window = window

        # 加载我方飞机图片
        self.image = pygame.image.load("images/my_plane.png")
        # 获得我方飞机的矩形
        self.rect = self.image.get_rect()
        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()
        # 设置我方飞机的矩形的初始位置为: 窗口的底部居中位置
        self.rect.midbottom = self.window_rect.midbottom

    def update(self):
        """更新我方飞机的位置"""

        # 减少我方飞机的矩形的属性top以向上移动
        self.rect.top -= 20

    def draw(self):
        """再窗口中绘制我方飞机"""

        # 在窗口的指定位置绘制一架我方飞机
        self.window.blit(self.image, self.rect)




"""游戏的入口"""

import pygame
import sys

from my_plane import MyPlane


class PlaneWar:
    """管理游戏的总体类"""

    def __init__(self):
        """初始化游戏"""
        pygame.init()

        # 获得当前电脑屏幕的尺寸
        screen_width, screen_height = self.get_screen_size()
        # 根据当前电脑屏幕的尺寸计算窗口的尺寸
        window_width, window_height = screen_width * (2 / 5), \
                                      screen_height * (4 / 5)
        # 创建指定尺寸的窗口(游戏画面的所有元素都将在创建的这个窗口中绘制) - round对float数进行四舍五入
        self.windows = pygame.display.set_mode((round(window_width), round(window_height)))
        # 设置窗口
        self._set_window()
        # 创建一架我方飞机
        self.my_plane = MyPlane(self.windows, (299, 774))

        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()

    def get_screen_size(self):
        """获得当前电脑屏幕的尺寸"""
        # 创建一个视频显示信息对象
        info = pygame.display.Info()

        # 获得当前电脑屏幕的宽度
        screen_width = info.current_w
        # 获得当前电脑屏幕的高度
        screen_height = info.current_h
        # 返回当前电脑的尺寸
        return screen_width, screen_height

    def _set_window(self):
        """设置窗口"""
        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载窗口图标
        windows_icon = pygame.image.load("images/my_plane.png")
        # 设置窗口图标
        pygame.display.set_icon(windows_icon)

    def run_game(self):
        """运行游戏"""
        # 初始化pygame库

        # 让创建窗口一直显示
        while True:
            # 处理事件
            self._handle_events()
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

    def _handle_events(self):
        """处理事件"""
        # 从事件队列中将所有事件全部取出并逐个进行处理
        for event in pygame.event.get():
            # 如果某个事件是退出程序

            # 退出程序
            if event.type == pygame.QUIT:
                # 卸载pygame库
                pygame.quit()
                # 退出程序
                sys.exit()


# 只有当直接运行main.py时
if __name__ == '__main__':
    # 运行游戏
    PlaneWar().run_game()
