import pygame
class Settings():
    """一个存储游戏所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1100
        self.screen_height = 600
        self.bg_color =  pygame.image.load('images/xiaoqiao.jpg')
        #飞机设置
        self.plane_limit = 3
        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 1,12,23
        self.bullet_allowed = 3
        #外星人设置
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        #以什么速度加快游戏节奏
        self.speedup_scale = 1.1
        #击杀外星人，分数提高速度
        self.score_scale = 1.5
        self.dongtai_game()

    def dongtai_game(self):
        self.plane_speed__fator = 10
        self.bullet_speed_factor = 10
        self.alien_speed_factor = 3
        self.alien_jisha = 100

    def increase_speed(self):
        self.plane_speed__fator *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_jisha *= self.score_scale
        print('提升一个等级击杀外星人获得的得分为：',self.alien_jisha)