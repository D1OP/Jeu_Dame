import pygame


WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS


RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)
CHESTNUT = (88, 41, 0)


IMAGE_ROI = pygame.transform.scale(pygame.image.load('roi.jpg'), (44, 25))
