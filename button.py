import pygame.font

class Button():
    def __init__(self,screen,sz):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()#引入整个屏幕的参数
        #设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (25,25,25)
        self.font = pygame.font.SysFont(None,56)
        #创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        #按钮的标签只需要创建一次
        self.xs_sz(sz)
    def xs_sz(self,sz):
        """将数字渲染成图像"""
        self.sz_image = self.font.render(sz,True,self.text_color,
                                         self.button_color)
        self.sz_image_rect = self.sz_image.get_rect()
        self.sz_image_rect.center = self.rect.center

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.sz_image,self.sz_image_rect)
