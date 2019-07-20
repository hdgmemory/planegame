import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_settings,screen):
        """初始化外星人，并设置起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载外星人图像
        self.image = pygame.image.load('images/guaishou.png')
        self.rect = self.image.get_rect()
        #每个外星人都在屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        """向右或者向右移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor
                  * self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        """如果外星人处于边缘就返回Ture"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

