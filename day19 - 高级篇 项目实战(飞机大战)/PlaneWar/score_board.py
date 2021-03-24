"""得分板"""

import constants
import pygame


class ScoreBoard:
    """得分板类"""

    def __init__(self, window):
        """初始化得分板"""
        # 窗口对象
        self.window = window
        # 当前得分
        self.current_score = 0

        #  获得指定字体和指定字体大小的字体对象
        self.font_36 = pygame.font.Font("fonts/wawa.ttf", constants.FONT_SIZE_36)

    def draw_current_score(self):
        """在得分板中绘制当前得分"""
        # 当前得分的文本
        current_score_text = "当前得分:{}".format(self.current_score)
        # 获得当前得分的文本对应的surface对象
        current_score_text_surface = self.font_36.render(current_score_text,
                                                         True,
                                                         constants.WHITE_COLOR)
        # 获取当前得分的文本的矩形
        current_score_rect = current_score_text_surface.get_rect()

        # 将提示当前得分的文本矩形定位在窗口的左上角
        current_score_rect.left = constants.MARGIN
        current_score_rect.top = constants.MARGIN

        # 在窗口的的左上角绘制当前得分
        self.window.blit(current_score_text_surface, current_score_rect)
