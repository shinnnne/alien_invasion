import sys

import pygame

def run_game():
	
	pygame.init()
	screen = pygame.display.set_mode(1200, 800)
	pygame.display.set_caption("Alien Invasion")
	
	# ���ñ���ɫ
	bg_color = (230, 230, 230)
	
	# ��ʼ��Ϸ����ѭ��
	while True:
		#�������ͼ����¼�
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		#ÿ��ѭ��ʱ���ػ���Ļ
		screen.fill(bg_color)
		
		# ��������Ƶ���Ļ�ɼ�	
		pygame.display.flip()

run_game()
			
