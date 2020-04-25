class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (25, 25, 162)

		# Ship settings
		self.ship_speed = 1.5

		#Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (90, 255, 10)
		self.bullets_allowed = 3