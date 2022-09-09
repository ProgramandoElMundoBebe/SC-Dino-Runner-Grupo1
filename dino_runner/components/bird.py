import random
from components.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        self.rect.y = 230
        self.rect.x = 400