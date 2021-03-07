"""测试矩形的属性"""

import pygame

rect = pygame.Rect(100, 50, 180, 120)
print("left = {}".format(rect.left))
print("top = {}".format(rect.top))
print("width = {}".format(rect.width))
print("height = {}".format(rect.height))
# right = left + width
print("right = {}".format(rect.right))
# bottom = top + height
print("bottom = {}".format(rect.bottom))
# centerx = left + width / 2
print("centerx = {}".format(rect.centerx))
# centery = top + height / 2
print("centery = {}".format(rect.centery))

# x = left
print("x = {}".format(rect.x))
# y = top
print("y = {}".format(rect.y))
# w = width
print("w = {}".format(rect.w))
# h = height
print("h = {}".format(rect.h))

# size = (width, height)
print("size = {}".format(rect.size))
# center = (centerx, centery)
print("center = {}".format(rect.center))

# topleft = (left, top), 左上角
print("topleft = {}".format(rect.topleft))
# bottomleft = (left, bottom), 左下角
print("bottomleft = {}".format(rect.bottomleft))
# bottomright = (right, bottom),右下角
print("bottomright = {}".format(rect.bottomright))
# topright = (right, top), 右上角
print("topright = {}".format(rect.topright))

# midtop = (centerx, top), 上边缘中心点
print("midtop = {}".format(rect.midtop))
# midleft = (left, centery), 左边缘中心点
print("midleft = {}".format(rect.midleft))
# midbottom = (centerx, bottom), 下边缘中心点
print("midbottom = {}".format(rect.midbottom))
# midright = (right, centery), 右边缘中心点
print("midright = {}".format(rect.midright))

# rect.width = 170
# rect.w = 170
# rect.size = (170, rect.height)
print(rect.width)
