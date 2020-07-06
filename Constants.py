import pygame
import tcod
import sys
import os

pygame.init()

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# MISC
MAX_NAME_LEN = 12

# GAME SIZES
CAMERA_WIDTH = 800
CAMERA_HEIGHT = 600
CELL_WIDTH = 32
CELL_HEIGHT = 32

# FPS LIMIT
GAME_FPS = 60

# MAP LIMITATIONS
MAP_WIDTH = 50
MAP_HEIGHT = 50
MAP_MAX_NUM_ROOMS = 20
MAP_MAX_LEVELS = 8

#ROOM LIMITATIONS

ROOM_MAX_HEIGHT = 8
ROOM_MIN_HEIGHT = 6
ROOM_MAX_WIDTH = 8
ROOM_MIN_WIDTH = 6

# GAME DEFS
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)
COLOR_DGREY = (150, 150, 150)
COLOR_DARKERGREY = (200, 200, 200)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_PURPLE = (128, 0, 128)
COLOR_YELLOW = (255, 255, 0)


# GAME COLORS
COLOR_DEFAULT_BG = COLOR_GREY

# FOV SETTINGS
FOV_ALGO = tcod.FOV_BASIC
FOV_LIGHTWALLS = True
TORCH_RADIUS = 10

# MESSAGE DEFAULTS
NUM_MESSAGES = 8
SPACE_BETWEEN_TEXT = 5

# FONTS

fdmesspath = resource_path("data/assets/joystix monospace.ttf")
ftmesspath = resource_path("data/assets/joystix monospace.ttf")
fcmesspath = resource_path("data/assets/joystix monospace.ttf")
ftitmesspath = resource_path("data/assets/joystix monospace.ttf")
fmenmesspath = resource_path("data/assets/joystix monospace.ttf")

FONT_DEBUG_MESSAGE = pygame.font.Font(fdmesspath, 20)
FONT_MESSAGE_TEXT = pygame.font.Font(ftmesspath, 12)
FONT_CURSOR_TEXT = pygame.font.Font(ftitmesspath, CELL_HEIGHT)
FONT_TITLE_SCREEN = pygame.font.Font(fmenmesspath, 30)
FONT_MENU_TEXT = pygame.font.Font(fmenmesspath, 14)

# DEPTHS
DEPTH_PLAYER = -100
DEPTH_CREATURES = 2
DEPTH_ITEM = 1
DEPTH_CORPSE = 3
DEPTH_BACK = 4