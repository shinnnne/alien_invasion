import sys

import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化pygame 设置和屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# 创建一艘飞船，一个用于存储子弹的编组，外星人
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# 开始游戏的主循环
	while True:
		#监听鼠标和键盘事件
		gf.check_event(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)		
	
run_game()
			
