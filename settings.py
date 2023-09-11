class Settings():
    #File class to store all setup for Alien invasion
    def __init__(self):
        """Init the game settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (230,230,230)
        #Ship modifiers
        self.ship_speed_factor = 0.72
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3