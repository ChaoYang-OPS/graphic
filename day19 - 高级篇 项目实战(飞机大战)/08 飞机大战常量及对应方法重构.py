"""小型敌机"""
import random
import pygame


class SmallEnemy:
    """小型敌机类"""

    def __init__(self, window):
        """初始化小型敌机"""

        # 获得窗口对象

        self.window = window

        # 加载小型敌机图片
        self.image = pygame.image.load("images/small_enemy.png")
        # 获得小型敌机的矩形
        self.rect = self.image.get_rect()
        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()
        # 设置小型敌机的矩形的初始位置为: 窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width - self.rect.width)

        # 小型敌机每次移动时的偏移量
        self.offset = 6

    def update(self):
        """更新小型敌机的位置"""

        # 增大小型敌机的属性top以向下移动
        self.rect.top += self.offset

    def draw(self):
        """再窗口中绘制小型敌机"""

        # 在窗口的指定位置绘制一架小型敌机
        self.window.blit(self.image, self.rect)


"""我方飞机"""

import pygame


class MyPlane:
    """我方飞机类"""

    def __init__(self, window):
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
        # 我方飞机每次移动时的偏移量
        self.offset = 20

    def update(self):
        """更新我方飞机的位置"""
        # 如果我方飞机被标记为向上移动，并且向上移动后不会超出窗口的上边缘
        if self.is_move_up and self.rect.top - self.offset > 0:
            self.rect.top -= self.offset
        # 如果我方飞机被标记为向下移动,并且向下移动后不会超出窗口的下边缘
        if self.is_move_down and self.rect.bottom + self.offset < \
                self.window_rect.height:
            # 增大我方飞机的矩形属性bottom以向下移动
            self.rect.bottom += self.offset
        # 如果我方飞机被标记为向左移动,并且向左移动后不会超出窗口的左边缘
        if self.is_move_left and self.rect.left - self.offset > 0:
            # 减少我方飞机的矩形属性left以向左移动
            self.rect.left -= self.offset
        # 如果我方飞机被标记为向右移动,并且向右移动后不会超出窗口的右边缘
        if self.is_move_right and self.rect.right + self.offset < self.window_rect.width:
            # 增大我方飞机的矩形属性right以向右移动
            self.rect.right += self.offset

    def draw(self):
        """再窗口中绘制我方飞机"""

        # 在窗口的指定位置绘制一架我方飞机
        self.window.blit(self.image, self.rect)


"""子弹"""

import pygame


class Bullet:
    """子弹类"""

    def __init__(self, window, my_plane):
        """初始化子弹"""

        # 获得窗口对象

        self.window = window

        # 加载子弹图片
        self.image = pygame.image.load("images/bullet.png")
        # 获得我子弹的矩形
        self.rect = self.image.get_rect()
        # 获得我方飞机的矩形
        self.my_plane_rect = my_plane.rect
        # 设置我子弹的矩形的初始位置为: 我方飞机的矩形的顶部居中位置
        self.rect.midtop = self.my_plane_rect.midtop

        # 子弹每次移动时的偏移量
        self.offset = 50

    def update(self):
        """更新子弹的位置"""
        self.rect.top -= self.offset

    def draw(self):
        """再窗口中绘制子弹"""

        # 在窗口的指定位置绘制一颗子弹
        self.window.blit(self.image, self.rect)


"""我方飞机"""

import pygame


