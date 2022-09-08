import pygame
import random
from components.powerups.shield import Shield


class PowerUpManager:
    
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0

    def update(self, game):
        self.generate_power_ups()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.dinosaur.dino_rect.collidrect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.dinosaur.isShieldType = True
                game.dinosaur.type = power_up.type
                power_up.start_time = pygame.time.get_ticks()
                time_random = random.randrange(5,8)
                game.dinosaur.shield_time_up = power_up.start_time + (time_random * 1000)
                game.dinosaur_shield = True
                self.power_ups.remove(power_up)                

    def generate_power_ups(self):
        if len(self.power_ups) == 0:
            self.power_ups.append(Shield())

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
