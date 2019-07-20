import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event,ai_settings,screen,plane,bullets):
    if event.key == pygame.K_RIGHT:
        plane.moving_right = True
    elif event.key == pygame.K_LEFT:
        plane.moving_left = True
    elif event.key == pygame.K_UP:
        plane.moving_up = True
    elif event.key == pygame.K_DOWN:
        plane.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, plane,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, plane,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        # 创建一颗子弹，并将其加入到编组当中
        new_bullet = Bullet(ai_settings, screen, plane)
        bullets.add(new_bullet)

def check_keyup_events(event,plane):
    if event.key == pygame.K_RIGHT:
        plane.moving_right = False
    elif event.key == pygame.K_LEFT:
        plane.moving_left = False
    elif event.key == pygame.K_UP:
        plane.moving_up = False
    elif event.key == pygame.K_DOWN:
        plane.moving_down = False

def check_events(ai_settings,scree,plane,bullets,but,stat,aliens,screen,sb):
    # 响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,scree,plane,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,plane)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(but,mouse_x,mouse_y,stat,bullets,aliens,ai_settings, screen, plane,sb)

def check_play_button(but,mouse_x,mouse_y,stat,bullets,aliens,ai_settings, screen, plane,sb):
    """在玩家单机play按钮时开始游戏"""
    button_check = but.rect.collidepoint(mouse_x,mouse_y)
    if button_check and not stat.game_ative :
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stat.rest_stats()
        stat.game_ative = True
        #重置记分
        sb.rep_score()
        #sb.rep_high_score()
        sb.rep_level()
        sb.rep_planes()
        #清空子弹和外星人
        bullets.empty()
        aliens.empty()
        #创建一群新的外星人，并让战斗机居中，目前感觉此代码要不要不影响效果
        creat_fleet(ai_settings, screen, plane, aliens)
        plane.center_plane()

def update_bullets(bullets,aliens,ai_settings,screen,plane,stat,sb):
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            # print(len(bullets))
    check_bullet_alien_cl(ai_settings, screen, plane, aliens, bullets,stat,sb)

def check_bullet_alien_cl(ai_settings, screen, plane, aliens,bullets,stat,sb):
    # 检查是否有子弹击中外星人
    # 如果是这样，就删除子弹和外星人
    cl = pygame.sprite.groupcollide(bullets, aliens, False, True)
    if cl:
        for aliens in cl.values():
            stat.score += ai_settings.alien_jisha * len(aliens)
            sb.rep_score()
        check_high_score(stat,sb)
    if len(aliens) == 0:
        # 删除所有的子弹，并重新创建一群外星人,加快游戏节奏,提升一个等级
        bullets.empty()
        ai_settings.increase_speed()
        stat.level += 1
        sb.rep_level()
        creat_fleet(ai_settings, screen, plane, aliens)

def update_screen(ai_settings,screen,plane,bullets,aliens,but,stat,sb):
    # 每次循环都重绘屏幕
    screen.blit(ai_settings.bg_color,(0,0))
    #在外星人和飞机后绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    plane.blitme()
    aliens.draw(screen)
    #显示得分
    sb.draw_score()
    if  stat.game_ative == False:
        but.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def get_number_rows(ai_settings,plane_height,alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (5*alien_height)-plane_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien (ai_settings,screen,aliens,alien_number,row_number):
    """创建外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def creat_fleet(ai_settings,screen,plane,aliens):

    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens(ai_settings,alien.rect.width)
    number_row = get_number_rows(ai_settings,plane.rect.height,alien.rect.height)
    #创建外星人群
    for ro_numbe in range(number_row):
        for alien_num in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_num,ro_numbe)

def get_number_aliens(ai_settings,alien_width):
    # 计算一行可容纳多少个外星人
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (alien_width * 2))
    return number_aliens_x

def update_aliens(aliens,ai_settings,plane,stats, bullets,screen,sb):
    """检查外星人是否处于屏幕边缘，并更新外星人的位置"""
    check_fleet_edges(aliens, ai_settings)
    aliens.update()
    #检测外星人与飞机之间的碰撞
    if pygame.sprite.spritecollideany(plane,aliens,):
        plane_hit(stats, bullets, aliens, ai_settings, screen, plane,sb )
        #print('外星人把飞机撞毁了！！！')
    #检查外星人是否到达屏幕底端
    check_aliens_bottom(ai_settings, screen, aliens, stats, bullets, plane,sb)

def change_fleet_direction(aliens,ai_settings):
    """将整群外星人下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(aliens,ai_settings):
    """有外星人到达边缘时，采取相应措施"""
    for al in aliens.sprites():
        if al.check_edges():
            change_fleet_direction(aliens, ai_settings)
            break

def plane_hit(stat,bullets,aliens,ai_settings, screen, plane,sb):
    """响应被外星人撞的飞机"""
    if stat.plane_left > 0:
        #将plane_left - 1
        stat.plane_left -= 1
        sb.rep_planes()
        #清空外星人和子弹
        bullets.empty()
        aliens.empty()
        #创建一群新的外星人，并将飞机放到屏幕中间
        creat_fleet(ai_settings, screen, plane, aliens)
        plane.center_plane()
        #暂停
        sleep(1)
    else:
        stat.game_ative = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,screen,aliens,stats, bullets,plane,sb):
    """检测是否有外星人到达屏幕底部"""
    screen_rect = screen.get_rect()
    for ali in aliens.sprites():
        if ali.rect.bottom >= screen_rect.bottom:
            plane_hit(stats, bullets, aliens, ai_settings, screen, plane,sb )
            break

def check_high_score(stat,sb):
    """检测是否诞生了新的最高分"""
    if stat.height_score < stat.score:
        stat.height_score = stat.score
        sb.rep_high_score()







