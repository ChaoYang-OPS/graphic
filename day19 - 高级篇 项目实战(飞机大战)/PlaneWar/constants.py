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


# 自定义事件"创建中型敌机"的id

ID_OF_CREATE_MID_ENEMY = pygame.USEREVENT + 2

# 自定义事件"创建大型敌机"的id

ID_OF_CREATE_BIG_ENEMY = pygame.USEREVENT + 3

# 自定义事件"创建小型敌机的时间间隔" 2秒

INTERVAL_OF_CREATE_SMALL_ENEMY = 2000


# 自定义事件"创建中型敌机的时间间隔"

INTERVAL_OF_CREATE_MID_ENEMY = 3600

# 自定义事件"创建大型敌机的时间间隔" 18秒

INTERVAL_OF_CREATE_BIG_ENEMY = 18000

# 切换我方飞机图片的频率
MY_PLANE_SWITCH_IMAGE_FREQUENCY = 3

# 切换小型敌机爆炸图片的频率
SMALL_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 8


# 切换中型敌机爆炸图片的频率
MID_ENEMY_SWITCH_EXPLODE_IMAGE_FREQUENCY = 8
# 爆炸声音的音量
EXPLODE_SOUND_VOLUME = 0.8

# 中型敌机的初始能量
MID_ENEMY_INITIAL_ENERGY = 5

# 切换中型敌机中型敌机被击中的频率
MID_ENEMY_SWITCH_HIT_IMAGE_FREQUENCY = 3