class MyPlane:
    """我方飞机类"""

    def __init__(self, window):
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
        # 我方飞机每次移动时的偏移量
        self.offset = 20

    def update(self):
        """更新我方飞机的位置"""
        # 如果我方飞机被标记为向上移动，并且向上移动后不会超出窗口的上边缘
        if self.is_move_up and self.rect.top - self.offset > 0:
            self.rect.top -= self.offset
        # 如果我方飞机被标记为向下移动,并且向下移动后不会超出窗口的下边缘
        if self.is_move_down and self.rect.bottom + self.offset < \
                self.window_rect.height:
            # 增大我方飞机的矩形属性bottom以向下移动
            self.rect.bottom += self.offset
        # 如果我方飞机被标记为向左移动,并且向左移动后不会超出窗口的左边缘
        if self.is_move_left and self.rect.left - self.offset > 0:
            # 减少我方飞机的矩形属性left以向左移动
            self.rect.left -= self.offset
        # 如果我方飞机被标记为向右移动,并且向右移动后不会超出窗口的右边缘
        if self.is_move_right and self.rect.right + self.offset < self.window_rect.width:
            # 增大我方飞机的矩形属性right以向右移动
            self.rect.right += self.offset

    def draw(self):
        """再窗口中绘制我方飞机"""

        # 在窗口的指定位置绘制一架我方飞机
        self.window.blit(self.image, self.rect)


"""所有常量"""

import pygame

# 在水平方向上，窗口尺寸占电脑屏幕尺寸的比例
# 常量要全部大写


SCALE_HORIZONTAL = 2 / 5

# 在竖直方向上，窗口尺寸占电脑屏幕尺寸的比例
SCALE_VERTICAL = 4 / 5

# 动画的最大帧率
MAX_FRAMERATE = 30

# 自定义事件"创建子弹"的id

ID_OF_CREATE_BULLET = pygame.USEREVENT

# 自定义事件"创建子弹的时间间隔"

INTERVAL_OF_CREATE_BULLET = 500

# 自定义事件"创建小型敌机"的id

ID_OF_CREATE_SMALL_ENEMY = pygame.USEREVENT + 1

# 自定义事件"创建小型敌机的时间间隔" 2秒

INTERVAL_OF_CREATE_SMALL_ENEMY = 2000

"""游戏的入口"""

import pygame
import sys

from my_plane import MyPlane
from bullet import Bullet
from small_enemy import SmallEnemy

import constants


