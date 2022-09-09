from winsound import PlaySound
import pygame
from components.obstacles.obstacle_manager import ObstacleManager
from components.powerups.powerup_manager import PowerUpManager
from utils.constants import BG, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from utils import text_utils
#from components.sound import PlaySound

from components.dinosaur import Dinosaur


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.dinosaur = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.powerup_manager = PowerUpManager() 
        self.points = 0
        self.game_running = True
        self.dinosaur_shield = False
        #self.playsound = PlaySound('Crome Dino.mp4')

    def run(self):
        # Game loop: events - update - draw
        self.reset_components()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_components(self):
        self.obstacle_manager.reset_obstacles()
        self.powerup_manager.reset_power_ups()
        self.points = 0

    def execute(self):
        while self.game_running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dinosaur.update(user_input)
        self.obstacle_manager.update(self)
        self.powerup_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.dinosaur.draw(self.screen)
        self.show_score()
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)

    #def play_sound(self):
        #self.playsound()

    def show_menu(self):
        self.game_running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        self.show_options_menu()

        pygame.display.update()

        self.handle_key_events_menu()

    def show_options_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        #if self.playing == True:
        text, text_rect = text_utils.get_text_element('Press any Key to Star', half_screen_width, half_screen_height)
        
        self.screen.blit(text, text_rect)

        self.screen.blit(RUNNING[0], (HALF_SCREEN_WIDTH - 20, HALF_SCREEN_HEIGHT - 140))

        #text, text_rect = text_utils.get_text_element('¿do you want to restart?', half_screen_width, half_screen_height)
        
        #self.screen.blit(text, text_rect)

        #self.screen.blit(RUNNING[0], (HALF_SCREEN_WIDTH - 20, HALF_SCREEN_HEIGHT - 140))

    def handle_key_events_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()
