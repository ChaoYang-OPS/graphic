"""炸弹补给"""
import random
import pygame
from pygame.sprite import Sprite


class BombSupply(Sprite):
    """炸弹补给类"""

    def __init__(self, window):
        """初始化炸弹补给"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象

        self.window = window

        # 加载炸弹补给相关图片

        # 加载炸弹补给图片
        self.image = pygame.image.load("images/bomb_supply.png")

        # 获得炸弹补给的矩形
        self.rect = self.image.get_rect()
        # 获得窗口的矩形
        self.window_rect = self.window.get_rect()
        # 设置炸弹补给的矩形的初始位置为: 窗口的矩形的顶部一个随机的水平位置
        self.rect.bottom = self.window_rect.top
        self.rect.left = random.randint(0, self.window_rect.width - self.rect.width)

        # 炸弹补给每次移动时的偏移量
        self.offset = 5

    def update(self):
        """更新炸弹补给的位置"""

        # 增大炸弹补给的属性top以向下移动
        self.rect.top += self.offset
