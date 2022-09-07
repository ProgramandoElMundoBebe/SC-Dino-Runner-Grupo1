import pygame

FONT_FAMILY = 'freesansbold.ttf'
FONT_COLOR_BLACK = (0, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FONT_FAMILY, 30)

    text = font.render('Score: ' + str(points), True, FONT_COLOR_BLACK)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return text, text_rect

def get_text_element(text_to_display, width, height):
    font = pygame.font.Font(FONT_FAMILY, 30)

    text = font.render(text_to_display, True, FONT_COLOR_BLACK)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
