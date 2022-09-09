from components.powerups.power_up import PowerUp
from utils.constants import SHIELD, SHIELD_TYPE

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        super(Shield, self).__init__(self.image, SHIELD_TYPE)

