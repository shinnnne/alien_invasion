class Settings():
	'''存储所有设置的类'''
	
	def __init__(self):
		'''初始化游戏的设置'''
		
		#屏幕设置
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230,230,230)

		# 子弹设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 3
		
		#外星人设置
		self.alen_speed_factor = 1
