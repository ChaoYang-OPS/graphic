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
        # 标记我方飞机不向上移动
        self.is_move_up = False
        # 标记我方飞机不向下移动
        self.is_move_down = False

        # 标记我方飞机不向左移动
        self.is_move_left = False

        # 标记我方飞机不向右移动
        self.is_move_right = False

    def update(self):
        """更新我方飞机的位置"""
        # 如果我方飞机被标记为向上移动
        if self.is_move_up:
            self.rect.top -= 20
        # 如果我方飞机被标记为向下移动
        if self.is_move_down:
            # 增大我方飞机的矩形属性bottom以向下移动
            self.rect.bottom += 20
        # 如果我方飞机被标记为向左移动
        if self.is_move_left:
            # 减少我方飞机的矩形属性left以向左移动
            self.rect.left -= 20
        # 如果我方飞机被标记为向右移动
        if self.is_move_right:
            # 增大我方飞机的矩形属性right以向右移动
            self.rect.right += 20



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
            # 如果某个事件是用户按下了键盘上的某个键
            elif event.type == pygame.KEYDOWN:
                # 如果按下的键是上箭头或者w键
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    # 标记我方飞机向上移动
                    self.my_plane.is_move_up = True
                # 如果按下的键是下箭头或者S键
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    # 标记我方飞机向下移动
                    self.my_plane.is_move_down = True
                # 如果按下的键是左箭头或者A键
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    # 标记我方飞机向左移动
                    self.my_plane.is_move_left = True
                # 如果按下的键是右箭头或者D键
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # 标记我方飞机向右移动
                    self.my_plane.is_move_right = True
            # 如果某个事件是用户松开了键盘上的某个键
            elif event.type == pygame.KEYUP:
                # 如果松开的键是上箭头或者w键
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    # 标记我方飞机不向上移动
                    self.my_plane.is_move_up = False
                # 如果松开的键是下箭头或者s键
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    # 标记我方飞机不向下移动
                    self.my_plane.is_move_down = False
                # 如果松开的键是左箭头或者a键
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    # 标记我方飞机不向左移动
                    self.my_plane.is_move_left = False
                # 如果松开的键是右箭头或者d键
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    # 标记我方飞机不向右移动
                    self.my_plane.is_move_right = False


# 只有当直接运行main.py时
if __name__ == '__main__':
    # 运行游戏
    PlaneWar().run_game()
