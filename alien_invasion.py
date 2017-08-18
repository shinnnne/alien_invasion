import sys

import pygame
from pygame.sprite import Group

from setting import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化pygame 设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建play按钮
	play_button = Button(ai_settings, screen, "Play")
	
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	# 创建一艘飞船，一个用于存储子弹的编组，外星人
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	
	# 开始游戏的主循环
	while True:
		#监听鼠标和键盘事件
		gf.check_event(ai_settings, screen, stats, play_button, ship, 
						aliens, bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
			
		
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)		
	
run_game()
			
