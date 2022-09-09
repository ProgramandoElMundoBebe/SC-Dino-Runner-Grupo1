import random
from pygame.sprite import Sprite

from utils.constants import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH

class PowerUp(Sprite): #para moverse y decirle que es un elemento disponible para mostrarse en pantalla
    def __init__(self, image, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(HALF_SCREEN_WIDTH, SCREEN_WIDTH) - 100 #rango en que se va a mostrar
        self.rect.y = HALF_SCREEN_HEIGHT - random.randint(25, 150)
        self.start_time = 0 #visibles por un tiempo
        self.width = self.image.get_width()
        self.type = type

    def update(self, game_speed, powerups):
        self.rect.x -= game_speed

        if self.rect.x < -self.width:
            powerups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
