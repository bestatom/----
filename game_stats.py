# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:33:00 2017

@author: Administrator
"""

class GameStats():
    def __init__(self,ai_settings):
    	#初始化统计信息
        self.ai_settings = ai_settings
        self.reset_stats()
        #让游戏开始处于非活跃状态
        self.game_active = False
        self.high_score = 0
    
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1