class PlaneWar:
    """管理游戏的总体类"""

    def __init__(self):
        """初始化游戏"""
        pygame.init()

        # 创建窗口
        self._create_window()

        # 设置窗口
        self._set_window()
        # 创建一架我方飞机
        self.my_plane = MyPlane(self.windows)

        # 创建管理画面元素的列表
        self._create_lists()
        # 创建一个用于跟踪时间的时钟对象
        self.clock = pygame.time.Clock()
        # 设置定时器
        self._set_timers()

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

    def _create_window(self):
        """创建窗口"""

        # 获得当前电脑屏幕的尺寸
        screen_width, screen_height = self.get_screen_size()
        # 根据当前电脑屏幕的尺寸计算窗口的尺寸
        window_width, window_height = screen_width * constants.SCALE_HORIZONTAL, \
                                      screen_height * constants.SCALE_VERTICAL
        # 创建指定尺寸的窗口(游戏画面的所有元素都将在创建的这个窗口中绘制) - round对float数进行四舍五入
        self.windows = pygame.display.set_mode((round(window_width), round(window_height)))
        # 创建全屏模式的窗口
        # self.windows = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def _set_window(self):
        """设置窗口"""
        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载窗口图标
        windows_icon = pygame.image.load("images/my_plane.png")
        # 设置窗口图标
        pygame.display.set_icon(windows_icon)

    def _create_lists(self):
        """创建管理画面元素的列表"""
        # 创建一个管理所有子弹的列表
        self.bullet_list = []

        # 创建一个管理所有小型敌机的列表
        self.small_enemy_list = []

    def _set_timers(self):
        """设置定时器"""

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建子弹"
        pygame.time.set_timer(constants.ID_OF_CREATE_BULLET, constants.INTERVAL_OF_CREATE_BULLET)

        # 在事件队列中每隔一段时间就生成一个自定义事件"创建小型敌机"
        pygame.time.set_timer(constants.ID_OF_CREATE_SMALL_ENEMY, constants.INTERVAL_OF_CREATE_SMALL_ENEMY)

    def run_game(self):
        """运行游戏"""
        # 初始化pygame库

        # 让创建窗口一直显示
        while True:
            # 处理事件
            self._handle_events()
            # 设置窗口的背景色
            self.windows.fill(pygame.Color("lightskyblue"))
            # 在窗口中绘制所有画面元素
            self._draw_elements()
            # 将内存中的窗口对象绘制到屏幕上以更新屏幕

            pygame.display.flip()

            # 设置while循环体在一秒内执行的最大次数(设置动画的最大帧率)
            self.clock.tick(constants.MAX_FRAMERATE)
            # 更新窗口中所有画面元素的位置
            self._update_positions()

            # 删除窗口中所有不可见的画面元素
            self._delete_invisible_elements()

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
                # 处理键盘按下的事件
                self._handle_keydown_events(event)
            # 如果某个事件是用户松开了键盘上的某个键
            elif event.type == pygame.KEYUP:
                # 处理键盘松开的事件
                self._handle_keyup_events(event)
            # 如果某个事件是自定义事件"创建子弹"
            elif event.type == constants.ID_OF_CREATE_BULLET:
                # 创建一颗子弹
                bullet = Bullet(self.windows, self.my_plane)
                # 将创建的子弹添加到子弹列表中
                self.bullet_list.append(bullet)

            # 如果某个事件是自定义事件"创建小型敌机"
            elif event.type == constants.ID_OF_CREATE_SMALL_ENEMY:
                # 创建一架小型敌机
                small_enemy = SmallEnemy(self.windows)
                # 将创建的小型敌机添加到小型敌机列表中
                self.small_enemy_list.append(small_enemy)

    def _handle_keydown_events(self, event):
        """处理键盘按下的事件"""
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
        # 如果按下的键是Esc键
        elif event.key == pygame.K_ESCAPE:

            # 卸载pygame库
            pygame.quit()
            # 退出游戏
            sys.exit()
        # 如果按下的是空格键

    def _handle_keyup_events(self, event):
        """处理键盘松开的事件"""
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

    def _draw_elements(self):
        """在窗口中绘制所有画面元素"""
        # 在窗口中绘制我方飞机
        self.my_plane.draw()
        # 在窗口中绘制所有子弹
        for bullet in self.bullet_list:
            # 在窗口中绘制子弹
            bullet.draw()

        # 在窗口中绘制所有小型敌机
        for small_enemy in self.small_enemy_list:
            # 在窗口中绘制小型敌机
            small_enemy.draw()

    def _update_positions(self):
        """更新窗口中所有画面元素的位置"""
        # 更新我方飞机的位置
        self.my_plane.update()
        # 更新所有子弹的位置
        for bullet in self.bullet_list:
            # 更新子弹的位置
            bullet.update()

        # 更新所有小型敌机的位置
        for small_enemy in self.small_enemy_list:
            # 更新小型敌机的位置
            small_enemy.update()

    def _delete_invisible_elements(self):
        """删除窗口中所有不可见的画面元素"""

        # 删除窗口中所有不可见的子弹
        self._delete_invisible_bullets()

        # 删除窗口中所有不可见的小型敌机
        self._delete_invisible_small_enemies()

    def _delete_invisible_bullets(self):
        """删除窗口中所有不可见的子弹"""
        # 遍历子弹列表
        for bullet in self.bullet_list:
            # 如果某颗子弹在窗口中不可见了
            if bullet.rect.bottom <= 0:
                # 从子弹列表中删除该颗子弹
                self.bullet_list.remove(bullet)

    def _delete_invisible_small_enemies(self):
        """删除窗口中所有不可见的小型敌机"""
        # 遍历子弹列表
        for small_enemy in self.small_enemy_list:
            # 如果某架小型敌机在窗口中不可见了
            if small_enemy.rect.top >= self.windows.get_rect().height:
                # 从小型敌机列表中删除该架小型敌机
                self.small_enemy_list.remove(small_enemy)


# 只有当直接运行main.py时
if __name__ == '__main__':
    # 运行游戏
    PlaneWar().run_game()
