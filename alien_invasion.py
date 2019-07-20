
import pygame
from settings import Settings
from plane import Plane
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStas
from button import Button
from scoreboard import ScoreBoard
def run_game():
    #初始化游戏，并创建一个游戏对象
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('HB霍东阁')
    pygame.mixer.music.load('images/98k.mp3')
    #bg = pygame.image.load('images/xiaoqiao.jpg')
    #创建一个按钮
    but = Button(screen,'playing',)
    #创建一个用于统计游戏信息的实例,并创建记分牌
    stat = GameStas(ai_settings)
    sb = ScoreBoard(screen,ai_settings,stat)
     #创建一个飞船，一个子弹编组和一个外星人编组
    plane = Plane(screen,ai_settings)
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.creat_fleet(ai_settings,screen,plane,aliens)
    #开始游戏的主循环
    while True:
        #screen.blit(bg,(0,0))
        gf.check_events(ai_settings,screen,plane,bullets,but,stat,aliens,screen,sb)
        if stat.game_ative == True:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play()
            plane.update()
            gf.update_bullets(bullets,aliens,ai_settings,screen,plane,stat,sb)
            gf.update_aliens(aliens,ai_settings,plane,stat, bullets,screen,sb)
        gf.update_screen(ai_settings,screen,plane,bullets,aliens,but,stat,sb)


run_game()