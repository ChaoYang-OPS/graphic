"""双发子弹"""

import pygame
from pygame.sprite import Sprite

class DoubleBullet(Sprite):
    """双发子弹类"""

    # 双发子弹每次移动时的偏移量
    offset = 50

    def __init__(self, window, my_plane):
        """初始化双发子弹"""

        # 调用父类Sprite的特殊方法__init__()
        super().__init__()

        # 获得窗口对象

        self.window = window

        # 加载双发子弹图片
        self.image = pygame.image.load("images/double_bullet.png")
        # 获得我双发子弹的矩形
        self.rect = self.image.get_rect()
        # 获得我方飞机的矩形
        self.my_plane_rect = my_plane.rect


    @classmethod
    def update_offset(cls, pixels):
        """更新小型敌机每次移动时的偏移量"""
        # 小型敌机每次移动时的偏移量增加指定的像素数
        DoubleBullet.offset += pixels

    def update(self):
        """更新双发子弹的位置"""
        self.rect.top -= DoubleBullet.offset

