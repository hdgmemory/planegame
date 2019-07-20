import pygame
from pygame.sprite import Sprite
class Plane(Sprite):
    def  __init__(self,screen,ai_settings,):
        """初始化飞船并设置初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/plane2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将每艘飞机放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """在指定位置绘制飞机"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """根据移动标志调整飞机的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.plane_speed__fator
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.plane_speed__fator
        # if self.moving_up and self.rect.top < self.screen_rect.top:
        #     self.center += self.ai_settings.plane_speed__fator
        # if self.moving_down and self.rect.bottom > self.screen_rect.bottom:
        #     self.center -= self.ai_settings.plane_speed__fator
        self.rect.centerx = self.center

    def center_plane(self):
        """让飞机在屏幕上居中"""
        self.center = self.rect.centerx