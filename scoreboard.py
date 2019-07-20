import pygame.font
from pygame.sprite import Group
from plane import Plane
class ScoreBoard():
    def __init__(self,screen,ai_settings,stat):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()#引入整个屏幕的参数
        self.ai_settings = ai_settings
        self.stat = stat
        """设置得分的字样，文本颜色"""
        self.text_color = (45,45,65)
        self.font = pygame.font.SysFont(None, 32)
        #准备初始得分图像
        self.rep_score()
        self.rep_high_score()
        self.rep_level()
        self.rep_planes()

    def rep_score(self):
        """将得分渲染成一幅图像"""
        #score_str = str(self.stat.score)
        rounded_score = round(self.stat.score,-1)
        score_str = '{}{:,}'.format('score:',rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color
                                            ,self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top =  self.screen_rect.top

    def rep_high_score(self):
        """将最高得分渲染成另外一幅图像"""
        zuigao_score = round(self.stat.height_score,-1)
        scor_str = '{}{:,}'.format('high_score:',zuigao_score)
        self.scor_image = self.font.render(scor_str,True,self.text_color,
                                           self.ai_settings.bg_color)
        self.scor_rect = self.scor_image.get_rect()
        self.scor_rect.center = self.screen_rect.center
        self.scor_rect.top = self.screen_rect.top

    def rep_level(self):
        """将等级渲染成一幅图片"""
        level_sz = round(self.stat.level)
        level_str = '{}{:,}'.format('level:',level_sz)
        self.level_image = self.font.render(level_str,True,self.text_color,
                                            self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.scor_rect.bottom + 10

    def draw_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.scor_image,self.scor_rect)
        self.screen.blit(self.level_image,self.level_rect)
        #绘制飞机
        self.planes.draw(self.screen)

    def rep_planes(self):
        """显示还剩下多少艘飞机"""
        self.planes = Group()
        for plane_num in range(self.stat.plane_left):
            plane = Plane(self.screen, self.ai_settings)
            plane.rect.x = 10 + plane_num * plane.rect.width
            plane.rect.y = 0
            self.planes.add(plane)