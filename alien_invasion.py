import pygame
from settings import Settings
from game_stats import GameStats   
from scoreboard import Scoreboard
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from button import Button


def run_game():
    #初始化Pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")
    ship = Ship(ai_settings,screen)
    bullets = Group()      
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)   
     #开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
       #2 每次循 环时都重绘屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

        
run_game()
