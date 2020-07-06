import pygame
import os
import sys
import tcod
import random
import Constants
import math
import pickle
import gzip
import datetime
import os.path
import astar



# .........................,,...,,,,.,,,.....,,,,,,,,,,,,.........................
# .........................,**..,,,,,,*,...,*,,,,,,,,,,,..........................
# ..........................,/*..,,,,*/(.,,,,,,,,,,,,,............................
# ..........................,*/,..,,,*(#,,,,,,,,,,,,,,............................
# ...........................,*/*..,,/(..,,,.,,,,,................................
# .....,*.................,*.,*/((.,,/,.,,,....,..................................
# .......*#*...........(&%%%%.,*//*.,*..,...,###%%%*..............................
# .........##/......,%%%%%%%##.,,(##/,,*((##########%#,...............,,..........
# ........../%(/...#%##(((((((((((((((((#((############/..........*(#(............
# ..........,(#%(%%%%%##########(########(////(((((#####(.....,(/(((/.............
# .........../(#(#((((((##(##%%%%%%##((((//(((###(/((((##*..,/(#(((/..............
# ............(#&%((//(///(###((((/((((((((////(/(##((((##%(((((/((,..............
# ............,#%&(*.**,**/##%(((((//(/((((/(//////(#((((((#(/((//,...............
# ..............#%%##(((((###%###(((/////*.***(,*/(((((((((///(//,................
# ................%#((((((#(%#(((((#//(((#((////((((((((((/(////..................
# .................(##(((((%#((((((#/((((((/////((((((((#/.///*...................
# ..................*###%%%&&&%#%#(///////(((((((((((((#/.........................
# ....................,%###((((///////((%%((/((((#####(...........................
# ....................../%%%%#######%%%#########%###*.............................
# ,.........................,####################(,...............................
# ((///(#%%#(/////((/*,.,,....*#((((((((#%(,.,,...................................
# /,.......*/(/,*((///((((((#&@@&##((##(//(##,....................................
# .....................,***//((((((((((((((####%%%%#(/,...........................
# ...........................,((((/////////////////////(####%#(/,,................
# ...........................,%#(((/////////(##,..,,...,*////*,/((((####((((*,....
# ...........................##((##((/(((((((((*.......................,*((/(####(
# ...........................(#((((//////////((,............................//(/(/
# ...........................,#((//////////(((,....................,..........(/..
# .............................*#(((//(((((#(..................................,,.
# .............................,#%#(##%%%%##(.....................................
# .............................((*.......*#((,....................................
# ............................/(/..........((,....................................


#  ____ _____ ____  _   _  ____ _____
# / ___|_   _|  _ \| | | |/ ___|_   _|
# \___ \ | | | |_) | | | | |     | |
#  ___) || | |  _ <| |_| | |___  | |
# |____/ |_| |_| \_\\___/ \____| |_|


def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class struc_Tile:
    def __init__(self, block_path):
        self.block_path = block_path
        self.explored = False


class struc_Assets:
    def __init__(self):
        self.snd_list = []

        self.load_assets()
        self.sound_adjust()
        self.volume_adjust()

    def load_assets(self):

        ### SPRITESSHEETS ###

        self.csheetpath = resource_path("data/assets/creaturespritsheet.png")
        self.isheetpath = resource_path("data/assets/itemspritesheet.png")


        self.creaturespritesheet = obj_Spritesheet(self.csheetpath)
        self.itemspritesheet = obj_Spritesheet(self.isheetpath)

        # CREATURE ANIMATIONS

        self.A_RED_CHOGGUS = self.creaturespritesheet.get_animation('a', 1, 32, 32, 2)
        self.A_PURPLE_CHOGGUS = self.creaturespritesheet.get_animation('c', 1, 32, 32, 2)
        self.A_TEAL_CHOGGUS = self.creaturespritesheet.get_animation('e', 1, 32, 32, 2)
        self.A_SLEECH = self.creaturespritesheet.get_animation('a', 4, 32, 32, 2)
        self.A_GOGY = self.creaturespritesheet.get_animation('c', 4, 32, 32, 2)
        self.A_PODMAN = self.creaturespritesheet.get_animation('e', 4, 32, 32, 2)
        self.A_GREMLIN = self.creaturespritesheet.get_animation('d', 3, 32, 32, 2)
        self.A_SPITTINGSPUG = self.creaturespritesheet.get_animation('e', 2, 32, 32, 2)
        self.A_MONSTERMATRON = self.creaturespritesheet.get_animation('a', 6, 32, 32, 2)
        self.A_MATRONMINION = self.creaturespritesheet.get_animation('c', 6, 32, 32, 2)
        self.A_BOXLOX = self.creaturespritesheet.get_animation('e', 7, 32, 32, 2)
        self.A_JUGO = self.creaturespritesheet.get_animation('a', 8, 32, 32, 2)
        self.A_GREATERGREMLIN = self.creaturespritesheet.get_animation('c', 8, 32, 32, 2)
        self.A_VIXLAX = self.creaturespritesheet.get_animation('e', 8, 32, 32, 2)


        self.A_PLAYER = self.creaturespritesheet.get_animation('a', 3, 32, 32, 2)

        # BOSS ANIMATIONS
        self.A_CHOGGUSKING = self.creaturespritesheet.get_animation('e', 6, 32, 32, 2)
        self.A_SHIFTINGSERPENT = self.creaturespritesheet.get_animation('a', 7, 32, 32, 2)
        self.A_SPACEWIZARD = self.creaturespritesheet.get_animation('c', 7, 32, 32, 2)
        self.A_USM = self.creaturespritesheet.get_animation('a', 9, 32, 32, 2)


        # SPRITES

        # CORPSES
        self.S_RED_CHOGGUS_CORPSE = self.creaturespritesheet.get_image('a', 2, 32, 32)
        self.S_PURPLE_CHOGGUS_CORPSE = self.creaturespritesheet.get_image('c', 2, 32, 32)
        self.S_TEAL_CHOGGUS_CORPSE = self.creaturespritesheet.get_image('b', 2, 32, 32)
        self.S_SLEECH_CORPSE = self.creaturespritesheet.get_image('a', 5, 32, 32)
        self.S_GOGY_CORPSE = self.creaturespritesheet.get_image('c', 5, 32, 32)
        self.S_PLAYER_CORPSE = self.creaturespritesheet.get_image('c', 3, 32, 32)
        self.S_PODMAN_CORPSE = self.creaturespritesheet.get_image('e', 5, 32, 32)
        self.S_GREMLIN_CORPSE = self.creaturespritesheet.get_image('d', 2, 32, 32)
        self.S_SPITTINGSPUG_CORPSE = self.creaturespritesheet.get_image('f', 3, 32, 32)
        self.S_MONSTERMATRON_CORPSE = self.creaturespritesheet.get_image('b', 5, 32, 32)
        self.S_MATRONMINION_CORPSE = self.creaturespritesheet.get_image('d', 5, 32, 32)
        self.S_BOXLOX_CORPSE = self.creaturespritesheet.get_image('g', 3, 32, 32)
        self.S_JUGO_CORPSE = self.creaturespritesheet.get_image('g', 4, 32, 32)
        self.S_GREATERGREMLIN_CORPSE = self.creaturespritesheet.get_image('g', 5, 32, 32)
        self.S_VIXLAX_CORPSE = self.creaturespritesheet.get_image('g', 6, 32, 32)

        # BOSS CORPSES
        self.S_CHOGGUSKING_CORPSE = self.creaturespritesheet.get_image('f', 5, 32, 32)
        self.S_SHIFTINGSERPENT_CORPSE = self.creaturespritesheet.get_image('g', 1, 32, 32)
        self.S_SPACEWIZARD_CORPSE = self.creaturespritesheet.get_image('g', 2, 32, 32)
        self.S_USM_CORPSE = self.creaturespritesheet.get_image('g', 7, 32, 32)


        # ITEMS


        self.S_LASERBLASTER_GUN = self.itemspritesheet.get_image('a', 4, 32, 32)
        self.S_FIRE_GRENADE = self.itemspritesheet.get_image('b', 4, 32, 32)
        self.S_IMPLOSION_GRENADE = self.itemspritesheet.get_image('i', 2, 32, 32)
        self.S_BRAINSCRAMBLER_GUN = self.itemspritesheet.get_image('c', 4, 32, 32)
        self.S_PLURALISBLASTER_GUN = self.itemspritesheet.get_image('i', 3, 32, 32)
        self.S_PERFORMANCEENHANCER_SERUM = self.itemspritesheet.get_image('c', 1, 32, 32)
        self.S_ATTRIBOOSTER = self.itemspritesheet.get_image('i', 1, 32, 32)
        self.S_ATTRISWAPPER = self.itemspritesheet.get_image('i', 4, 32, 32)
        self.S_AUTOTRANSFUSER_SERUM = self.itemspritesheet.get_image('e', 1, 32, 32)
        self.S_VITALITYINJECTOR_SERUM = self.itemspritesheet.get_image('f', 1, 32, 32)
        self.S_IMMENSIUM_GRENADE = self.itemspritesheet.get_image('g', 5, 32, 32)
        self.S_PLURALIS_GRENADE = self.itemspritesheet.get_image('i', 5, 32, 32)
        self.S_S_BOOSTER_SERUM = self.itemspritesheet.get_image('b', 6, 32, 32)
        self.S_I_BOOSTER_SERUM = self.itemspritesheet.get_image('d', 6, 32, 32)
        self.S_D_BOOSTER_SERUM = self.itemspritesheet.get_image('a', 6, 32, 32)
        self.S_W_BOOSTER_SERUM = self.itemspritesheet.get_image('c', 6, 32, 32)

        # EQUIPMENT

        self.S_BLACKJACK = self.itemspritesheet.get_image('b', 1, 32, 32)
        self.S_GOBLINCOAT = self.itemspritesheet.get_image('a', 1, 32, 32)
        self.S_BASICVISOR = self.itemspritesheet.get_image('d', 1, 32, 32)
        self.S_PGLOVE = self.itemspritesheet.get_image('g', 3, 32, 32)
        self.S_PBOOT = self.itemspritesheet.get_image('h', 1, 32, 32)
        self.S_TOOTHPROOFVEST = self.itemspritesheet.get_image('g', 1, 32, 32)
        self.S_THINKCAP = self.itemspritesheet.get_image('h', 2, 32, 32)
        self.S_LABCOAT = self.itemspritesheet.get_image('h', 3, 32, 32)
        self.S_CHEMGRAPS = self.itemspritesheet.get_image('h', 4, 32, 32)
        self.S_CHEMSTEPS = self.itemspritesheet.get_image('h', 5, 32, 32)
        self.S_GREMLINGRIPPERS = self.itemspritesheet.get_image('h', 6, 32, 32)
        self.S_CHOGGUSCLUB = self.itemspritesheet.get_image('e', 6, 32, 32)
        self.S_GOGYSNEAKERS = self.itemspritesheet.get_image('f', 6, 32, 32)
        self.S_GREMLINCOAT = self.itemspritesheet.get_image('g', 6, 32, 32)
        self.S_PODAXE = self.itemspritesheet.get_image('i', 6, 32, 32)
        self.S_GREATERGREMLINCOAT = self.itemspritesheet.get_image('f', 5, 32, 32)
        self.S_VIXHELMET = self.itemspritesheet.get_image('c', 5, 32, 32)
        self.S_BOXGLOVE = self.itemspritesheet.get_image('a', 7, 32, 32)
        self.S_SLEECHLASH = self.itemspritesheet.get_image('e', 5, 32, 32)
        self.S_MATRONGLOVE = self.itemspritesheet.get_image('d', 5, 32, 32)

        #  BOSS LOOTS

        self.S_CHOGGUSKINGCROWN = self.itemspritesheet.get_image('d', 2, 32, 32)
        self.S_CHOGGUSKINGMANTLE = self.itemspritesheet.get_image('e', 2, 32, 32)
        self.S_SERPENTWHIP = self.itemspritesheet.get_image('f', 2, 32, 32)
        self.S_SERPENTHEAD = self.itemspritesheet.get_image('g', 2, 32, 32)
        self.S_SPWIZARDSTAFF = self.itemspritesheet.get_image('f', 4, 32, 32)
        self.S_SPWIZARDHAT = self.itemspritesheet.get_image('g', 4, 32, 32)
        self.S_USMSKULL = self.itemspritesheet.get_image('b', 7, 32, 32)


        # WALLS AND FLOORS
        self.S_WALL = self.itemspritesheet.get_image('a', 2, 32, 32)[0]
        self.S_FLOOR = self.itemspritesheet.get_image('a', 3, 32, 32)[0]

        self.S_WALL_EX = self.itemspritesheet.get_image('b', 2, 32, 32)[0]
        self.S_FLOOR_EX = self.itemspritesheet.get_image('b', 3, 32, 32)[0]

        ## SPECIAL

        self.S_STAIRDOWN = self.itemspritesheet.get_image('c', 3, 32, 32)
        self.S_STAIRDOWN_EX = self.itemspritesheet.get_image('d', 3, 32, 32)
        self.S_STAIRUP = self.itemspritesheet.get_image('e', 3, 32, 32)
        self.S_STAIRUP_EX = self.itemspritesheet.get_image('f', 3, 32, 32)
        self.S_CORENUCLEUS = self.itemspritesheet.get_image('c', 2, 32, 32)
        self.S_DOORCLOSED = self.itemspritesheet.get_image('d', 4, 32, 32)
        self.S_DOOROPEN = self.itemspritesheet.get_image('e', 4, 32, 32)

        self.animation_dict = {
            # CREATURE SPRITES
            "A_RED_CHOGGUS": self.A_RED_CHOGGUS,
            "A_PURPLE_CHOGGUS": self.A_PURPLE_CHOGGUS,
            "A_TEAL_CHOGGUS": self.A_TEAL_CHOGGUS,
            "A_SLEECH": self.A_SLEECH,
            "A_GOGY": self.A_GOGY,
            "A_PODMAN": self.A_PODMAN,
            "A_GREMLIN": self.A_GREMLIN,
            "A_SPITTINGSPUG": self.A_SPITTINGSPUG,
            "A_MONSTERMATRON": self.A_MONSTERMATRON,
            "A_MATRONMINION": self.A_MATRONMINION,
            "A_BOXLOX": self.A_BOXLOX,
            "A_JUGO": self.A_JUGO,
            "A_GREATERGREMLIN": self.A_GREATERGREMLIN,
            "A_VIXLAX": self.A_VIXLAX,


            "A_PLAYER": self.A_PLAYER,

            # BOSS ANIMATIONS

            "A_CHOGGUSKING": self.A_CHOGGUSKING,
            "A_SHIFTINGSERPENT": self.A_SHIFTINGSERPENT,
            "A_SPACEWIZARD": self.A_SPACEWIZARD,
            "A_USM": self.A_USM,

            # SPRITES

            # CORPSES
            "S_RED_CHOGGUS_CORPSE": self.S_RED_CHOGGUS_CORPSE,
            "S_PURPLE_CHOGGUS_CORPSE": self.S_PURPLE_CHOGGUS_CORPSE,
            "S_TEAL_CHOGGUS_CORPSE": self.S_TEAL_CHOGGUS_CORPSE,
            "S_SLEECH_CORPSE": self.S_SLEECH_CORPSE,
            "S_PLAYER_CORPSE": self.S_PLAYER_CORPSE,
            "S_GOGY_CORPSE": self.S_GOGY_CORPSE,
            "S_PODMAN_CORPSE": self.S_PODMAN_CORPSE,
            "S_GREMLIN_CORPSE": self.S_GREMLIN_CORPSE,
            "S_SPITTINGSPUG_CORPSE": self.S_SPITTINGSPUG_CORPSE,
            "S_MONSTERMATRON_CORPSE": self.S_MONSTERMATRON_CORPSE,
            "S_MATRONMINION_CORPSE": self.S_MATRONMINION_CORPSE,
            "S_BOXLOX_CORPSE": self.S_BOXLOX_CORPSE,
            "S_JUGO_CORPSE": self.S_JUGO_CORPSE,
            "S_GREATERGREMLIN_CORPSE": self.S_GREATERGREMLIN_CORPSE,
            "S_VIXLAX_CORPSE": self.S_VIXLAX_CORPSE,


            # BOSS CORPSES

            "S_CHOGGUSKING_CORPSE": self.S_CHOGGUSKING_CORPSE,
            "S_SHIFTINGSERPENT_CORPSE": self.S_SHIFTINGSERPENT_CORPSE,
            "S_SPACEWIZARD_CORPSE": self.S_SPACEWIZARD_CORPSE,
            "S_USM_CORPSE": self.S_USM_CORPSE,

            # BOSS LOOT

            "S_CHOGGUSKINGMANTLE": self.S_CHOGGUSKINGMANTLE,
            "S_CHOGGUSKINGCROWN": self.S_CHOGGUSKINGCROWN,
            "S_SERPENTWHIP": self.S_SERPENTWHIP,
            "S_SERPENTHEAD": self.S_SERPENTHEAD,
            "S_SPWIZARDSTAFF": self.S_SPWIZARDSTAFF,
            "S_SPWIZARDHAT": self.S_SPWIZARDHAT,
            "S_USMSKULL": self.S_USMSKULL,

            # ITEMS

            "S_LASERBLASTER_GUN": self.S_LASERBLASTER_GUN,
            "S_FIRE_GRENADE": self.S_FIRE_GRENADE,
            "S_BRAINSCRAMBLER_GUN": self.S_BRAINSCRAMBLER_GUN,
            "S_PERFORMANCEENHANCER_SERUM": self.S_PERFORMANCEENHANCER_SERUM,
            "S_AUTOTRANSFUSER_SERUM": self.S_AUTOTRANSFUSER_SERUM,
            "S_VITALITYINJECTOR_SERUM": self.S_VITALITYINJECTOR_SERUM,
            "S_PLURALISBLASTER_GUN": self.S_PLURALISBLASTER_GUN,
            "S_IMPLOSION_GRENADE": self.S_IMPLOSION_GRENADE,
            "S_ATTRIBOOSTER_SERUM": self.S_ATTRIBOOSTER,
            "S_ATTRISWAPPER_SERUM": self.S_ATTRISWAPPER,
            "S_PLURALIS_GRENADE": self.S_PLURALIS_GRENADE,
            "S_IMMENSIUM_GRENADE": self.S_IMMENSIUM_GRENADE,
            "S_S_BOOSTER_SERUM": self.S_S_BOOSTER_SERUM,
            "S_D_BOOSTER_SERUM": self.S_D_BOOSTER_SERUM,
            "S_I_BOOSTER_SERUM": self.S_I_BOOSTER_SERUM,
            "S_W_BOOSTER_SERUM": self.S_W_BOOSTER_SERUM,

            # EQUIPMENT

            "S_BLACKJACK": self.S_BLACKJACK,
            "S_GOBLINCOAT": self.S_GOBLINCOAT,
            "S_BASICVISOR": self.S_BASICVISOR,
            "S_PGLOVE": self.S_PGLOVE,
            "S_PBOOT": self.S_PBOOT,
            "S_TOOTHPROOFVEST": self.S_TOOTHPROOFVEST,
            "S_THINKCAP": self.S_THINKCAP,
            "S_CHEMGRAPS": self.S_CHEMGRAPS,
            "S_CHEMSTEPS": self.S_CHEMSTEPS,
            "S_LABCOAT": self.S_LABCOAT,
            "S_GREMLINGRIPPERS": self.S_GREMLINGRIPPERS,
            "S_GREMLINCOAT": self.S_GREMLINCOAT,
            "S_PODAXE": self.S_PODAXE,
            "S_CHOGGUSCLUB": self.S_CHOGGUSCLUB,
            "S_GOGYSNEAKERS": self.S_GOGYSNEAKERS,
            "S_VIXHELMET": self.S_VIXHELMET,
            "S_MATRONGLOVE": self.S_MATRONGLOVE,
            "S_SLEECHLASH": self.S_SLEECHLASH,
            "S_GREATERGREMLINCOAT": self.S_GREATERGREMLINCOAT,
            "S_BOXGLOVE": self.S_BOXGLOVE,

            ## SPECIAL

            "S_STAIRDOWN": self.S_STAIRDOWN,
            "S_STAIRDOWN_EX": self.S_STAIRDOWN_EX,
            "S_STAIRUP": self.S_STAIRUP,
            "S_STAIRUP_EX": self.S_STAIRUP_EX,
            "S_CORENUCLEUS": self.S_CORENUCLEUS,
            "S_DOORCLOSED": self.S_DOORCLOSED,
            "S_DOOROPEN": self.S_DOOROPEN

        }

        ## AUDIO

        self.mbackgroundpath = resource_path("data/audio/music/gameloop1.wav")
        self.mmenupath = resource_path("data/audio/music/menu music.wav")

        self.hit1path = resource_path("data/audio/sfx/Hit_1.wav")
        self.hit2path = resource_path("data/audio/sfx/Hit_2.wav")
        self.hit3path = resource_path("data/audio/sfx/Hit_3.wav")
        self.hit4path = resource_path("data/audio/sfx/Hit_4.wav")
        self.hit5path = resource_path("data/audio/sfx/Hit_5.wav")

        self.music_background = self.mbackgroundpath
        self.music_menu = self.mmenupath
        self.sfx_hit_1 = self.sound_add(self.hit1path)
        self.sfx_hit_2 = self.sound_add(self.hit2path)
        self.sfx_hit_3 = self.sound_add(self.hit3path)
        self.sfx_hit_4 = self.sound_add(self.hit4path)
        self.sfx_hit_5 = self.sound_add(self.hit5path)

        self.sfx_list_hit = [self.sfx_hit_1, self.sfx_hit_2, self.sfx_hit_3,
                             self.sfx_hit_4, self.sfx_hit_5]

        self.miss1path = resource_path("data/audio/sfx/Miss_1.wav")
        self.miss2path = resource_path("data/audio/sfx/Miss_2.wav")
        self.miss3path = resource_path("data/audio/sfx/Miss_3.wav")
        self.miss4path = resource_path("data/audio/sfx/Miss_4.wav")
        self.miss5path = resource_path("data/audio/sfx/Miss_5.wav")

        self.sfx_miss_1 = self.sound_add(self.miss1path)
        self.sfx_miss_2 = self.sound_add(self.miss2path)
        self.sfx_miss_3 = self.sound_add(self.miss3path)
        self.sfx_miss_4 = self.sound_add(self.miss4path)
        self.sfx_miss_5 = self.sound_add(self.miss5path)

        self.sfx_list_miss = [self.sfx_miss_1, self.sfx_miss_2, self.sfx_miss_3,
                              self.sfx_miss_4, self.sfx_miss_5]

        self.crit1path = resource_path("data/audio/sfx/Crit_1.wav")
        self.crit2path = resource_path("data/audio/sfx/Crit_2.wav")
        self.crit3path = resource_path("data/audio/sfx/Crit_3.wav")
        self.crit4path = resource_path("data/audio/sfx/Crit_4.wav")

        self.sfx_crit_1 = self.sound_add(self.crit1path)
        self.sfx_crit_2 = self.sound_add(self.crit2path)
        self.sfx_crit_3 = self.sound_add(self.crit3path)
        self.sfx_crit_4 = self.sound_add(self.crit4path)

        self.sfx_list_crit = [self.sfx_crit_1, self.sfx_crit_2, self.sfx_crit_3,
                              self.sfx_crit_4]

    def sound_add(self, file_address):
        new_sound = pygame.mixer.Sound(file_address)

        self.snd_list.append(new_sound)

        return new_sound

    def sound_adjust(self):

        for sound in self.snd_list:
            sound.set_volume(PREFERENCES.vol_sound)

        pygame.mixer.music.set_volume(PREFERENCES.vol_music)

    def volume_adjust(self):

        for sound in self.snd_list:
            sound.set_volume(PREFERENCES.vol_sound)

        pygame.mixer.music.set_volume(PREFERENCES.vol_music)


class struc_Preferences():

    def __init__(self):
        self.vol_sound = 0.5
        self.vol_music = 0.5


#   ___  ____      _ _____ ____ _____ ____
#  / _ \| __ )    | | ____/ ___|_   _/ ___|
# | | | |  _ \ _  | |  _|| |     | | \___ \
# | |_| | |_) | |_| | |__| |___  | |  ___) |
#  \___/|____/ \___/|_____\____| |_| |____/

class obj_Actor:
    def __init__(self, x, y,
                 name_object,
                 animation_key,
                 animation_speed=0.5,
                 depth=0,
                 state=None,

                 # components
                 creature=None,
                 ai=None,
                 container=None,
                 stairs=None,
                 item=None,
                 equipment=None,
                 exitportal=None):
        self.x = x  # map address
        self.y = y  # map address
        self.name_object = name_object
        self.animation_key = animation_key
        self.animation = ASSETS.animation_dict[animation_key]
        self.depth = depth
        self.state = None
        self.animation_speed = animation_speed

        # animation flicker speed
        self.flicker_speed = (self.animation_speed / len(self.animation))
        self.flicker_timer = 0.0
        self.sprite_image = 0

        self.container = container
        if container:
            if self.container:
                self.container.owner = self

        self.creature = creature
        if creature:
            self.creature.owner = self
            self.to_hit = self.creature.to_hit
            self.ac = self.creature.ac

        self.ai = ai
        if ai:
            self.ai.owner = self

        self.exitportal = exitportal
        if self.exitportal:
            self.exitportal.owner = self

        self.item = item
        if item:
            self.corpse = item.corpse
            if self.item:
                self.item.owner = self

        self.equipment = equipment
        if self.equipment:
            self.equipment.owner = self

            self.item = com_Item()
            self.item.owner = self

        self.stairs = stairs
        if self.stairs:
            self.stairs.owner = self

    def update_name(self, name):

        self.creature.name_instance = str(name)

    @property
    def display_name(self):

        if self.creature:
            return (self.creature.name_instance + " the " + self.name_object)

        if self.item:
            if self.equipment and self.equipment.equipped:
                return (self.name_object + "[E]")
            elif self.item.item_name:
                return (self.item.item_name)
            else:
                return (self.name_object)

    def draw(self):
        is_visible = tcod.map_is_in_fov(FOV_MAP, self.x, self.y)

        if is_visible:
            if len(self.animation) == 1:
                SURFACE_MAP.blit(self.animation[0], (self.x * Constants.CELL_WIDTH, self.y * Constants.CELL_HEIGHT))
            elif len(self.animation) > 1:
                if CLOCK.get_fps() > 0.0:
                    self.flicker_timer += 1 / CLOCK.get_fps()

                if self.flicker_timer >= self.flicker_speed:
                    self.flicker_timer = 0.0

                    if self.sprite_image >= len(self.animation) - 1:
                        self.sprite_image = 0

                    else:
                        self.sprite_image += 1

                SURFACE_MAP.blit(self.animation[self.sprite_image],
                                 (self.x * Constants.CELL_WIDTH, self.y * Constants.CELL_HEIGHT))

    def distance_to(self, other):

        dx = other.x - self.x
        dy = other.y - self.y

        return math.sqrt(dx ** 2 + dy ** 2)

    def move_towards(self, target):

        path = tcod.path_new_using_map(FOV_MAP, 1.0)
        tcod.path_compute(path, self.x, self.y, target.x, target.y)

        if tcod.path_size(path) > 0:
            new_x, new_y = tcod.path_get(path, 0)

            tcod.map_set_properties(FOV_MAP, self.x, self.y, not GAME.current_map[self.x][self.y].block_path, True)
            tcod.map_set_properties(FOV_MAP, new_x, new_y, not GAME.current_map[new_x][new_y].block_path, False)

            self.x = new_x
            self.y = new_y

    def move_away(self, other):

        dx = self.x - other.x
        dy = self.y - other.y

        distance = math.sqrt(dx ** 2 + dy ** 2)

        dx = int(round(dx / distance))
        dy = int(round(dy / distance))

        self.creature.move(dx, dy)

    def animation_destroy(self):

        self.animation = None

    def animation_init(self):

        self.animation = ASSETS.animation_dict[self.animation_key]

    def draw_health_rect(self):
        if self.creature:
            current_hp = self.creature.current_hp

            if current_hp > Constants.CELL_WIDTH:
                bar_w = Constants.CELL_WIDTH
            else:
                bar_w = current_hp
            bar_h = 3

            rect_surf = pygame.Surface((bar_w, bar_h))
            if current_hp < self.creature.max_hp and current_hp > 0:
                if bar_w == Constants.CELL_WIDTH:
                    pygame.Surface.fill(rect_surf, Constants.COLOR_YELLOW)
                else:
                    pygame.Surface.fill(rect_surf, Constants.COLOR_RED)

                SURFACE_MAP.blit(rect_surf, (self.x * Constants.CELL_WIDTH, self.y * Constants.CELL_HEIGHT + 33))


class obj_Game:
    def __init__(self):
        self.current_objects = []
        self.message_history = []
        self.maps_previous = []
        self.maps_next = []
        self.current_map, self.current_rooms = map_create()
        self.name = None

    def transition_next(self):

        global FOV_CALCULATE

        FOV_CALCULATE = True

        for obj in self.current_objects:
            obj.animation_destroy()

        self.maps_previous.append((PLAYER.x, PLAYER.y, self.current_map,
                                   self.current_rooms, self.current_rooms,
                                   self.current_objects))

        if len(self.maps_next) == 0:

            self.current_objects = [PLAYER]

            PLAYER.animation_init()

            self.current_map, self.current_rooms = map_create()
            map_place_objects(self.current_rooms)

        else:
            (PLAYER.x, PLAYER.y, self.current_map, self.current_rooms,
             self.current_rooms, self.current_objects) = self.maps_next[-1]

            for obj in self.current_objects:
                obj.animation_init()

            map_make_fov(self.current_map)

            del self.maps_next[-1]

    def transition_previous(self):

        global FOV_CALCULATE

        if len(self.maps_previous) != 0:

            for obj in self.current_objects:
                obj.animation_destroy()

            self.maps_next.append((PLAYER.x, PLAYER.y, self.current_map, self.current_rooms,
                                   self.current_rooms, self.current_objects))

            (PLAYER.x, PLAYER.y, self.current_map, self.current_rooms,
             self.current_rooms, self.current_objects) = self.maps_previous[-1]

            for obj in self.current_objects:
                obj.animation_init()

            map_make_fov(self.current_map)

            FOV_CALCULATE = True

            del self.maps_previous[-1]


class obj_Spritesheet:
    # USED TO GET IMAGES FROM A SPRITESHEET
    def __init__(self, file_name):
        # LOAD IN THE SPRITESHEET
        self.spritesheet = pygame.image.load(file_name).convert()
        self.tiledict = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
                         'e': 5, 'f': 6, 'g': 7,
                         'h': 8, 'i': 9, 'j': 10,
                         'k': 11, 'l': 12, 'm': 13,
                         'n': 14, 'o': 15, 'p': 16}

    ###############

    def get_image(self, col, row, width=Constants.CELL_WIDTH, height=Constants.CELL_HEIGHT, scale=None):

        image_list = []

        image = pygame.Surface([width, height]).convert()

        image.blit(self.spritesheet, (0, 0), (self.tiledict[col] * width, row * height, width, height))

        image.set_colorkey(Constants.COLOR_BLACK)

        if scale:
            (new_w, new_h) = scale
            image = pygame.transform.scale(image, (new_w, new_h))

        image_list.append(image)

        return image_list

    def get_animation(self, col, row, width=Constants.CELL_WIDTH, height=Constants.CELL_HEIGHT, num_sprites=1,
                      scale=None):

        image_list = []

        for i in range(num_sprites):
            # CREATE BLANK IMAGE
            image = pygame.Surface([width, height]).convert()

            # COPY IMAGE FROM SHEET ONTO BLANK
            image.blit(self.spritesheet, (0, 0),
                       (self.tiledict[col] * width + (width * i), row * height, width, height))

            # SET TRANSPARENCY KEY TO BLACK
            image.set_colorkey(Constants.COLOR_BLACK)

            if scale:
                (new_w, new_h) = scale
                image = pygame.transform.scale(image, (new_w, new_h))

            image_list.append(image)

        return image_list


class obj_Room:
    # THIS IS A RECTANGLE THAT LIVES ON THE MAP
    def __init__(self, coords, size):
        self.x1, self.y1 = coords
        self.w, self.h = size

        self.x2 = self.x1 + self.w
        self.y2 = self.y1 + self.h

    @property
    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2

        return int(center_x), int(center_y)

    def intersect(self, other):
        # return True if other obj intersects with this one
        objects_intersect = (self.x1 <= other.x2 and self.x2 >= other.x1 and
                             self.y1 <= other.y2 and self.y2 >= other.y1)

        return objects_intersect


class obj_Camera:
    def __init__(self):
        self.width = Constants.CAMERA_WIDTH
        self.height = Constants.CAMERA_HEIGHT
        self.x, self.y = (0, 0)

    @property
    def rectangle(self):
        pos_rect = pygame.Rect((0, 0), (Constants.CAMERA_WIDTH, Constants.CAMERA_HEIGHT))

        pos_rect.center = self.x, self.y

        return pos_rect

    @property
    def map_address(self):
        map_x = int(self.x / Constants.CELL_WIDTH)
        map_y = int(self.y / Constants.CELL_HEIGHT)

        return (map_x, map_y)

    def update(self):
        target_x = int(PLAYER.x * Constants.CELL_WIDTH + (Constants.CELL_WIDTH / 2))
        target_y = int(PLAYER.y * Constants.CELL_HEIGHT + (Constants.CELL_HEIGHT / 2))

        distance_x, distance_y = self.map_dist((target_x, target_y))

        self.x += int(distance_x)
        self.y += int(distance_y)

    def win_to_map(self, coords):
        tar_x, tar_y = coords

        # convert coords into distance from camera

        cam_d_x, cam_d_y = self.camera_dist((tar_x, tar_y))

        # convert distance from camera into map coord
        map_p_x = int(self.x + cam_d_x)
        map_p_y = int(self.y + cam_d_y)

        return (map_p_x, map_p_y)

    def map_dist(self, coords):
        new_x, new_y = coords

        dist_x = int(new_x - self.x)
        dist_y = int(new_y - self.y)

        return (dist_x, dist_y)

    def camera_dist(self, coords):
        win_x, win_y = coords

        dist_x = int(win_x - (self.width / 2))
        dist_y = int(win_y - (self.height / 2))

        return (dist_x, dist_y)


#   ____ ___  __  __ ____   ___  _   _ _____ _   _ _____ ____
#  / ___/ _ \|  \/  |  _ \ / _ \| \ | | ____| \ | |_   _/ ___|
# | |  | | | | |\/| | |_) | | | |  \| |  _| |  \| | | | \___ \
# | |__| |_| | |  | |  __/| |_| | |\  | |___| |\  | | |  ___) |
#  \____\___/|_|  |_|_|    \___/|_| \_|_____|_| \_| |_| |____/

# creatures have health,  can damage other objects by attacking them, and can die
class com_Creature:
    def __init__(self,
                 name_instance,
                 base_atk=2,
                 base_chance=0,
                 base_str=10,
                 base_dex=10,
                 base_con=10,
                 base_int=10,
                 base_wis=10,
                 base_def=0,
                 base_ac=10,
                 hp=10,
                 current_xp=0,
                 xp_reward=0,
                 level=1,
                 death_function=None,
                 state=None,
                 creature_d=None):
        self.name_instance = name_instance
        self.death_function = death_function
        self.base_chance = base_chance
        self.base_atk = base_atk
        self.base_str = base_str
        self.base_dex = base_dex
        self.base_con = base_con
        self.base_int = base_int
        self.base_wis = base_wis
        self.base_def = base_def
        self.base_ac = base_ac
        self.hp = hp + int(base_con / 5)
        self.max_hp = hp + int(base_con / 5)
        self.current_hp = hp + int(base_con / 5)
        self.creature_d = creature_d
        self.current_xp = current_xp
        self.xp_reward = xp_reward
        self.charpoints = 0
        self.level = 1

    def increase_stat(self, stat, target):
        self.stat = stat
        if target.creature.charpoints > 0:
            if stat == 1:
                target.creature.base_con += 1
                game_message("your constitution went up!", Constants.COLOR_PURPLE)
                target.creature.max_hp += 5
                target.creature.current_hp += 5
                target.creature.charpoints -= 1
            if stat == 2:
                target.creature.base_str += 1
                game_message("your strength went up!", Constants.COLOR_PURPLE)
                target.creature.charpoints -= 1
            if stat == 3:
                target.creature.base_dex += 1
                game_message("your dexterity went up!", Constants.COLOR_PURPLE)
                target.creature.charpoints -= 1
            if stat == 4:
                target.creature.base_int += 1
                game_message("your intelligence went up!", Constants.COLOR_PURPLE)
                target.creature.charpoints -= 1
            if stat == 5:
                target.creature.base_wis += 1
                game_message("your wisdom went up!", Constants.COLOR_PURPLE)
                target.creature.charpoints -= 1

        else:
            game_message("not enough character points")

    def get_xp(self, xp_reward, target):
        target.current_xp += xp_reward
        xp_to_level = (target.level * target.level) * 100
        if target.current_xp >= xp_to_level:
            target.charpoints += 2
            target.level += 1
            target.max_hp += random.randint(2, 3)
            target.current_hp += random.randint(1, 2)
            game_message("you level up!")

    # MOVES CREATURE, STOPS ON WALLS AND TARGETS, ATTACKS IF MOVING WOULD PLACE SELF ON TARGET
    def move(self, dx, dy):

        tile_is_wall = (GAME.current_map[self.owner.x + dx][self.owner.y + dy].block_path == True)

        target = map_check_for_creatures(self.owner.x + dx, self.owner.y + dy, self.owner)

        # IF TARGET, ATTACKS
        if target:
            self.attack(target)
        # IF WALL, DOESNT MOVE
        if not tile_is_wall and not target:
            self.owner.x += dx
            self.owner.y += dy

    # PRINTS DAMAGENUMBER AND NAMES ON SCREEN
    def attack(self, target):

        # gets info on own tohit bonus and targets armor class
        to_hit = self.to_hit
        this_ac = target.creature.ac

        # calculates how much damage will be dealt on hit
        damage_roll = random.randint(int(self.atk_power / 2), int(self.atk_power)) - target.creature.defense
        damage_dealt = damage_roll

        # rolls for hit
        atk_roll = (random.randint(1, 21) + to_hit)

        # if hits shows hit message and damage

        if (atk_roll - to_hit) == 20:
            if self.owner is PLAYER:
                crit_sound = (random.choice(ASSETS.sfx_list_crit))
                pygame.mixer.Sound.play(crit_sound)

            game_message(self.name_instance + " CRITICALLY HITS " + target.creature.name_instance + " FOR "
                         + str(damage_dealt * 2) + " DAMAGE!", Constants.COLOR_GREEN)
            target.creature.take_damage(damage_dealt * 2)

        elif this_ac <= atk_roll:
            game_message(self.name_instance + " rolls a " + str(atk_roll) + " and hits " + target.creature.name_instance
                         + " for " + str(damage_dealt) + " damage!", Constants.COLOR_WHITE)
            target.creature.take_damage(damage_dealt)

            if self.owner is PLAYER:
                hit_sound = (random.choice(ASSETS.sfx_list_hit))
                pygame.mixer.Sound.play(hit_sound)

        # is misses shows roll result and message
        else:

            game_message(
                self.name_instance + " rolls a " + str(atk_roll) + " and misses " + target.creature.name_instance)

            if self.owner is PLAYER:
                miss_sound = (random.choice(ASSETS.sfx_list_miss))
                pygame.mixer.Sound.play(miss_sound)

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.owner == PLAYER:
            game_message(self.name_instance + "'s health is " + str(self.current_hp) + "/" + str(self.max_hp),
                         Constants.COLOR_RED)
        else:
            if self.current_hp <= 0:
                game_message(self.name_instance + "'s health is " + str(0) + "/" + str(self.max_hp),
                             Constants.COLOR_GREEN)

            else:
                game_message(self.name_instance + "'s health is " + str(self.current_hp) + "/" + str(self.max_hp),
                             Constants.COLOR_GREEN)

        if self.current_hp <= 0:

            if self.death_function:
                death_monster(self.owner)

    def heal(self, amount):
        self.current_hp += amount

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

    def display_stats(self):
        all_stat_list = []

        all_stat_list.append("Level:" + str(self.level))
        all_stat_list.append("xp:" + str(self.current_xp))
        all_stat_list.append("Character Points:" + str(self.charpoints))
        all_stat_list.append("max hp:" + str(self.max_hp))
        all_stat_list.append("current hp:" + str(self.current_hp))
        all_stat_list.append("[1] constitution:" + str(self.constitution))
        all_stat_list.append("[2] strength:" + str(self.strength))
        all_stat_list.append("[3] dexterity:" + str(self.dexterity))
        all_stat_list.append("[4] intelligence:" + str(self.intelligence))
        all_stat_list.append("[5] wisdom:" + str(self.wisdom))
        all_stat_list.append("attack power:" + str(self.atk_power))
        all_stat_list.append("attack bonus:" + str(self.to_hit))
        all_stat_list.append("device damage bonus:" + str(int(self.intelligence/5)))
        all_stat_list.append("serum power bonus:" + str(int(self.wisdom / 5)))
        all_stat_list.append("defense:" + str(self.defense))
        all_stat_list.append("armor class:" + str(self.ac))

        return all_stat_list

    @property
    def dexterity(self):

        total_dex = self.base_dex

        if self.owner.container:
            object_bonuses = [obj.equipment.dexterity_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_dex += bonus

        return total_dex

    @property
    def strength(self):

        total_str = self.base_str

        if self.owner.container:
            object_bonuses = [obj.equipment.strength_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_str += bonus

        return total_str

    @property
    def constitution(self):

        total_con = self.base_con

        if self.owner.container:
            object_bonuses = [obj.equipment.constitution_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_con += bonus

        return total_con

    @property
    def intelligence(self):
        total_int = self.base_int

        if self.owner.container:
            object_bonuses = [obj.equipment.intelligence_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_int += bonus

        return total_int

    @property
    def wisdom(self):
        total_wis = self.base_wis

        if self.owner.container:
            object_bonuses = [obj.equipment.wisdom_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_wis += bonus

        return total_wis

    @property
    def atk_power(self):

        total_power = self.base_atk + int(self.strength / 5)

        if self.owner.container:
            object_bonuses = [obj.equipment.attack_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_power += bonus

        return total_power

    @property
    def to_hit(self):

        total_chance = self.base_chance + int(self.dexterity / 5)

        if self.owner.container:
            object_bonuses = [obj.equipment.chance_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_chance += bonus

        return total_chance

    @property
    def defense(self):

        total_defense = self.base_def

        if self.owner.container:
            object_bonuses = [obj.equipment.defense_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_defense += bonus

        return total_defense

    @property
    def ac(self):

        total_ac = self.base_ac + int(self.dexterity / 5)

        if self.owner.container:
            object_bonuses = [obj.equipment.ac_bonus for obj in self.owner.container.equipped_items]

            for bonus in object_bonuses:
                if bonus:
                    total_ac += bonus

        return total_ac


class com_Container:
    def __init__(self, max_items=16, inventory=None):
        self.inventory = inventory
        self.max_items = max_items
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    # get names of everything in inventory

    # get items in container
    @property
    def item_amount(self):
        num_items = len(self.inventory)

        return num_items

    # get a list of all equipped items
    @property
    def equipped_items(self):
        list_of_equipped_items = [obj for obj in self.inventory if obj.equipment and obj.equipment.equipped]

        return list_of_equipped_items

    # get weight of everything in inventory


class com_Item:
    '''Items are components that can be picked up and used.

    Attributes:

    '''

    def __init__(self, use_function=None,
                 value=None, corpse=None, item_name=None, num_charges=0, item_d=None):

        self.value = value
        self.use_function = use_function
        self.corpse = corpse
        self.item_name = item_name
        self.num_charges = num_charges
        self.item_d = item_d

    def pick_up(self, actor):

        '''The item is picked up and placed into an object's inventory.

        When called, this method seeks to place the item into an object's
        inventory if there is room.  It then removes the item from a Game's
        current_objects list.

        Args:
            actor (obj_Actor): the object that is picking up the item.

        '''

        if actor.container:  # first, checks for container component

            # does the container have room for this object?
            if actor.container.item_amount + 1 > actor.container.max_items:

                # if no, print error message
                game_message("Not enough room to pick up")
            else:
                # otherwise, pick the item up, remove from GAME.current_objects
                # message the player
                game_message('Picking up')

                # add to actor inventory
                actor.container.inventory.append(self.owner)

                self.owner.animation_destroy()
                # remove from game active list
                GAME.current_objects.remove(self.owner)

                # tell item what container holds it
                self.current_container = actor.container

    def drop(self, new_x, new_y):

        '''Drops the item onto the ground.

        This method removes the item from the actor.container inventory and
        places it into the GAME.current_objects list.  Drops the item at the
        location defined in the args.

        Args:
            new_x (int): x coord on the map to drop item
            new_y (int): y coord on the map to drop item

        '''

        # add this item to tracked objects
        GAME.current_objects.append(self.owner)

        self.owner.animation_init()

        # remove from the inventory of whatever actor holds it
        if self.owner.equipment:
            if self.owner.equipment.equipped == True:
                self.owner.equipment.unequip()

        self.current_container.inventory.remove(self.owner)

        # set item location to as defined in the args
        self.owner.x = new_x
        self.owner.y = new_y

        # confirm successful placement with game message
        game_message("Item Dropped!")

    def use(self):

        '''Use the item by producing an effect and removing it.

        '''

        if self.owner.equipment:
            self.owner.equipment.toggle_equip()
            return

        if self.use_function:
            result = self.use_function(self.current_container.owner, self.value)

            if result != None:

                print("use function failed")
            else:
                if self.num_charges <= 1:
                    self.current_container.inventory.remove(self.owner)
                else:
                    self.num_charges -= 1
                    game_message("The " + self.item_name + " has " + str(self.num_charges) + " charge(s) left")


class com_Equipment:

    def __init__(self, slot=None,
                 attack_bonus=0,
                 defense_bonus=0,
                 chance_bonus=0,
                 ac_bonus=0,
                 constitution_bonus=0,
                 strength_bonus=0,
                 dexterity_bonus=0,
                 intelligence_bonus=0,
                 wisdom_bonus=0,
                 equipment_d=None):

        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.chance_bonus = chance_bonus
        self.ac_bonus = ac_bonus
        self.slot = slot
        self.equipment_d = equipment_d

        self.constitution_bonus = constitution_bonus
        self.strength_bonus = strength_bonus
        self.dexterity_bonus = dexterity_bonus
        self.intelligence_bonus = intelligence_bonus
        self.wisdom_bonus = wisdom_bonus

        self.equipped = False


    def stat_display(self):
        display = []

        display.append(str(self.equipment_d))
        if self.ac_bonus > 0:
            display.append("armor class bonus:" + str(self.ac_bonus))
        if self.defense_bonus > 0:
            display.append("defense bonus:" + str(self.defense_bonus))
        if self.chance_bonus > 0:
            display.append("chance to hit bonus:" + str(self.chance_bonus))
        if self.attack_bonus > 0:
            display.append("damage bonus:" + str(self.attack_bonus))
        if self.constitution_bonus > 0:
            display.append("Constitution bonus:" + str(self.constitution_bonus))
        if self.strength_bonus > 0:
            display.append("strength bonus:" + str(self.strength_bonus))
        if self.dexterity_bonus > 0:
            display.append("dexterity bonus:" + str(self.dexterity_bonus))
        if self.intelligence_bonus > 0:
            display.append("intelligence bonus:" + str(self.intelligence_bonus))
        if self.wisdom_bonus > 0:
            display.append("wisdom bonus:" + str(self.wisdom_bonus))

        return display

    def toggle_equip(self):

        if self.equipped:
            self.unequip()
        else:
            self.equip()

    def equip(self):

        # check for equipment in slot
        all_equipped_items = self.owner.item.current_container.equipped_items

        if all_equipped_items:
            for item in all_equipped_items:
                if item.equipment.slot and (item.equipment.slot == self.slot):
                    game_message("Equipment slot is occupied", Constants.COLOR_RED)
                    return

        self.equipped = True

        game_message("item equipped", Constants.COLOR_WHITE)

    def unequip(self):
        # toggle self.equipped
        self.equipped = False

        game_message("item unequipped", Constants.COLOR_WHITE)


class com_Stairs:
    def __init__(self, downwards=True):

        self.downwards = downwards

    def use(self):

        if self.downwards:
            GAME.transition_next()
            if (len(GAME.maps_previous)+1) == 4 or (len(GAME.maps_previous)+1) == 8:
                game_message("you descend into floor " + str(len(GAME.maps_previous) + 1) + ", a powerful boss monster lurks in this floor", Constants.COLOR_YELLOW)
            else:
                game_message("you descend into floor " + str(len(GAME.maps_previous) + 1), Constants.COLOR_GREY)
        else:
            GAME.transition_previous()
            game_message("you ascend into floor " + str(len(GAME.maps_previous)+1), Constants.COLOR_GREY)


class com_Exitportal:
    def __init__(self):
        self.OPENSPRITE = "S_DOOROPEN"
        self.CLOSEDSPRITE = "S_DOORCLOSED"

    def update(self):
        # flag initialization
        found_core = False

        # check conditions
        portal_open = self.owner.state == "OPEN"

        for obj in PLAYER.container.inventory:
            if obj.name_object == "CORENUCLEUS":
                found_core = True

        if found_core and not portal_open:
            self.owner.state = "OPEN"
            self.owner.animation_key = self.OPENSPRITE
            self.owner.animation_init()

        if not found_core and portal_open:
            self.owner.state = "CLOSED"
            self.owner.animation_key = self.CLOSEDSPRITE
            self.owner.animation_init()

    def use(self):

        if self.owner.state == "OPEN":

            PLAYER.state = "STATUS_WIN"

            SURFACE_MAIN.fill(Constants.COLOR_WHITE)

            screen_center = (Constants.CAMERA_WIDTH / 2, Constants.CAMERA_HEIGHT / 2)

            draw_text(SURFACE_MAIN,
                      "YOU WON!",
                      Constants.FONT_TITLE_SCREEN,
                      screen_center,
                      Constants.COLOR_BLACK, center=True)

            pygame.display.update()

            filename = ("data\legacy\winrecord_" +
                        PLAYER.creature.name_instance + "." +
                        datetime.date.today().strftime("%Y%B%d") +
                        ".txt")

            file_exists = os.path.isfile(filename)
            save_exists = os.path.isfile("data\savedata")

            if file_exists: os.remove(filename)
            if save_exists: os.remove("data\savedata")

            legacy_file = open(filename, 'a+')

            legacy_file.write("******THIS CHARACTER WON!******" + "\n")

            for message, color in GAME.message_history:
                legacy_file.write(message + "\n")

            pygame.time.wait(2000)


#     _    ___
#    / \  |_ _|
#   / _ \  | |
#  / ___ \ | |
# /_/   \_\___|

class ai_Confuse:
    # once per turn, executes
    def __init__(self, old_ai, num_turns):

        self.old_ai = old_ai
        self.num_turns = num_turns

    def take_turn(self):
        if self.num_turns > 0:
            self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))

            self.num_turns -= 1

        else:
            self.owner.ai = self.old_ai

            game_message(self.owner.display_name + " has broken free!",
                         Constants.COLOR_RED)


class ai_Chase:
    ''' A basic monster ai, tries to chase and harm player'''

    def take_turn(self):

        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):

            # if far away from player, attempt to move closer
            if monster.distance_to(PLAYER) >= 2:
                self.owner.move_towards(PLAYER)

            # if close enough, attempt to attack player
            elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                monster.creature.attack(PLAYER)

class ai_Doublehit:
    ''' A basic monster ai, tries to chase and harm player'''

    def take_turn(self):

        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):

            # if far away from player, attempt to move closer
            if monster.distance_to(PLAYER) >= 2:
                self.owner.move_towards(PLAYER)

            # if close enough, attempt to attack player
            elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                monster.creature.attack(PLAYER)
                monster.creature.attack(PLAYER)

class ai_Chogking:

    def take_turn(self):

        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):
            spawn_creature = random.randint(0, 10)

            if monster.creature.current_hp > int(monster.creature.max_hp/3):
                # if far away from player, attempt to move closer
                if monster.distance_to(PLAYER) >= 2:
                    self.owner.move_towards(PLAYER)

                # if close enough, attempt to attack player
                elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                    monster.creature.attack(PLAYER)
            else:
                if spawn_creature <= 9:
                    game_message("the choggus king cries for help but nobody answers", Constants.COLOR_YELLOW)
                    if monster.distance_to(PLAYER) >= 2:
                        self.owner.move_towards(PLAYER)

                    # if close enough, attempt to attack player
                    elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                        monster.creature.attack(PLAYER)
                elif spawn_creature == 10:
                    game_message("a choggus arrives to help his king!", Constants.COLOR_YELLOW)
                    new_item = gen_enemy_choggus((monster.x, monster.y))
                    GAME.current_objects.append(new_item)

class ai_Spacewizard:

    def take_turn(self):

        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):
            charge = random.randint(1, 5)

            # if far away from player, attempt to move closer
            if charge != 5:
                if monster.distance_to(PLAYER) >= 4:
                    self.owner.move_towards(PLAYER)

                # if close enough, attempt to attack player
                elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                    monster.creature.attack(PLAYER)
            else:
                game_message("the space wizard pushes you with his magic!", Constants.COLOR_YELLOW)
                PLAYER.move_away(monster)
                PLAYER.move_away(monster)

class ai_USM:
    def take_turn(self):

        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):

            # if far away from player, attempt to move closer
            if monster.distance_to(PLAYER) >= 2:
                self.owner.move_towards(PLAYER)
                self.owner.move_towards(PLAYER)

            # if close enough, attempt to attack player
            elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                if monster.creature.current_hp > monster.creature.max_hp/3:
                    monster.creature.attack(PLAYER)
                else:
                    monster.creature.attack(PLAYER)
                    monster.creature.attack(PLAYER)

class ai_Ranged:
    ''' A basic monster ai, tries to chase and harm player'''

    def take_turn(self):

        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):

            # if far away from player, attempt to move closer
            if monster.distance_to(PLAYER) >= 4:
                self.owner.move_towards(PLAYER)

            # if close enough, attempt to attack player
            elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                monster.creature.attack(PLAYER)

class ai_Flee:

    def take_turn(self):
        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):
            self.owner.move_away(PLAYER)

class ai_Spawner:
    ''' A basic monster ai, tries to chase and harm player'''
    def take_turn(self):

        monster = self.owner



        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):
            spawn_creature = random.randint(0, 10)

            if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):
                # if far from player, keep moving away
                if spawn_creature < 10:
                    if monster.distance_to(PLAYER) >= 2:
                        self.owner.move_away(PLAYER)


                    # if close enough, attempt to attack player
                    elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                        monster.creature.attack(PLAYER)
                elif spawn_creature == 10:
                    new_item = gen_enemy_matronminion((monster.x, monster.y))
                    GAME.current_objects.append(new_item)

class ai_Fleefight:
    # ai for creatures that flee on sight but fight if cornered

    def take_turn(self):
        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):
            # if far from player, keep moving away
            if monster.distance_to(PLAYER) >= 2:
                self.owner.move_away(PLAYER)

            # if close enough, attempt to attack player
            elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                monster.creature.attack(PLAYER)

class ai_Shiftingserpent:
    # ai for creatures that flee on sight but fight if cornered

    def take_turn(self):
        shift = random.randint(1, 3)
        monster = self.owner


        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):
            print(shift)

            if shift <= 2:
                # if far from player, keep moving away
                if monster.distance_to(PLAYER) >= 2:
                    self.owner.move_towards(PLAYER)

                # if close enough, attempt to attack player
                elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                    monster.creature.attack(PLAYER)

            else:
                game_message("The serpent teleports!", Constants.COLOR_YELLOW)
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))


class ai_Fleetp:
    def take_turn(self):
        monster = self.owner

        if tcod.map_is_in_fov(FOV_MAP, monster.x, monster.y):
            # if far from player, keep moving away
            if monster.distance_to(PLAYER) >= 2:
                self.owner.move_away(PLAYER)

            # if close enough, attempt to attack player
            elif PLAYER.creature and PLAYER.creature.current_hp > 0:
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))
                self.owner.creature.move(random.randint(-1, 1), random.randint(-1, 1))


#  ____  _____    _  _____ _   _
# |  _ \| ____|  / \|_   _| | | |
# | | | |  _|   / _ \ | | | |_| |
# | |_| | |___ / ___ \| | |  _  |
# |____/|_____/_/   \_\_| |_| |_|

def death_monster(monster):
    # on death most enemies stop moving

    # plays message on death
    game_message((monster.creature.name_instance + " dies!"), Constants.COLOR_RED)

    # checks to see if the dying creature is a player, in which case calls the death player function
    if monster.creature.death_function == death_player:
        death_player(PLAYER)

    # if the dying creature is a monster, plays the rest of this function
    if monster.creature.death_function == death_monster:
        dropchance = random.randint(1, 100) + ((monster.creature.level)*10)
        # sets the animation_key to the monsters corpse image
        monster.animation_key = str(monster.item.corpse)
        # sets the animation to the monsters new animation key
        monster.animation = ASSETS.animation_dict[monster.animation_key]
        # makes the tile the monster is standing on passable, fix for monsters not being able to see past corpses
        tcod.map_set_properties(FOV_MAP, monster.x, monster.y,
                                not GAME.current_map[monster.x][monster.y].block_path, True)

        # whenever a monster dies the player gets some experience
        monster.creature.get_xp(monster.creature.xp_reward, PLAYER.creature)
        ##
        if 80 < dropchance:
            if (len(GAME.maps_previous)+1) <= 3:
                gen_item_tier_1((monster.x, monster.y))
            elif (len(GAME.maps_previous)+1) > 3:
                gen_item_tier_2((monster.x, monster.y))
        # sets the creature component for the monster to none
        monster.creature = None
        # sets the ai component for the monster to none
        monster.ai = None


def death_player(player):
    # sets the player state to dead
    player.state = "STATUS_DEAD"

    # fills the screen with black
    SURFACE_MAIN.fill(Constants.COLOR_BLACK)

    # assigns the values for center of screen
    screen_center = (Constants.CAMERA_WIDTH / 2, Constants.CAMERA_HEIGHT / 2)

    # draws text on the center of the new death screen
    draw_text(SURFACE_MAIN,
              "YOU DIED!",
              Constants.FONT_TITLE_SCREEN,
              screen_center,
              Constants.COLOR_WHITE, center=True)

    # updates the display
    pygame.display.update()

    # assigns filename the values for where to store legacy files
    #filename = ("data\legacy\legacy_" +
                #PLAYER.creature.name_instance + "." +
                #datetime.date.today().strftime("%Y%B%d") +
                #".txt")


    # checks if file and savegames exist in the target location
    #file_exists = os.path.isfile(filename)
    save_exists = os.path.isfile("data\savedata")

    # if they do, delete them
    #if file_exists: os.remove(filename)
    if save_exists: os.remove("data\savedata")

    # writes a new legacy file
    #legacy_file = open(filename, 'a+')

    #legacy_file.write("******THIS CHARACTER LOST!******" + "\n")

    # writes out every message ever printed in the game into the legacy file
    #for message, color in GAME.message_history:
        #legacy_file.write(message + "\n")

    # waits for 2 seconds before kicking player back to main menu
    pygame.time.wait(2000)


#  __  __    _    ____
# |  \/  |  / \  |  _ \
# | |\/| | / _ \ | |_) |
# | |  | |/ ___ \|  __/
# |_|  |_/_/   \_\_|

def map_create():
    new_map = [[struc_Tile(True) for y in range(0, int(Constants.MAP_HEIGHT))] for x in
               range(0, int(Constants.MAP_WIDTH))]

    # generate new room
    list_of_rooms = []
    for i in range(int(Constants.MAP_MAX_NUM_ROOMS)):

        w = random.randint(Constants.ROOM_MIN_WIDTH, Constants.ROOM_MAX_WIDTH)
        h = random.randint(Constants.ROOM_MIN_HEIGHT, Constants.ROOM_MAX_HEIGHT)

        x = random.randint(2, Constants.MAP_WIDTH - w - 2)
        y = random.randint(2, Constants.MAP_HEIGHT - h - 2)

        # create the room
        new_room = obj_Room((int(x), int(y)), (int(w), int(h)))

        failed = False

        # check for interference
        for other_room in list_of_rooms:
            if new_room.intersect(other_room):
                failed = True
                break

        if not failed:
            # place room
            map_create_room(new_map, new_room)

            current_center = new_room.center

            if len(list_of_rooms) != 0:
                previous_center = list_of_rooms[-1].center
                # digs the tunnels
                map_create_tunnels(current_center, previous_center, new_map)

            list_of_rooms.append(new_room)

    # CREATES FOVMAP
    map_make_fov(new_map)

    # RETURNS COMPLETED MAP
    return (new_map, list_of_rooms)


def map_place_objects(room_list):
    current_level = len(GAME.maps_previous) + 1
    enemies_to_place = (int(len(room_list) / 2) + (len(GAME.maps_previous) * 2))
    boss_to_place = 1
    items_to_place = (int(len(room_list) / 4)) + (int(len(GAME.maps_previous) / 4))
    top_level = (current_level == 1)
    final_level = (current_level == Constants.MAP_MAX_LEVELS)

    for room in room_list:

        first_room = (room == room_list[0])
        last_room = (room == room_list[-1])

        if first_room: PLAYER.x, PLAYER.y = room.center

        if first_room and top_level:
            gen_portal(room.center)

        if first_room and not top_level:
            gen_stairs((PLAYER.x, PLAYER.y), downwards=False)

        if last_room:
            if final_level:
                gen_core(room.center)
            else:
                gen_stairs(room.center)

        if enemies_to_place != 0 and not first_room:
            if current_level <= 4:
                    enemy_amount = random.randint(0, 100)
                    if enemy_amount > 0:
                        if enemy_amount <= 70:
                            x = random.randint(room.x1 + 1, room.x2 - 1)
                            y = random.randint(room.y1 + 1, room.y2 - 1)
                            gen_enemy_tier_1((x, y))
                            enemies_to_place -= 1
                        if 70 < enemy_amount <= 90:
                            x = random.randint(room.x1 + 1, room.x2 - 1)
                            y = random.randint(room.y1 + 1, room.y2 - 1)
                            gen_enemy_tier_1((x, y))
                            x = random.randint(room.x1 + 1, room.x2 - 1)
                            y = random.randint(room.y1 + 1, room.y2 - 1)
                            gen_enemy_tier_1((x, y))
                            enemies_to_place -= 1
                        if enemy_amount > 90 and not top_level:
                            x = random.randint(room.x1 + 1, room.x2 - 1)
                            y = random.randint(room.y1 + 1, room.y2 - 1)
                            gen_enemy_tier_1((x, y))
                            x = random.randint(room.x1 + 1, room.x2 - 1)
                            y = random.randint(room.y1 + 1, room.y2 - 1)
                            gen_enemy_tier_1((x, y))
                            x = random.randint(room.x1 + 1, room.x2 - 1)
                            y = random.randint(room.y1 + 1, room.y2 - 1)
                            gen_enemy_tier_1((x, y))
                            enemies_to_place -= 1
                        if enemy_amount > 90 and top_level:
                            x = random.randint(room.x1 + 1, room.x2 - 1)
                            y = random.randint(room.y1 + 1, room.y2 - 1)
                            gen_enemy_tier_1((x, y))
            elif 3 < current_level <= 8:
                enemy_amount = random.randint(0, 100)
                if enemy_amount > 0:
                    if enemy_amount <= 70:
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_enemy_tier_2((x, y))
                        enemies_to_place -= 1
                    if 70 < enemy_amount <= 90:
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_enemy_tier_2((x, y))
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_enemy_tier_2((x, y))
                        enemies_to_place -= 1
                    if enemy_amount > 90 and not top_level:
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_enemy_tier_2((x, y))
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_enemy_tier_2((x, y))
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_enemy_tier_2((x, y))
                        enemies_to_place -= 1


        if boss_to_place != 0 and last_room:
            if current_level == 4:
                gen_boss_tier_1(room.center)
                boss_to_place -= 1
            elif current_level == 8:
                gen_boss_tier_2(room.center)

        if items_to_place != 0:
            if current_level <= 4:
                item_amount = random.randint(0, 100)
                if item_amount > 0:
                    if item_amount <= 90:
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_item_tier_1((x, y))
                        items_to_place -= 1
                    if item_amount > 90:
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_item_tier_1((x, y))
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_item_tier_1((x, y))
                        items_to_place -= 1
            elif current_level <= 8:
                item_amount = random.randint(0, 100)
                if item_amount > 0:
                    if item_amount <= 90:
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_item_tier_2((x, y))
                        items_to_place -= 1
                    if item_amount > 90:
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_item_tier_2((x, y))
                        x = random.randint(room.x1 + 1, room.x2 - 1)
                        y = random.randint(room.y1 + 1, room.y2 - 1)
                        gen_item_tier_2((x, y))
                        items_to_place -= 1


def map_create_room(new_map, new_room):
    for x in range(new_room.x1, new_room.x2):
        for y in range(new_room.y1, new_room.y2):
            new_map[x][y].block_path = False


def map_create_tunnels(coords1, coords2, new_map):
    coin_flip = (random.randint(0, 1) == 1)

    x1, y1 = coords1
    x2, y2 = coords2

    if coin_flip:
        for x in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
            new_map[x][y1].block_path = False
        for y in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
            new_map[x2][y].block_path = False
    else:
        for y in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
            new_map[x1][y].block_path = False
        for x in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
            new_map[x][y2].block_path = False


def map_check_for_creatures(x, y, exclude_object=None):
    target = None

    # FINDS CREATURE AT LOCATION EXCEPT EXCLUDE_OBJECT
    if exclude_object:
        for object in GAME.current_objects:
            if (object is not exclude_object and
                    object.x == x and
                    object.y == y and
                    object.creature):
                target = object

            if target:
                return target

    # FINDS ANY CREATURE AT LOCATION
    else:
        for object in GAME.current_objects:
            if (object is not exclude_object and
                    object.x == x and
                    object.y == y and
                    object.creature):
                target = object

            if target:
                return target


def map_check_for_items(x, y, exclude_object=None):
    target = None

    # FINDS ITEM AT LOCATION EXCEPT EXCLUDE_OBJECT
    if exclude_object:
        for object in GAME.current_objects:
            if (object is not exclude_object and
                    object.x == x and
                    object.y == y and
                    object.item):
                target = object

            if target:
                return target

    # FINDS ANY ITEM AT LOCATION
    else:
        for object in GAME.current_objects:
            if (object is not exclude_object and
                    object.x == x and
                    object.y == y and
                    object.item):
                target = object

            if target:
                return target


def map_make_fov(incoming_map):
    global FOV_MAP

    FOV_MAP = tcod.map_new(Constants.MAP_WIDTH, Constants.MAP_HEIGHT)

    for y in range(Constants.MAP_HEIGHT):
        for x in range(Constants.MAP_WIDTH):
            tcod.map_set_properties(FOV_MAP, int(x), int(y),
                                    not incoming_map[x][y].block_path, not incoming_map[x][y].block_path)


def map_calculate_fov():
    global FOV_CALCULATE

    if FOV_CALCULATE:
        FOV_CALCULATE = False

        tcod.map_compute_fov(FOV_MAP, PLAYER.x, PLAYER.y, Constants.TORCH_RADIUS, Constants.FOV_LIGHTWALLS,
                             Constants.FOV_ALGO)


def map_object_at_coords(coords_x, coords_y):
    object_options = [obj for obj in GAME.current_objects if obj.x == coords_x and obj.y == coords_y]

    return object_options


def map_find_line(coords1, coords2):
    '''
    Converts two x,y coords into list of tiles between them

    :param coords1: x,y coords from first point in the line
    :param coords2: x,y coords from second point in the line
    :return: returns a list of all tiles between the two points
    '''

    x1, y1 = coords1

    x2, y2 = coords2

    tcod.line_init(x1, y1, x2, y2)

    calc_x, calc_y = tcod.line_step()

    coord_list = []

    if x1 == x2 and y1 == y2:
        return [(x1, y1)]

    while not calc_x is None:
        coord_list.append((calc_x, calc_y))

        calc_x, calc_y = tcod.line_step()

    return coord_list


def map_find_radius(coords, radius):
    center_x, center_y = coords

    tile_list = []
    start_x = (center_x - radius)
    end_x = center_x + radius + 1

    start_y = (center_y - radius)
    end_y = center_y + radius + 1

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            tile_list.append((x, y))

    return tile_list


#  ____  ____      ___        _____ _   _  ____
# |  _ \|  _ \    / \ \      / /_ _| \ | |/ ___|
# | | | | |_) |  / _ \ \ /\ / / | ||  \| | |  _
# | |_| |  _ <  / ___ \ V  V /  | || |\  | |_| |
# |____/|_| \_\/_/   \_\_/\_/  |___|_| \_|\____|

def draw_game():
    global SURFACE_MAIN, PLAYER

    # CLEAR SURFACE
    SURFACE_MAIN.fill(Constants.COLOR_DEFAULT_BG)
    SURFACE_MAP.fill(Constants.COLOR_DEFAULT_BG)

    CAMERA.update()

    # DRAW MAP
    draw_map(GAME.current_map)

    # DRAW CHARACTER
    for obj in sorted(GAME.current_objects, key=lambda obj: obj.depth, reverse=True):
        obj.draw()

    if PLAYER.state == None:
        for obj in GAME.current_objects:
            if obj.creature:
                obj.draw_health_rect()

    SURFACE_MAIN.blit(SURFACE_MAP, (0, 0), CAMERA.rectangle)

    draw_messages()

    # UPDATE DISPLAY


def draw_map(map_to_draw):
    cam_x, cam_y = CAMERA.map_address

    display_map_w = int(Constants.CAMERA_WIDTH / Constants.CELL_WIDTH)
    display_map_h = int(Constants.CAMERA_HEIGHT / Constants.CELL_HEIGHT)

    render_w_min = int(cam_x - (display_map_w / 2))
    render_h_min = int(cam_y - (display_map_h / 2))
    render_w_max = int(cam_x + (display_map_w / 2))
    render_h_max = int(cam_y + (display_map_h / 2))

    if render_w_min < 0: render_w_min = 0
    if render_h_min < 0: render_h_min = 0

    if render_w_max > Constants.MAP_WIDTH: render_w_max = Constants.MAP_WIDTH
    if render_h_max > Constants.MAP_HEIGHT: render_h_max = Constants.MAP_HEIGHT

    for x in range(render_w_min, render_w_max):
        for y in range(render_h_min, render_h_max):

            is_visible = tcod.map_is_in_fov(FOV_MAP, x, y)

            if is_visible:

                map_to_draw[x][y].explored = True

                if map_to_draw[x][y].block_path == True:
                    # draw wall
                    SURFACE_MAP.blit(ASSETS.S_WALL, (x * Constants.CELL_WIDTH, y * Constants.CELL_HEIGHT))
                else:
                    # draw floor
                    SURFACE_MAP.blit(ASSETS.S_FLOOR, (x * Constants.CELL_WIDTH, y * Constants.CELL_HEIGHT))

            elif map_to_draw[x][y].explored:

                if map_to_draw[x][y].block_path == True:
                    # draw wall
                    SURFACE_MAP.blit(ASSETS.S_WALL_EX, (x * Constants.CELL_WIDTH, y * Constants.CELL_HEIGHT))
                else:
                    # draw floor
                    SURFACE_MAP.blit(ASSETS.S_FLOOR_EX, (x * Constants.CELL_WIDTH, y * Constants.CELL_HEIGHT))


# def draw_debug():
#    draw_text(SURFACE_MAIN,
#              "fps: " + str(int(CLOCK.get_fps())),
#              Constants.FONT_DEBUG_MESSAGE,
#              (0, 0),
#              Constants.COLOR_WHITE,
#              Constants.COLOR_BLACK)


def draw_messages():
    if len(GAME.message_history) <= Constants.NUM_MESSAGES:
        to_draw = GAME.message_history
    else:
        to_draw = GAME.message_history[-Constants.NUM_MESSAGES:]

    text_height = helper_text_height(Constants.FONT_MESSAGE_TEXT)

    start_y = (Constants.CAMERA_HEIGHT - Constants.NUM_MESSAGES * text_height)

    i = 0

    for message, color in to_draw:
        draw_text(SURFACE_MAIN,
                  message,
                  Constants.FONT_MESSAGE_TEXT,
                  (0, start_y + (i * text_height)),
                  color, Constants.COLOR_BLACK)

        i += 1


def draw_text(display_surface, text_to_display, font,
              coords, text_color, back_color=None, center=False):
    # get both the surface and rectangle of the desired message
    text_surf, text_rect = helper_text_objects(text_to_display, font, text_color, back_color)

    # adjust the location of the surface based on the coordinates
    if not center:
        text_rect.topleft = coords
    else:
        text_rect.center = coords

    # draw the text onto the display surface.
    display_surface.blit(text_surf, text_rect)


def draw_tile_rect(coords, tile_color=None, tile_alpha=None, mark=None):
    x, y = coords

    if tile_color:
        local_color = tile_color
    else:
        local_color = Constants.COLOR_WHITE

    if tile_alpha:
        local_alpha = tile_alpha
    else:
        local_alpha = 200

    new_x = x * Constants.CELL_WIDTH
    new_y = y * Constants.CELL_HEIGHT

    new_surface = pygame.Surface((Constants.CELL_WIDTH, Constants.CELL_HEIGHT))

    new_surface.fill(local_color)

    new_surface.set_alpha(local_alpha)
    if mark:
        draw_text(new_surface, mark, font=Constants.FONT_CURSOR_TEXT,
                  coords=(Constants.CELL_WIDTH / 2, Constants.CELL_HEIGHT / 2), text_color=Constants.COLOR_BLACK,
                  center=True)

    SURFACE_MAP.blit(new_surface, (new_x, new_y))


#  _   _ _____ _     ____  _____ ____  ____
# | | | | ____| |   |  _ \| ____|  _ \/ ___|
# | |_| |  _| | |   | |_) |  _| | |_) \___ \
# |  _  | |___| |___|  __/| |___|  _ < ___) |
# |_| |_|_____|_____|_|   |_____|_| \_\____/

def helper_text_objects(incoming_text, incoming_font, incoming_color, incoming_bg):
    # if there is a background color, render with that.
    if incoming_bg:
        Text_surface = incoming_font.render(incoming_text,
                                            False,
                                            incoming_color,
                                            incoming_bg)

    else:  # otherwise, render without a background.
        Text_surface = incoming_font.render(incoming_text,
                                            False,
                                            incoming_color)

    return Text_surface, Text_surface.get_rect()


def helper_text_height(font):
    font_object = font.render('a', False, (0, 0, 0))
    font_rect = font_object.get_rect()

    return font_rect.height


#   __  __    _    ____ ___ ____
# |  \/  |  / \  / ___|_ _/ ___|
# | |\/| | / _ \| |  _ | | |
# | |  | |/ ___ \ |_| || | |___
# |_|  |_/_/   \_\____|___\____|

def cast_heal(caster, amount):
    this_amount = amount + int(caster.creature.wisdom/5)

    if caster.creature.current_hp == caster.creature.max_hp:
        game_message(caster.creature.name_instance + " the " + caster.name_object +
                     " is already at full health!")
        return "canceled"
    else:
        caster.creature.heal(this_amount)
        game_message(caster.creature.name_instance + " the " + caster.name_object +
                     " healed for " + str(this_amount) + " health!")

    return None

def consume_this(caster, amount):
    this_amount = amount + int(caster.creature.wisdom / 5)

    if caster.creature.current_hp == caster.creature.max_hp:
        game_message(caster.creature.name_instance + " the " + caster.name_object +
                     " is already at full health!")
        return "canceled"
    else:
        caster.creature.heal(this_amount)
        game_message("you eat the item for " + str(this_amount) + " hitpoints!")

    return None

def cast_spwizardmagic(caster, damage):
    rangemax = 3 + (int(caster.creature.intelligence/5))
    dam = damage + int(caster.creature.intelligence/5)

    player_location = (caster.x, caster.y)

    # prompt for tile
    point_selected = menu_tile_select(coord_origin=player_location, max_range=rangemax, penetrate_walls=False, penetrate_creature=False)
    if point_selected:
        # convert tile into list of tiles a -> b
        list_of_tiles = map_find_line(player_location, point_selected)

        # damage everything in line

        for i, (x, y) in enumerate(list_of_tiles):

            target = map_check_for_creatures(x, y)

            if target:
                target.move_away(PLAYER)
                target.move_away(PLAYER)
                target.creature.take_damage(dam)

def get_drop(caster, tier):
    coords = caster.x, caster.y

    if tier == 1:
        gen_item_tier_1(coords)

    if tier == 2:
        gen_item_tier_2(coords)

    if tier == 31:
        drop_what = random.randint(1, 2)
        if drop_what == 1:
            boss_new_item = gen_weapon_serpentwhip(coords)
            GAME.current_objects.append(boss_new_item)
        elif drop_what == 2:
            boss_new_item = gen_accessory_serpenthead(coords)
            GAME.current_objects.append(boss_new_item)

    if tier == 32:
        drop_what = random.randint(1, 2)
        if drop_what == 1:
            boss_new_item = gen_armor_chogguskingmantle(coords)
            GAME.current_objects.append(boss_new_item)
        elif drop_what == 2:
            boss_new_item = gen_accessory_chogguskingcrown(coords)
            GAME.current_objects.append(boss_new_item)

    if tier == 33:
        drop_what = random.randint(1, 2)
        if drop_what == 1:
            boss_new_item = gen_item_spwizardstaff(coords)
            GAME.current_objects.append(boss_new_item)
        elif drop_what == 2:
            boss_new_item = gen_accessory_spwizardhat(coords)
            GAME.current_objects.append(boss_new_item)

    if tier == 61:
        boss_new_item = gen_helmet_usmskull(coords)
        GAME.current_objects.append(boss_new_item)

def deploy_device_laser_blaster(caster, damage):
    damage = damage + int(caster.creature.intelligence / 5)

    player_location = (caster.x, caster.y)

    # prompt for tile
    point_selected = menu_tile_select(coord_origin=player_location, max_range=5, penetrate_walls=False)
    if point_selected:
        # convert tile into list of tiles a -> b
        list_of_tiles = map_find_line(player_location, point_selected)

        # damage everything in line

        for i, (x, y) in enumerate(list_of_tiles):

            target = map_check_for_creatures(x, y)

            if target:
                target.creature.take_damage(damage)
                game_message("A flash of heat flies across the room, dealing " + str(damage) +
                             " points of damage!", Constants.COLOR_RED)

def deploy_device_pluralis_blaster(caster, damage):
    damage = damage + int(caster.creature.intelligence / 5)

    player_location = (caster.x, caster.y)

    # prompt for tile
    point_selected = menu_tile_select(coord_origin=player_location, max_range=9, penetrate_walls=False,
                                      penetrate_creature=False)
    if point_selected:
        # convert tile into list of tiles a -> b
        list_of_tiles = map_find_line(player_location, point_selected)

        # damage everything in line

        for i, (x, y) in enumerate(list_of_tiles):

            target = map_check_for_creatures(x, y)

            if target:
                target.creature.take_damage(damage)
                game_message("A neon yellow blast of energy flies across the room, dealing " + str(damage) +
                             " points of damage!", Constants.COLOR_RED)

def deploy_device_implosiongrenade(caster, damage):
    damage = damage + int(caster.creature.intelligence / 5)

    player_location = (caster.x, caster.y)

    # prompt for tile
    point_selected = menu_tile_select(coord_origin=player_location, max_range=5, penetrate_walls=False)
    if point_selected:
        # convert tile into list of tiles a -> b
        list_of_tiles = map_find_line(player_location, point_selected)

        # damage everything in line

        for i, (x, y) in enumerate(list_of_tiles):

            target = map_check_for_creatures(x, y)

            if target:
                target.creature.take_damage(damage)
                game_message("The grenade explodes in a restrained manner, dealing " + str(damage) +
                             " points of damage!", Constants.COLOR_RED)

def deploy_device_firegrenade(caster, damage):
    # defs
    damage = damage + int(caster.creature.intelligence / 5)
    this_radius = 1
    max_r = 5

    player_location = (caster.x, caster.y)

    # get target tile
    point_selected = menu_tile_select(coord_origin=player_location,
                                      max_range=max_r,
                                      radius=this_radius,
                                      penetrate_walls=False,
                                      penetrate_creature=False)
    if point_selected:
        # get sequence of tiles
        tiles_to_damage = map_find_radius(point_selected, this_radius)

        creature_hit = False

        # damage all creatures in aoe
        for (x, y) in tiles_to_damage:
            creature_to_damage = map_check_for_creatures(x, y)

            if creature_to_damage:
                creature_to_damage.creature.take_damage(damage)

                if creature_to_damage is not PLAYER:
                    creature_hit = True

        if creature_hit:
            game_message("Heat and shrapnel fill the area dealing " + str(damage) + " points of damage!",
                         Constants.COLOR_RED)

def deploy_device_pluralisgrenade(caster, damage):
    # defs
    damage = damage + int(caster.creature.intelligence / 5)
    this_radius = 1
    max_r = 5

    player_location = (caster.x, caster.y)

    # get target tile
    point_selected = menu_tile_select(coord_origin=player_location,
                                      max_range=max_r,
                                      radius=this_radius,
                                      penetrate_walls=False,
                                      penetrate_creature=False)
    if point_selected:
        # get sequence of tiles
        tiles_to_damage = map_find_radius(point_selected, this_radius)

        creature_hit = False

        # damage all creatures in aoe
        for (x, y) in tiles_to_damage:
            creature_to_damage = map_check_for_creatures(x, y)

            if creature_to_damage:
                creature_to_damage.creature.take_damage(damage)

                if creature_to_damage is not PLAYER:
                    creature_hit = True

        if creature_hit:
            game_message("The bomb boomerangs across the room dealing " + str(damage) + " points of damage!",
                         Constants.COLOR_RED)

def deploy_device_immensiumgrenade(caster, damage):
    # defs
    damage = damage + int(caster.creature.intelligence / 5)
    this_radius = 2
    max_r = 5

    player_location = (caster.x, caster.y)

    # get target tile
    point_selected = menu_tile_select(coord_origin=player_location,
                                      max_range=max_r,
                                      radius=this_radius,
                                      penetrate_walls=False,)
    if point_selected:
        # get sequence of tiles
        tiles_to_damage = map_find_radius(point_selected, this_radius)

        creature_hit = False

        # damage all creatures in aoe
        for (x, y) in tiles_to_damage:
            creature_to_damage = map_check_for_creatures(x, y)

            if creature_to_damage:
                creature_to_damage.creature.take_damage(damage)

                if creature_to_damage is not PLAYER:
                    creature_hit = True

        if creature_hit:
            game_message("A huge blast of light and electricity fills the room dealing " + str(damage) + " points of damage!",
                         Constants.COLOR_RED)

def deploy_device_brain_scrambler(caster, num_turns):
    # defs
    max_r = 6
    player_location = (caster.x, caster.y)
    num_turns = num_turns + int(caster.creature.intelligence / 10)

    #   select tile

    #   get target from tile
    point_selected = menu_tile_select(coord_origin=player_location,
                                      max_range=max_r,
                                      penetrate_walls=False, )

    if point_selected:
        tile_x, tile_y = point_selected
        target = map_check_for_creatures(tile_x, tile_y)

        #   temporarily confuse target
        if target:
            this_old_ai = target.ai
            target.ai = ai_Confuse(old_ai=this_old_ai, num_turns=num_turns)
            target.ai.owner = target

            game_message(target.display_name + "'s eyes glaze over", Constants.COLOR_PURPLE)

def deploy_serum_attribooster(caster, increase):
    increase = int(increase + (caster.creature.wisdom / 10))
    stat_to_increase = random.randint(1, 4)

    if stat_to_increase == 1:
        caster.creature.base_int += increase
        game_message("your intelligence went up!", Constants.COLOR_PURPLE)
    elif stat_to_increase == 2:
        caster.creature.base_dex += increase
        game_message("your dexterity went up!", Constants.COLOR_PURPLE)
    elif stat_to_increase == 3:
        caster.creature.base_str += increase
        game_message("your strength went up!", Constants.COLOR_PURPLE)
    elif stat_to_increase == 4:
        caster.creature.base_wis += increase
        game_message("your wisdom went up!", Constants.COLOR_PURPLE)

def deploy_serum_attriswapper(caster, increase):
    increase = int(increase + (caster.creature.wisdom / 10))
    decrease = int(increase/2)
    stat_to_increase = random.randint(1, 4)

    if stat_to_increase == 1:
        caster.creature.base_int += increase
        caster.creature.base_str -= decrease
        game_message("your intelligence went up, but your strength went down", Constants.COLOR_PURPLE)
    elif stat_to_increase == 2:
        caster.creature.base_dex += increase
        caster.creature.base_wis -= decrease
        game_message("your dexterity went up, but your wisdom went down", Constants.COLOR_PURPLE)
    elif stat_to_increase == 3:
        caster.creature.base_str += increase
        caster.creature.base_int -= decrease
        game_message("your strength went up, but your intelligence went down", Constants.COLOR_PURPLE)
    elif stat_to_increase == 4:
        caster.creature.base_wis += increase
        caster.creature.base_dex -= decrease
        game_message("your wisdom went up, but your dexterity went down", Constants.COLOR_PURPLE)

def deploy_serum_performance_enhancer(caster, increase):
    damage = int(5 * (len(GAME.maps_previous) + 1)) - (int(caster.creature.wisdom/5))
    increase = int(increase + (caster.creature.wisdom / 5))
    stat_to_increase = random.randint(1, 4)

    if caster.creature.max_hp <= damage:
        game_message("poking yourself with this right now would kill you!", Constants.COLOR_RED)
    else:
        if stat_to_increase == 1:
            caster.creature.base_int += increase
            caster.creature.max_hp -= damage
            game_message("your intelligence went up!", Constants.COLOR_PURPLE)
        elif stat_to_increase == 2:
            caster.creature.base_dex += increase
            caster.creature.max_hp -= damage
            game_message("your dexterity went up!", Constants.COLOR_PURPLE)
        elif stat_to_increase == 3:
            caster.creature.base_str += increase
            caster.creature.max_hp -= damage
            game_message("your strength went up!", Constants.COLOR_PURPLE)
        elif stat_to_increase == 4:
            caster.creature.base_wis += increase
            caster.creature.max_hp -= damage
            game_message("your wisdom went up!", Constants.COLOR_PURPLE)

def deploy_serum_autotransfuser(caster, healing):
    this_healing = healing + int(caster.creature.wisdom/5)
    stat_dmg = int(2 + (len(GAME.maps_previous)/2))

    stat_to_reduce = random.randint(1, 4)

    if stat_to_reduce == 1:
        caster.creature.base_int -= stat_dmg
        caster.creature.current_hp += this_healing
        game_message("your intelligence goes down!", Constants.COLOR_PURPLE)
    elif stat_to_reduce == 2:
        caster.creature.base_str -= stat_dmg
        caster.creature.current_hp += this_healing
        game_message("your strength goes down!", Constants.COLOR_PURPLE)
    elif stat_to_reduce == 3:
        caster.creature.base_dex -= stat_dmg
        caster.creature.current_hp += this_healing
        game_message("your dexterity goes down!", Constants.COLOR_PURPLE)
    elif stat_to_reduce == 4:
        caster.creature.base_wis -= stat_dmg
        caster.creature.current_hp += this_healing
        game_message("your wisdom goes down!", Constants.COLOR_PURPLE)

def deploy_serum_booster2(caster, type):
    increase = int(2 + (caster.creature.wisdom / 10))
    decrease = int(increase / 2)
    stat_to_increase = type

    if stat_to_increase == 1:
        caster.creature.base_int += increase
        caster.creature.base_str -= decrease
        caster.creature.base_dex -= decrease
        game_message("your intelligence went up, but your strength and dexterity went down", Constants.COLOR_PURPLE)
    elif stat_to_increase == 2:
        caster.creature.base_dex += increase
        caster.creature.base_wis -= decrease
        caster.creature.base_int -= decrease
        game_message("your dexterity went up, but your wisdom and intelligence went down", Constants.COLOR_PURPLE)
    elif stat_to_increase == 3:
        caster.creature.base_str += increase
        caster.creature.base_int -= decrease
        caster.creature.base_wis -= decrease
        game_message("your strength went up, but your intelligence and wisdom went down", Constants.COLOR_PURPLE)
    elif stat_to_increase == 4:
        caster.creature.base_wis += increase
        caster.creature.base_dex -= decrease
        caster.creature.base_str -= decrease
        game_message("your wisdom went up, but your dexterity and strength went down", Constants.COLOR_PURPLE)

#  _   _ ___
# | | | |_ _|
# | | | || |
# | |_| || |
#  \___/|___|

class ui_Button:

    def __init__(self, surface, button_text, size, center_coords,
                 color_box_mouseover=Constants.COLOR_RED,
                 color_box_default=Constants.COLOR_GREEN,
                 color_text_mouseover=Constants.COLOR_GREY,
                 color_text_default=Constants.COLOR_GREY):

        ## C_BOX_MO MEANS COLOR BOX MOUSEOVER, FOR THE COLOR OF THE BOX WHEN MOUSING OVER, NAMING SCHEME FOR EVERYTHING
        ## ELSE FOLLOWS
        self.surface = surface
        self.button_text = button_text
        self.size = size
        self.center_coords = center_coords

        self.c_box_mo = color_box_mouseover
        self.c_box_default = color_box_default
        self.c_text_mo = color_text_mouseover
        self.c_text_default = color_text_default
        self.c_c_box = color_box_default
        self.c_c_text = color_text_default

        self.rect = pygame.Rect((0, 0), size)
        self.rect.center = center_coords

    def update(self, player_input):

        mouse_clicked = False

        this_events, this_mousepos = player_input

        mouse_x, mouse_y = this_mousepos

        mouse_over = (self.rect.left <= mouse_x <= self.rect.right and
                      self.rect.top <= mouse_y <= self.rect.bottom)

        for event in this_events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_clicked = True

        if mouse_over and mouse_clicked:
            return True

        if mouse_over:
            self.c_c_box = self.c_box_mo
            self.c_c_text = self.c_text_mo
        else:
            self.c_c_box = self.c_box_default
            self.c_c_text = self.c_text_default

    def draw(self):

        pygame.draw.rect(self.surface, self.c_c_box, self.rect)
        draw_text(self.surface,
                  self.button_text,
                  Constants.FONT_DEBUG_MESSAGE,
                  self.center_coords,
                  self.c_c_text,
                  center=True)

class ui_Slider:

    def __init__(self, surface, size, center_coords, bg_color, fg_color, parameter_value):
        self.surface = surface
        self.size = size
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.current_val = parameter_value

        self.bg_rect = pygame.Rect((0, 0), size)
        self.bg_rect.center = center_coords
        self.fg_rect = pygame.Rect((0, 0),
                                   (self.bg_rect.w * self.current_val, self.bg_rect.h))
        self.fg_rect.topleft = self.bg_rect.topleft

        self.grip_tab = pygame.Rect((0, 0), (20, self.bg_rect.h + 4))
        self.grip_tab.center = (self.fg_rect.right, self.bg_rect.centery)

    def update(self, player_input):
        mouse_down = pygame.mouse.get_pressed()[0]

        local_events, local_mousepos = player_input
        mouse_x, mouse_y = local_mousepos

        mouse_over = (self.bg_rect.left <= mouse_x <= self.bg_rect.right
                      and self.bg_rect.top <= mouse_y <= self.bg_rect.bottom)

        if mouse_down and mouse_over:
            self.current_val = (float(mouse_x) - float(self.bg_rect.left)) / self.bg_rect.w

            self.fg_rect.width = self.bg_rect.width * self.current_val

            self.grip_tab.center = (self.fg_rect.right, self.bg_rect.centery)

    def draw(self):
        # draw background rectangle
        pygame.draw.rect(self.surface, self.bg_color, self.bg_rect)

        # draw foreground rectangle
        pygame.draw.rect(self.surface, self.fg_color, self.fg_rect)

        # draw slider tab
        pygame.draw.rect(self.surface, Constants.COLOR_BLACK, self.grip_tab)


#  __  __ _____ _   _ _   _ ____
# |  \/  | ____| \ | | | | / ___|
# | |\/| |  _| |  \| | | | \___ \
# | |  | | |___| |\  | |_| |___) |
# |_|  |_|_____|_| \_|\___/|____/

def menu_main():
    game_initialize()


    button_offset = 40
    title_x = int(Constants.CAMERA_WIDTH / 2)
    title_y = int((Constants.CAMERA_HEIGHT / 2) - 70)
    title_text = "Epic globintime video and game"

    continue_button_y = title_y + button_offset
    new_game_button_y = continue_button_y + button_offset
    options_button_y = new_game_button_y + button_offset
    quit_button_y = options_button_y + button_offset

    menu_running = True

    pygame.mixer.music.load(ASSETS.music_menu)
    pygame.mixer.music.play(-1)

    continue_game_button = ui_Button(SURFACE_MAIN, "Continue Game", (300, 30), (title_x, continue_button_y))
    new_game_button = ui_Button(SURFACE_MAIN, "New Game", (300, 30), (title_x, new_game_button_y))
    options_button = ui_Button(SURFACE_MAIN, "Options", (300, 30), (title_x, options_button_y))
    quit_button = ui_Button(SURFACE_MAIN, "Quit", (300, 30), (title_x, quit_button_y))

    while menu_running:

        list_of_events = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()

        game_input = (list_of_events, mouse_position)

        # GET INPUT
        for event in list_of_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if continue_game_button.update(game_input):
            # tries to load game, if problem just make a new one
            try:
                game_load()
            except:
                game_new()

            game_main_loop()
            game_initialize()

        if new_game_button.update(game_input):
            # starts a new game
            menu_name()

        if options_button.update(game_input):
            menu_options()

        if quit_button.update(game_input):
            pygame.quit()
            exit()

        # DRAW MENU
        SURFACE_MAIN.fill(Constants.COLOR_BLACK)

        draw_text(SURFACE_MAIN, title_text, Constants.FONT_TITLE_SCREEN,
                  (title_x, title_y), Constants.COLOR_GREEN, center=True)

        quit_button.draw()
        options_button.draw()
        new_game_button.draw()
        continue_game_button.draw()

        # UPDATE SURFACE
        pygame.display.update()

def menu_options():
    # MENU VARS #
    settings_menu_width = 200
    settings_menu_height = 200
    settings_menu_bgcolor = Constants.COLOR_GREY

    # SLIDER VARS #
    slider_x = Constants.CAMERA_WIDTH / 2
    sound_effect_slider_y = Constants.CAMERA_HEIGHT / 2 - 60
    sound_effect_vol = .5
    music_effect_slider_y = sound_effect_slider_y + 50

    # TEXT VARS #
    text_y_offset = 20
    sound_text_y = sound_effect_slider_y - text_y_offset
    music_text_y = music_effect_slider_y - text_y_offset

    # BUTTON VARS#
    button_save_y = music_effect_slider_y + 50

    window_center = (Constants.CAMERA_WIDTH / 2, Constants.CAMERA_HEIGHT / 2)

    settings_menu_surface = pygame.Surface((settings_menu_width,
                                            settings_menu_height))

    settings_menu_rect = pygame.Rect(0, 0,
                                     settings_menu_width,
                                     settings_menu_height)

    settings_menu_rect.center = window_center

    menu_close = False

    sound_effect_slider = ui_Slider(SURFACE_MAIN,
                                    (125, 15),
                                    (slider_x, sound_effect_slider_y),
                                    Constants.COLOR_RED,
                                    Constants.COLOR_GREEN,
                                    PREFERENCES.vol_sound)

    music_effect_slider = ui_Slider(SURFACE_MAIN,
                                    (125, 15),
                                    (slider_x, music_effect_slider_y),
                                    Constants.COLOR_RED,
                                    Constants.COLOR_GREEN,
                                    PREFERENCES.vol_music)

    save_button = ui_Button(SURFACE_MAIN,
                            "Save",
                            (100, 30),
                            (slider_x, button_save_y),
                            Constants.COLOR_DARKERGREY,
                            Constants.COLOR_DGREY,
                            Constants.COLOR_BLACK,
                            Constants.COLOR_BLACK)

    while not menu_close:

        list_of_events = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()

        game_input = (list_of_events, mouse_position)

        # handle menu events
        for event in list_of_events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu_close = True

        current_sound_vol = PREFERENCES.vol_sound
        current_music_vol = PREFERENCES.vol_music

        sound_effect_slider.update(game_input)
        music_effect_slider.update(game_input)

        if current_sound_vol is not sound_effect_slider.current_val:
            PREFERENCES.vol_sound = sound_effect_slider.current_val
            ASSETS.volume_adjust()

        if current_music_vol is not music_effect_slider.current_val:
            PREFERENCES.vol_music = music_effect_slider.current_val
            ASSETS.volume_adjust()

        if save_button.update(game_input):
            preferences_save()
            menu_close = True

        # Draw the Menu
        settings_menu_surface.fill(settings_menu_bgcolor)

        SURFACE_MAIN.blit(settings_menu_surface, settings_menu_rect.topleft)

        draw_text(SURFACE_MAIN,
                  "SOUND",
                  Constants.FONT_DEBUG_MESSAGE,
                  (slider_x, sound_text_y),
                  Constants.COLOR_BLACK,
                  center=True)

        draw_text(SURFACE_MAIN,
                  "MUSIC",
                  Constants.FONT_DEBUG_MESSAGE,
                  (slider_x, music_text_y),
                  Constants.COLOR_BLACK,
                  center=True)

        sound_effect_slider.draw()
        music_effect_slider.draw()
        save_button.draw()

        pygame.display.update()

def menu_inventory():
    menu_close = False

    window_width = Constants.CAMERA_WIDTH
    window_height = Constants.CAMERA_HEIGHT

    menu_width = 400
    menu_height = 400
    menu_x = (window_width / 2) - (menu_width / 2)
    menu_y = (window_height / 2) - (menu_height / 2)

    menu_text_font = Constants.FONT_MESSAGE_TEXT
    menu_text_height = helper_text_height(menu_text_font)

    menu_text_color = Constants.COLOR_WHITE

    local_inventory_surface = pygame.Surface((menu_width, menu_height))

    while not menu_close:

        ## CLEAR MENU
        local_inventory_surface.fill(Constants.COLOR_BLACK)

        ## REGISTER CHANGE

        # GETS NAME OF ALL OBJECTS INSIDE PLAYER INVENTORY
        print_list = [obj.display_name for obj in PLAYER.container.inventory]

        # GETS LIST OF ALL INPUT EVENTS
        events_list = pygame.event.get()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        mouse_x_rel = mouse_x - menu_x
        mouse_y_rel = mouse_y - menu_y

        mouse_in_window = (0 < mouse_x_rel < menu_width and
                           0 < mouse_y_rel < menu_height)

        mouse_line_selection = int(mouse_y_rel / menu_text_height)

        for event in events_list:

            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:
                    menu_close = True
                    menu_character()

                if event.key == pygame.K_i:
                    menu_close = True

                if event.key == pygame.K_h:
                    menu_close = True
                    menu_help()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mouse_in_window and mouse_line_selection <= len(print_list) - 1:
                        PLAYER.container.inventory[mouse_line_selection].item.use()
                        for obj in GAME.current_objects:
                            if obj.ai:
                                obj.ai.take_turn()
                        menu_close = True
                if event.button == 3:
                    if mouse_in_window and mouse_line_selection <= len(print_list) - 1:
                        PLAYER.container.inventory[mouse_line_selection].item.drop(PLAYER.x, PLAYER.y)
                        menu_close = True

        ## DRAW LIST
        for line, (name) in enumerate(print_list):

            if line == mouse_line_selection and mouse_in_window:
                draw_text(local_inventory_surface,
                          name,
                          Constants.FONT_MESSAGE_TEXT,
                          (0, 0 + (line * menu_text_height)),
                          menu_text_color, Constants.COLOR_GREY)
            else:
                draw_text(local_inventory_surface,
                          name,
                          Constants.FONT_MESSAGE_TEXT,
                          (0, 0 + (line * menu_text_height)),
                          menu_text_color, Constants.COLOR_BLACK)

        ## RENDER GAME
        draw_game()

        ## DISPLAY MENU
        SURFACE_MAIN.blit(local_inventory_surface, (menu_x, menu_y))

        CLOCK.tick(Constants.GAME_FPS)

        pygame.display.flip()

def menu_tile_select(coord_origin=None, max_range=None, radius=None, penetrate_walls=True, penetrate_creature=True):
    '''
    Select a tile

    This function makes a pseudo menu and pauses the game, then it tracks the mouse and returns a coord, for spells and
    arrows and whatever else
    '''
    menu_close = False

    while not menu_close:
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Get click input
        events_list = pygame.event.get()

        # Mouse map selection

        mapx_pixel, mapy_pixel = CAMERA.win_to_map((mouse_x, mouse_y))

        map_coord_x = int(mapx_pixel / Constants.CELL_WIDTH)
        map_coord_y = int(mapy_pixel / Constants.CELL_HEIGHT)

        valid_tiles = []

        if coord_origin:
            full_list_of_tiles = map_find_line(coord_origin, (map_coord_x, map_coord_y))
            for i, (x, y) in enumerate(full_list_of_tiles):

                valid_tiles.append((x, y))
                # stop at max range
                if max_range and i == max_range - 1:
                    break
                # stop at wall
                if (not penetrate_walls) and GAME.current_map[x][y].block_path:
                    break
                # stop at creature
                if (not penetrate_creature) and map_check_for_creatures(x, y):
                    break
        else:
            valid_tiles = [(map_coord_x, map_coord_y)]

        # return mapcoords when press mouse

        for event in events_list:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    menu_close = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return (valid_tiles[-1])

            # Draw the game
            # CLEAR SURFACE
            SURFACE_MAIN.fill(Constants.COLOR_DEFAULT_BG)
            SURFACE_MAP.fill(Constants.COLOR_DEFAULT_BG)

            CAMERA.update()

            # DRAW MAP
            draw_map(GAME.current_map)

            # DRAW CHARACTER
            for obj in sorted(GAME.current_objects, key=lambda obj: obj.depth, reverse=True):
                obj.draw()

            # Draw rectangle at position
            for (tile_x, tile_y) in valid_tiles:
                if (tile_x, tile_y) == valid_tiles[-1]:
                    draw_tile_rect(coords=(tile_x, tile_y), mark="X")
                else:
                    draw_tile_rect(coords=(tile_x, tile_y))

            if radius:
                area_effect = map_find_radius(valid_tiles[-1], radius)

                for (tile_x, tile_y) in area_effect:
                    draw_tile_rect(coords=(tile_x, tile_y),
                                   tile_color=Constants.COLOR_RED,
                                   tile_alpha=125)

        SURFACE_MAIN.blit(SURFACE_MAP, (0, 0), CAMERA.rectangle)

        draw_messages()

        # updates display
        pygame.display.flip()

        # ticks clock
        CLOCK.tick(Constants.GAME_FPS)

def menu_look():
    '''
    Select a tile

    This function makes a pseudo menu and pauses the game, then it tracks the mouse and returns a coord, for spells and
    arrows and whatever else
    '''
    menu_close = False

    window_width = Constants.CAMERA_WIDTH
    window_height = Constants.CAMERA_HEIGHT

    menu_text_font = Constants.FONT_MESSAGE_TEXT
    menu_text_height = helper_text_height(menu_text_font)

    menu_width = window_width
    menu_height = menu_text_height * 8
    menu_x = window_width - menu_width
    menu_y = 0

    menu_text_color = Constants.COLOR_WHITE

    local_look_surface = pygame.Surface((menu_width, menu_height))

    while not menu_close:
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Get click input
        events_list = pygame.event.get()

        # Mouse map selection

        mapx_pixel, mapy_pixel = CAMERA.win_to_map((mouse_x, mouse_y))

        map_coord_x = int(mapx_pixel / Constants.CELL_WIDTH)
        map_coord_y = int(mapy_pixel / Constants.CELL_HEIGHT)

        valid_tiles = []

        valid_tiles = [(map_coord_x, map_coord_y)]

        # return mapcoords when press mouse

        for event in events_list:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    menu_close = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return (valid_tiles[-1])

            # Draw the game
            # CLEAR SURFACE
            SURFACE_MAIN.fill(Constants.COLOR_DEFAULT_BG)
            SURFACE_MAP.fill(Constants.COLOR_DEFAULT_BG)

            CAMERA.update()

            # DRAW MAP
            draw_map(GAME.current_map)

            # DRAW CHARACTER
            for obj in sorted(GAME.current_objects, key=lambda obj: obj.depth, reverse=True):
                obj.draw()

            # Draw rectangle at position
            for (tile_x, tile_y) in valid_tiles:
                if (tile_x, tile_y) == valid_tiles[-1]:
                    draw_tile_rect(coords=(tile_x, tile_y), mark="X")
                    # checks if the position of the rectangle has a creature
                    if map_check_for_creatures(tile_x, tile_y, PLAYER) is not None:
                        # if it does, prints out all the creature info on the menu
                        target = map_check_for_creatures(tile_x, tile_y, PLAYER)
                        local_look_surface.fill(Constants.COLOR_BLACK)
                        draw_text(local_look_surface,
                                  target.creature.name_instance + " the " + target.name_object,
                                  menu_text_font,
                                  (10, 0),
                                  Constants.COLOR_GREEN, Constants.COLOR_BLACK)
                        draw_text(local_look_surface,
                                  target.creature.creature_d,
                                  menu_text_font, (10, menu_text_height), menu_text_color, Constants.COLOR_BLACK)
                        draw_text(local_look_surface,
                                  "Base hp: " + str(target.creature.max_hp),
                                  menu_text_font, (10, menu_text_height * 2), Constants.COLOR_RED,
                                  Constants.COLOR_BLACK)
                        draw_text(local_look_surface,
                                  "Base atk: " + str(target.creature.base_atk),
                                  menu_text_font, (10, menu_text_height * 3), menu_text_color, Constants.COLOR_BLACK)
                        draw_text(local_look_surface,
                                  "Base def: " + str(target.creature.base_def),
                                  menu_text_font, (10, menu_text_height * 4), menu_text_color, Constants.COLOR_BLACK)
                        draw_text(local_look_surface,
                                  "Base attack bonus: " + str(target.creature.base_chance),
                                  menu_text_font, (10, menu_text_height * 5), menu_text_color, Constants.COLOR_BLACK)
                        draw_text(local_look_surface,
                                  "Base ac: " + str(target.creature.base_ac),
                                  menu_text_font, (10, menu_text_height * 6), menu_text_color, Constants.COLOR_BLACK)

                    # checks if the rectangle position has an item in it
                    elif map_check_for_items(tile_x, tile_y) is not None:
                        target = map_check_for_items(tile_x, tile_y)
                        local_look_surface.fill(Constants.COLOR_BLACK)
                        # if it does, checks again, to determine if the item is an item or a piece of equipment
                        if target.item.item_name is not None:
                            # if its an item, print all the info
                            draw_text(local_look_surface,
                                      target.item.item_name,
                                      menu_text_font, (10, 0), Constants.COLOR_GREEN,
                                      Constants.COLOR_BLACK)
                            draw_text(local_look_surface,
                                      target.item.item_d,
                                      menu_text_font, (10, menu_text_height * 2), menu_text_color,
                                      Constants.COLOR_BLACK)
                            if target.item.num_charges != 0:
                                draw_text(local_look_surface,
                                          "Number of uses: " + str((target.item.num_charges)),
                                          menu_text_font, (10, menu_text_height * 3), menu_text_color,
                                          Constants.COLOR_BLACK)
                        elif target.equipment:
                            # if its a piece of equipment, print only the relevant parts
                            draw_text(local_look_surface,
                                      target.equipment.owner.name_object,
                                      menu_text_font, (10, 0), Constants.COLOR_GREEN,
                                      Constants.COLOR_BLACK)
                            for line, (name) in enumerate(target.equipment.stat_display()):
                                    draw_text(local_look_surface,
                                              name,
                                              Constants.FONT_MESSAGE_TEXT,
                                              (10, 13 + (line * menu_text_height)),
                                              menu_text_color, Constants.COLOR_BLACK)


                else:
                    draw_tile_rect(coords=(tile_x, tile_y))

        SURFACE_MAIN.blit(SURFACE_MAP, (0, 0), CAMERA.rectangle)
        SURFACE_MAIN.blit(local_look_surface, (menu_x, menu_y))

        draw_messages()

        # updates display
        pygame.display.flip()

        # ticks clock
        CLOCK.tick(Constants.GAME_FPS)

def menu_help():
    menu_close = False

    window_width = Constants.CAMERA_WIDTH
    window_height = Constants.CAMERA_HEIGHT

    menu_text_font = Constants.FONT_MESSAGE_TEXT
    menu_text_height = helper_text_height(menu_text_font)

    menu_width = 410
    menu_height = menu_text_height * 20
    menu_x = (window_width / 2) - (menu_width / 2)
    menu_y = (window_height / 2) - (menu_height / 2)

    menu_text_color = Constants.COLOR_WHITE

    local_help_surface = pygame.Surface((menu_width, menu_height))

    while not menu_close:

        ## CLEAR MENU
        local_help_surface.fill(Constants.COLOR_BLACK)

        ## TEXT FOR MENU
        draw_text(local_help_surface, "WELCOME TO THE GAME",
                  Constants.FONT_MESSAGE_TEXT,
                  (95, 0), Constants.COLOR_GREEN, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Move with arrow keys or numpad",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 2 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Move onto an occupied space to attack",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 3 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Press i to open your inventory",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 4 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "left click on an item in your inventory",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 5 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "to use it",
                  Constants.FONT_MESSAGE_TEXT,
                  (130, 6 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "right click on an item in your inventory to drop it",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 7 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "to drop it",
                  Constants.FONT_MESSAGE_TEXT,
                  (130, 8 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Press f to use a set of stairs",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 9 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Press l to look",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 10 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Press g to pick up items, and d to drop",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 11 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Press c for character information",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 12 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Press l to inspect ",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 13 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "Press h to close this menu",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 14 * menu_text_height), Constants.COLOR_WHITE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "When you level up, go to the character",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 15 * menu_text_height), Constants.COLOR_PURPLE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "menu and press the respective numpad key",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 16 * menu_text_height), Constants.COLOR_PURPLE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "to increase that attribute",
                  Constants.FONT_MESSAGE_TEXT,
                  (90, 17 * menu_text_height), Constants.COLOR_PURPLE, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "find the corenucleus and bring it back",
                  Constants.FONT_MESSAGE_TEXT,
                  (10, 18 * menu_text_height), Constants.COLOR_GREEN, Constants.COLOR_BLACK)

        draw_text(local_help_surface, "to the start to win!",
                  Constants.FONT_MESSAGE_TEXT,
                  (110, 19 * menu_text_height), Constants.COLOR_GREEN, Constants.COLOR_BLACK)

        ## INPUT FOR CLOSE MENU
        events_list = pygame.event.get()

        for event in events_list:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_h:
                    menu_close = True

                if event.key == pygame.K_i:
                    menu_close = True
                    menu_inventory()

        ## RENDER GAME
        draw_game()

        ## DISPLAY MENU
        SURFACE_MAIN.blit(local_help_surface, (menu_x, menu_y))

        CLOCK.tick(Constants.GAME_FPS)

        pygame.display.flip()

def menu_character():
    global PLAYER

    menu_close = False

    window_width = Constants.CAMERA_WIDTH
    window_height = Constants.CAMERA_HEIGHT

    menu_width = 230
    menu_height = 350
    menu_x = 10
    menu_y = (window_height / 2) - (menu_height / 2)
    dist_ment = Constants.CELL_HEIGHT + 10

    menu_text_font = Constants.FONT_MENU_TEXT
    menu_text_height = helper_text_height(menu_text_font)

    menu_text_color = Constants.COLOR_WHITE

    local_character_surface = pygame.Surface((menu_width, menu_height))

    while not menu_close:

        ## CLEAR MENU
        local_character_surface.fill(Constants.COLOR_BLACK)

        ## display character info

        ## get input
        events_list = pygame.event.get()
        mouse_x, mouse_y = pygame.mouse.get_pos()

        mouse_x_rel = mouse_x - menu_x
        mouse_y_rel = (mouse_y - menu_y) - 60

        mouse_in_window = (0 < mouse_x_rel < menu_width and
                           0 < mouse_y_rel + 60 < menu_height)

        mouse_line_selection = int(mouse_y_rel / menu_text_height)

        # gets all the player info

        # displays the players name
        draw_text(local_character_surface,
                  PLAYER.display_name,
                  Constants.FONT_MESSAGE_TEXT,
                  (menu_x, dist_ment),
                  Constants.COLOR_GREEN)

        for event in events_list:

            if event.type == pygame.QUIT:
                return "QUIT"

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:
                    menu_close = True

                if event.key == pygame.K_i:
                    menu_close = True
                    menu_inventory()

                if event.key == pygame.K_h:
                    menu_close = True
                    menu_help()

                if event.key == pygame.K_KP1:
                    PLAYER.creature.increase_stat(target=PLAYER, stat=1)
                    menu_close = True

                if event.key == pygame.K_KP2:
                    PLAYER.creature.increase_stat(target=PLAYER, stat=2)
                    menu_close = True

                if event.key == pygame.K_KP3:
                    PLAYER.creature.increase_stat(target=PLAYER, stat=3)
                    menu_close = True

                if event.key == pygame.K_KP4:
                    PLAYER.creature.increase_stat(target=PLAYER, stat=4)
                    menu_close = True

                if event.key == pygame.K_KP5:
                    PLAYER.creature.increase_stat(target=PLAYER, stat=5)
                    menu_close = True

                # shows all the player info on screen
        for line, (name) in enumerate(PLAYER.creature.display_stats()):

            if line == mouse_line_selection and mouse_in_window:
                draw_text(local_character_surface,
                          name,
                          Constants.FONT_MESSAGE_TEXT,
                          (0, 60 + (line * menu_text_height)),
                          menu_text_color, Constants.COLOR_GREY)
            else:
                draw_text(local_character_surface,
                          name,
                          Constants.FONT_MESSAGE_TEXT,
                          (0, 60 + (line * menu_text_height)),
                          menu_text_color, Constants.COLOR_BLACK)

        ## RENDER GAME
        draw_game()

        ## DISPLAY MENU
        SURFACE_MAIN.blit(local_character_surface, (menu_x, menu_y))
        SURFACE_MAIN.blit(PLAYER.animation[PLAYER.sprite_image], (menu_width / 2 - 5, menu_y + menu_x))

        CLOCK.tick(Constants.GAME_FPS)

        pygame.display.flip()

def menu_name():
    global PLAYER

    menu_close = False

    # MENU VARS #
    name_menu_width = 500
    name_menu_height = 200

    text_surf_w = name_menu_width - 10
    text_surf_h = name_menu_height / 4

    menu_x = (Constants.CAMERA_WIDTH / 2 - name_menu_width / 2)
    menu_y = (Constants.CAMERA_HEIGHT / 2 - name_menu_height / 2)

    text_surf_x = menu_x + 5
    text_surf_y = menu_y + 100

    startb_x = menu_x + 420
    startb_y = text_surf_y + 75
    backb_x = menu_x + 80
    backb_y = text_surf_y + 75

    menu_text_font = Constants.FONT_MENU_TEXT

    name_menu_surface = pygame.Surface((name_menu_width, name_menu_height))

    text_surf = pygame.Surface((text_surf_w, text_surf_h))

    # button decs
    start_button = ui_Button(SURFACE_MAIN, "START", (100, 30), (startb_x, startb_y))
    back_button = ui_Button(SURFACE_MAIN, "BACK", (100, 30), (backb_x, backb_y))

    random_name = random.choice(["globin", "globoid", "globule", "gobbo", "g' bizzy", "globus", "glibs", "globinoid",
                                 "glob glob", "gobb", "glibus", "glebb", "glabuga", "hobglob"])

    name = random_name
    while not menu_close:

        events_list = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()

        name_menu_surface.fill(Constants.COLOR_GREY)
        text_surf.fill(Constants.COLOR_WHITE)

        draw_text(name_menu_surface, "Name your character", Constants.FONT_TITLE_SCREEN,
                  (10, 0), Constants.COLOR_GREEN, Constants.COLOR_GREY)

        game_input = (events_list, mouse_position)

        for event in events_list:

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if len(name) >= Constants.MAX_NAME_LEN - 1:
                    name = name[:-1]
                else:
                    if event.unicode.isalpha():
                        name += event.unicode
                        obj_Game.name = name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]

            if start_button.update(game_input):
                obj_Game.name = name
                pygame.mixer.music.stop()
                # starts new game
                game_new()
                game_main_loop()
                game_initialize()

            if back_button.update(game_input):
                menu_main()

        # DRAW MENU
        block = Constants.FONT_TITLE_SCREEN.render(name, True, Constants.COLOR_GREEN)

        SURFACE_MAIN.fill(Constants.COLOR_BLACK)
        SURFACE_MAIN.blit(name_menu_surface, (menu_x, menu_y))
        SURFACE_MAIN.blit(text_surf, (text_surf_x, text_surf_y))
        SURFACE_MAIN.blit(block, (text_surf_x + 5, text_surf_y + 5))

        start_button.draw()
        back_button.draw()

        # UPDATE SURFACE
        pygame.display.flip()


#   ____ _____ _   _ _____ ____      _  _____ ___  ____  ____
#  / ___| ____| \ | | ____|  _ \    / \|_   _/ _ \|  _ \/ ___|
# | |  _|  _| |  \| |  _| | |_) |  / _ \ | || | | | |_) \___ \
# | |_| | |___| |\  | |___|  _ <  / ___ \| || |_| |  _ < ___) |
#  \____|_____|_| \_|_____|_| \_\/_/   \_\_| \___/|_| \_\____/

## PLAYER GENERATOR
def gen_player(coords):
    global PLAYER

    x, y = coords

    # item_com = com_Item(corpse="S_PLAYER_CORPSE")
    container_com = com_Container(max_items=16)
    creature_com = com_Creature("Globin",
                                hp=20,
                                death_function=death_player)
    PLAYER = obj_Actor(x, y, "Globin", animation_key="A_PLAYER", creature=creature_com,
                       depth=Constants.DEPTH_PLAYER, container=container_com)

    GAME.current_objects.append(PLAYER)


## SPECIAL

def gen_stairs(coords, downwards=True):
    x, y = coords

    if downwards:
        stairs_com = com_Stairs()
        stairs = obj_Actor(x, y, "stairs", animation_key="S_STAIRDOWN", stairs=stairs_com, depth=Constants.DEPTH_BACK)

    else:
        stairs_com = com_Stairs(downwards)
        stairs = obj_Actor(x, y, "stairs", animation_key="S_STAIRUP", stairs=stairs_com, depth=Constants.DEPTH_BACK)

    GAME.current_objects.append(stairs)


def gen_portal(coords):
    x, y = coords
    port_com = com_Exitportal()
    portal = obj_Actor(x, y, "exit portal", animation_key="S_DOORCLOSED",
                       depth=Constants.DEPTH_BACK,
                       exitportal=port_com)

    GAME.current_objects.append(portal)


def gen_core(coords):
    x, y = coords

    item_com = com_Item()
    return_object = obj_Actor(x, y, "CORENUCLEUS", animation_key="S_CORENUCLEUS", depth=Constants.DEPTH_ITEM,
                              item=item_com)

    GAME.current_objects.append(return_object)


## ITEMS
def gen_item_tier_1(coords):
    random_num = random.randint(1, 100)


    if random_num <= 50:
        new_item = gen_usable_tier_1(coords)

    elif 50 < random_num:
        new_item = gen_equip_tier_1(coords)

    GAME.current_objects.append(new_item)

def gen_item_tier_2(coords):
    random_num = random.randint(1, 100)

    if random_num <= 50:
        new_item = gen_usable_tier_2(coords)

    elif 50 < random_num:
        new_item = gen_equip_tier_2(coords)

    GAME.current_objects.append(new_item)

def gen_usable_tier_1(coords):
    random_num = random.randint(1, 100)

    if random_num <= 10:
        new_item = gen_device_laser_blaster(coords)

    elif 10 < random_num <= 20:
        new_item = gen_device_brain_scrambler(coords)

    elif 20 < random_num <= 30:
        new_item = gen_device_grenade_fire(coords)

    elif 30 < random_num <= 40:
        new_item = gen_serum_performanceenhancer(coords)

    elif 40 < random_num <= 50:
        new_item = gen_serum_autotransfuser(coords)

    elif 50 < random_num <= 60:
        new_item = gen_serum_vitalityinjector(coords)

    elif 60 < random_num <= 70:
        new_item = gen_serum_attribooster(coords)

    elif 70 < random_num <= 80:
        new_item = gen_serum_attriswapper(coords)

    elif 80 < random_num <= 90:
        new_item = gen_device_pluralis_blaster(coords)

    elif 90 < random_num:
        new_item = gen_device_grenade_implosion(coords)

    return new_item

def gen_usable_tier_2(coords):
    random_num = random.randint(1, 100)

    if random_num <= 10:
        new_item = gen_serum_performanceenhancer(coords)

    elif 10 < random_num <= 25:
        new_item = gen_serum_autotransfuser(coords)

    elif 25 < random_num <= 40:
        new_item = gen_serum_attriswapper(coords)

    elif 40 < random_num <= 50:
        new_item = gen_serum_booster2(coords)

    elif 50 < random_num <= 60:
        new_item = gen_device_pluralis_blaster(coords)

    elif 60 < random_num <= 70:
        new_item = gen_device_grenade_implosion(coords)

    elif 70 < random_num <= 80:
        new_item = gen_device_brain_scrambler(coords)

    elif 80 < random_num <= 90:
        new_item = gen_device_immensiumgrenade(coords)

    elif 90 < random_num:
        new_item = gen_device_pluralisgrenade(coords)

    return new_item

def gen_device_laser_blaster(coords):
    x, y = coords

    damage = random.randint(5, 11)
    charges = random.randint(1, 3)

    item_com = com_Item(use_function=deploy_device_laser_blaster, value=damage, num_charges=charges,
                        item_name="Laser Blaster",
                        item_d="Standard blasting device, not many shots left though")

    return_object = obj_Actor(x, y, "Laser Blaster", depth=Constants.DEPTH_ITEM,
                              animation_key="S_LASERBLASTER_GUN", item=item_com)

    return return_object

def gen_device_pluralis_blaster(coords):
    x, y = coords

    damage = random.randint(2, 6)
    charges = random.randint(14, 20)

    item_com = com_Item(use_function=deploy_device_pluralis_blaster, value=damage, num_charges=charges,
                        item_name="Pluralis blaster",
                        item_d="blaster from the pluralis company, their motto is 'pluralis finishes last'")

    return_object = obj_Actor(x, y, "pluralis blaster", depth=Constants.DEPTH_ITEM,
                              animation_key="S_PLURALISBLASTER_GUN", item=item_com)

    return return_object

def gen_device_grenade_implosion(coords):
    x, y = coords

    damage = random.randint(19, 25)

    item_com = com_Item(use_function=deploy_device_implosiongrenade, value=damage,
                        item_name="implosion grenade",
                        item_d="a powerful device designed to cause a controlled, single target explosion")

    return_object = obj_Actor(x, y, "implosion grenade", depth=Constants.DEPTH_ITEM,
                              animation_key="S_IMPLOSION_GRENADE", item=item_com)

    return return_object

def gen_device_grenade_fire(coords):
    x, y = coords

    damage = random.randint(6, 12)

    item_com = com_Item(use_function=deploy_device_firegrenade, value=damage, item_name="Fire Grenade",
                        item_d="A powerful explosive device")

    return_object = obj_Actor(x, y, "Fire Grenade", animation_key="S_FIRE_GRENADE",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_device_brain_scrambler(coords):
    x, y = coords

    num_turns = random.randint(3, 9)
    charges = random.randint(1, 3)

    item_com = com_Item(use_function=deploy_device_brain_scrambler, value=num_turns, num_charges=charges,
                        item_name="Brain Scrambler",
                        item_d="reduces mental capacity of target to that of a choggus")

    return_object = obj_Actor(x, y, "Brain Scrambler", animation_key="S_BRAINSCRAMBLER_GUN",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_serum_performanceenhancer(coords):
    x, y = coords

    stat_increase = random.randint(1, 2)

    item_com = com_Item(use_function=deploy_serum_performance_enhancer, value=stat_increase,
                        item_name="Performance Enhancer",
                        item_d="randomly increases one of your stats, but using it will hurt bad")

    return_object = obj_Actor(x, y, "Performance Enhancer", animation_key="S_PERFORMANCEENHANCER_SERUM",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_serum_autotransfuser(coords):
    x, y = coords

    heal_value = random.randint(10, 15)

    item_com = com_Item(use_function=deploy_serum_autotransfuser, value=heal_value,
                        item_name="AUTO TRANSFUSER SERUM",
                        item_d="heals your wounds but reduces one of your attributes randomly")

    return_object = obj_Actor(x, y, "AUTO TRANSFUSER SERUM", animation_key="S_AUTOTRANSFUSER_SERUM",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_serum_vitalityinjector(coords):
    x, y = coords

    heal_value = random.randint(5, 10)

    item_com = com_Item(use_function=cast_heal, value=heal_value,
                        item_name="VITALITY INJECTOR SERUM",
                        item_d="quick shot of healing with zero side-effects!")

    return_object = obj_Actor(x, y, "VITALITY INJECTOR SERUM", animation_key="S_VITALITYINJECTOR_SERUM",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_serum_attribooster(coords):
    x, y = coords

    stat_increase = 1

    item_com = com_Item(use_function=deploy_serum_attribooster, value=stat_increase,
                        item_name="attribooster",
                        item_d="randomly increases one of your stats and has no drawbacks!")

    return_object = obj_Actor(x, y, "attribooster", animation_key="S_ATTRIBOOSTER_SERUM",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_serum_attriswapper(coords):
    x, y = coords

    stat_increase = 2

    item_com = com_Item(use_function=deploy_serum_attriswapper, value=stat_increase,
                        item_name="attriswapper",
                        item_d="randomly increases one of your stats while draining from another")

    return_object = obj_Actor(x, y, "attriswapper", animation_key="S_ATTRISWAPPER_SERUM",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

# TIER 2


def gen_device_pluralisgrenade(coords):
    x, y = coords

    damage = random.randint(5, 10)
    charges = random.randint(9, 12)

    item_com = com_Item(use_function=deploy_device_pluralisgrenade, value=damage, item_name="Pluralis Grenade",
                        num_charges=charges,
                        item_d="A cleverly designed reusable grenade")

    return_object = obj_Actor(x, y, "pluralis grenade", animation_key="S_PLURALIS_GRENADE",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_device_immensiumgrenade(coords):
    x, y = coords

    damage = random.randint(12, 16)

    item_com = com_Item(use_function=deploy_device_immensiumgrenade, value=damage, item_name="immensium Grenade",
                        item_d="immensium brand grenade, this thing is sure to make a big explosion")

    return_object = obj_Actor(x, y, "immensium Grenade", animation_key="S_IMMENSIUM_GRENADE",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_serum_booster2(coords):
    x, y = coords

    type = random.randint(1, 4)

    if type == 1:
        animkey = "S_I_BOOSTER_SERUM"
        name = "Intelligence booster"
    elif type == 2:
        animkey = "S_D_BOOSTER_SERUM"
        name = "Dexterity booster"
    elif type == 3:
        animkey = "S_S_BOOSTER_SERUM"
        name = "Strength booster"
    elif type == 4:
        animkey = "S_W_BOOSTER_SERUM"
        name = "Wisdom Booster"



    item_com = com_Item(use_function=deploy_serum_booster2, value=type,
                        item_name=name,
                        item_d="a booster for the desperate, increases one attribute at the cost of two others")

    return_object = obj_Actor(x, y, name, animation_key=animkey,
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

# EQUIPMENT

def gen_equip_tier_1(coords):
    random_num = random.randint(0, 100)

    if random_num <= 5:
        new_item = gen_weapon_blackjack(coords)
    elif 5 < random_num <= 10:
        new_item = gen_weapon_podaxe(coords)
    elif 10 < random_num <= 15:
        new_item = gen_helmet_thinkcap(coords)
    elif 15 < random_num <= 20:
        new_item = gen_helmet_basicvisor(coords)
    elif 20 < random_num <= 30:
        new_item = gen_glove_pglove(coords)
    elif 30 < random_num <= 40:
        new_item = gen_glove_gremlingrippers(coords)
    elif 40 < random_num <= 50:
        new_item = gen_boot_pboot(coords)
    elif 50 < random_num <= 60:
        new_item = gen_boot_chemsteps(coords)
    elif 60 < random_num <= 70:
        new_item = gen_boot_gogysneaks(coords)
    elif 70 < random_num <= 80:
        new_item = gen_glove_chemgraps(coords)
    elif 80 < random_num <= 90:
        new_item = gen_vest_tvest(coords)
    elif 90 < random_num <= 95:
        new_item = gen_armor_goblincoat(coords)
    elif 95 < random_num:
        new_item = gen_armor_gremlincoat(coords)



    return new_item

# TIER 1


def gen_vest_tvest(coords):
    x, y = coords

    bonus_ac = 2
    bonus_def = 1
    equipment_com = com_Equipment(ac_bonus=bonus_ac, defense_bonus=bonus_def,
                                  slot="vest",
                                  equipment_d="made by the same company that makes choggus mace")

    return_object = obj_Actor(x, y, "Toothproof vest", animation_key="S_TOOTHPROOFVEST",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_boot_pboot(coords):
    x, y = coords

    bonus_dex = random.randint(1, 2)

    equipment_com = com_Equipment(dexterity_bonus=bonus_dex,
                                  slot="boot",
                                  equipment_d="for all your kicking needs")

    return_object = obj_Actor(x, y, "heavy duty boots", animation_key="S_PBOOT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_boot_chemsteps(coords):
    x, y = coords

    bonus_int = random.randint(1, 2)

    equipment_com = com_Equipment(intelligence_bonus=bonus_int,
                                  slot="boot",
                                  equipment_d="FOR STEPPING ON ALL THOSE CHEMICALS")

    return_object = obj_Actor(x, y, "Chemical Steppers", animation_key="S_CHEMSTEPS",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_boot_gogysneaks(coords):
    x, y = coords

    bonus_dex = random.randint(1, 2)

    equipment_com = com_Equipment(dexterity_bonus=bonus_dex,
                                  slot="boot",
                                  equipment_d="you feel more like a coward just from wearing these")

    return_object = obj_Actor(x, y, "gogy sneakers", animation_key="S_GOGYSNEAKERS",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_glove_pglove(coords):
    x, y = coords

    bonus_str = random.randint(1, 2)


    equipment_com = com_Equipment(strength_bonus=bonus_str,
                                  slot="glove",
                                  equipment_d="for all your punching needs")

    return_object = obj_Actor(x, y, "heavy duty gloves", animation_key="S_PGLOVE",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_glove_chemgraps(coords):
    x, y = coords

    bonus_chance = random.randint(2, 3)

    equipment_com = com_Equipment(chance_bonus=bonus_chance,
                                  slot="glove",
                                  equipment_d="for grapping all those chemicals")

    return_object = obj_Actor(x, y, "chemical Grappers", animation_key="S_CHEMGRAPS",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_glove_gremlingrippers(coords):
    x, y = coords

    bonus_int = random.randint(1, 2)

    equipment_com = com_Equipment(intelligence_bonus=bonus_int,
                                  slot="glove",
                                  equipment_d="helps you hold onto stolen goods better")

    return_object = obj_Actor(x, y, "gremlin grippers", animation_key="S_GREMLINGRIPPERS",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_helmet_basicvisor(coords):
    x, y = coords

    bonus_dex = random.randint(1, 2)
    bonus_ac = 1


    equipment_com = com_Equipment(dexterity_bonus=bonus_dex, ac_bonus=bonus_ac,
                                  slot="head",
                                  equipment_d="protection for the head but not for the teeth")

    return_object = obj_Actor(x, y, "Basic Visor", animation_key="S_BASICVISOR",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_helmet_thinkcap(coords):
    x, y = coords

    bonus_int = random.randint(2, 3)
    bonus_wis = random.randint(2, 3)

    equipment_com = com_Equipment(intelligence_bonus=bonus_int, wisdom_bonus=bonus_wis,
                                  slot="head",
                                  equipment_d="the pulsating live brain helps you think betterer")

    return_object = obj_Actor(x, y, "Thinking cap", animation_key="S_THINKCAP",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_weapon_blackjack(coords):
    x, y = coords

    bonus_atk = random.randint(1, 4)
    bonus_str = random.randint(1, 2)
    bonus_dex = random.randint(1, 2)


    equipment_com = com_Equipment(attack_bonus=bonus_atk, dexterity_bonus=bonus_dex,strength_bonus=bonus_str, slot="hand_right",
                                  equipment_d="simple and efficient")

    return_object = obj_Actor(x, y, "Blackjack", animation_key="S_BLACKJACK",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_weapon_choggclub(coords):
    x, y = coords

    bonus_atk = random.randint(3, 5)

    equipment_com = com_Equipment(attack_bonus=bonus_atk,
                                  slot="hand_right",
                                  equipment_d="brush it at least 3 times a day and after every meal")

    return_object = obj_Actor(x, y, "Choggus club", animation_key="S_CHOGGUSCLUB",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_weapon_podaxe(coords):
    x, y = coords

    bonus_atk = random.randint(1, 3)
    bonus_dex = random.randint(1, 2)
    bonus_wis = random.randint(1, 2)

    equipment_com = com_Equipment(attack_bonus=bonus_atk, dexterity_bonus=bonus_dex, wisdom_bonus=bonus_wis,
                                  slot="hand_right",
                                  equipment_d="100% green killing tool")

    return_object = obj_Actor(x, y, "POD AXE", animation_key="S_PODAXE",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_armor_goblincoat(coords):
    x, y = coords

    bonus_ac = random.randint(2, 3)
    bonus_con = random.randint(1, 2)
    bonus_int = random.randint(1, 2)

    equipment_com = com_Equipment(ac_bonus=bonus_ac,constitution_bonus=bonus_con,intelligence_bonus=bonus_int, slot="body_coat",
                                  equipment_d="weird how these dont have seams")

    return_object = obj_Actor(x, y, "Goblin Coat", animation_key="S_GOBLINCOAT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_armor_gremlincoat(coords):
    x, y = coords

    bonus_dex = random.randint(1, 2)
    bonus_int = random.randint(1, 2)
    bonus_wis = random.randint(1, 2)

    equipment_com = com_Equipment(intelligence_bonus=bonus_int, dexterity_bonus=bonus_dex, wisdom_bonus=bonus_wis,
                                  slot="body_coat",
                                  equipment_d="not authentic gremlin fur but it'll have to do")

    return_object = obj_Actor(x, y, "GREMLIn fur Coat", animation_key="S_GREMLINCOAT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_armor_labcoat(coords):
    x, y = coords

    bonus_ac = 1
    bonus_int = random.randint(2, 3)
    bonus_wis = random.randint(2, 3)


    equipment_com = com_Equipment(ac_bonus=bonus_ac, intelligence_bonus=bonus_int, wisdom_bonus=bonus_wis,
                                  slot="body_coat",
                                  equipment_d="smart move, impersonating healthcare staff")

    return_object = obj_Actor(x, y, "Labcoat", animation_key="S_LABCOAT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object


# TIER 2

def gen_equip_tier_2(coords):
    random_num = random.randint(0, 100)

    if random_num <= 5:
        new_item = gen_weapon_blackjack1(coords)
    elif 5 < random_num <= 10:
        new_item = gen_weapon_sleechlash(coords)
    elif 10 < random_num <= 15:
        new_item = gen_helmet_thinkcap1(coords)
    elif 15 < random_num <= 20:
        new_item = gen_helmet_basicvisor1(coords)
    elif 20 < random_num <= 25:
        new_item = gen_helmet_vixhelmet(coords)
    elif 25 < random_num <= 35:
        new_item = gen_glove_pglove1(coords)
    elif 35 < random_num <= 45:
        new_item = gen_glove_matronglove(coords)
    elif 45 < random_num <= 55:
        new_item = gen_glove_boxglove(coords)
    elif 55 < random_num <= 65:
        new_item = gen_boot_pboot1(coords)
    elif 65 < random_num <= 75:
        new_item = gen_boot_chemsteps1(coords)
    elif 75 < random_num <= 85:
        new_item = gen_glove_chemgraps1(coords)
    elif 85 < random_num <= 90:
        new_item = gen_vest_tvest1(coords)
    elif 90 < random_num <= 95:
        new_item = gen_armor_goblincoat1(coords)
    elif 95 < random_num:
        new_item = gen_armor_greatergremlincoat(coords)

    return new_item

def gen_vest_tvest1(coords):
    x, y = coords

    bonus_ac = 3
    bonus_def = 2
    equipment_com = com_Equipment(ac_bonus=bonus_ac, defense_bonus=bonus_def,
                                  slot="vest",
                                  equipment_d="made by the same company that makes choggus mace")

    return_object = obj_Actor(x, y, "Toothproof vest+1", animation_key="S_TOOTHPROOFVEST",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_boot_pboot1(coords):
    x, y = coords

    bonus_dex = (random.randint(1, 2)+1)

    equipment_com = com_Equipment(dexterity_bonus=bonus_dex,
                                  slot="boot",
                                  equipment_d="for all your kicking needs")

    return_object = obj_Actor(x, y, "heavy duty boots+1", animation_key="S_PBOOT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_boot_chemsteps1(coords):
    x, y = coords

    bonus_int = (random.randint(1, 2)+1)

    equipment_com = com_Equipment(intelligence_bonus=bonus_int,
                                  slot="boot",
                                  equipment_d="FOR STEPPING ON ALL THOSE CHEMICALS")

    return_object = obj_Actor(x, y, "Chemical Steppers+1", animation_key="S_CHEMSTEPS",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_glove_pglove1(coords):
    x, y = coords

    bonus_str = (random.randint(1, 2)+1)


    equipment_com = com_Equipment(strength_bonus=bonus_str,
                                  slot="glove",
                                  equipment_d="for all your punching needs")

    return_object = obj_Actor(x, y, "heavy duty gloves+1", animation_key="S_PGLOVE",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_glove_chemgraps1(coords):
    x, y = coords

    bonus_chance = (random.randint(2, 3)+1)

    equipment_com = com_Equipment(chance_bonus=bonus_chance,
                                  slot="glove",
                                  equipment_d="for grapping all those chemicals")

    return_object = obj_Actor(x, y, "chemical Grappers+1", animation_key="S_CHEMGRAPS",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_glove_matronglove(coords):
    x, y = coords

    bonus_def = 2
    bonus_wis = random.randint(2, 4)

    equipment_com = com_Equipment(defense_bonus=bonus_def, wisdom_bonus=bonus_wis,
                                  slot="glove",
                                  equipment_d="too many fingerholes is the least of this glove's issues")

    return_object = obj_Actor(x, y, "monster matron gloves", animation_key="S_MATRONGLOVE",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_glove_boxglove(coords):
    x, y = coords

    bonus_atk = random.randint(3, 5)

    equipment_com = com_Equipment(attack_bonus=bonus_atk,
                                  slot="glove",
                                  equipment_d="makes you hungry for ears")

    return_object = obj_Actor(x, y, "box lox gloves", animation_key="S_BOXGLOVE",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_armor_goblincoat1(coords):
    x, y = coords

    bonus_ac = random.randint(2, 3)
    bonus_con = (random.randint(1, 2)+1)
    bonus_int = (random.randint(1, 2)+1)

    equipment_com = com_Equipment(ac_bonus=bonus_ac,constitution_bonus=bonus_con,intelligence_bonus=bonus_int, slot="body_coat",
                                  equipment_d="weird how these dont have seams")

    return_object = obj_Actor(x, y, "Goblin Coat+1", animation_key="S_GOBLINCOAT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_armor_labcoat1(coords):
    x, y = coords

    bonus_ac = 1
    bonus_int = (random.randint(2, 3)+1)
    bonus_wis = (random.randint(2, 3)+1)


    equipment_com = com_Equipment(ac_bonus=bonus_ac, intelligence_bonus=bonus_int, wisdom_bonus=bonus_wis,
                                  slot="body_coat",
                                  equipment_d="smart move, impersonating healthcare staff")

    return_object = obj_Actor(x, y, "Labcoat+1", animation_key="S_LABCOAT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_armor_greatergremlincoat(coords):
    x, y = coords

    bonus_ac = random.randint(3, 4)
    bonus_dex = random.randint(2, 3)
    bonus_int = random.randint(2, 3)

    equipment_com = com_Equipment(ac_bonus=bonus_ac, dexterity_bonus=bonus_dex, intelligence_bonus=bonus_int,
                                  slot="body_coat",
                                  equipment_d="made out of real greater gremlin fur")

    return_object = obj_Actor(x, y, "greater gremlin fur coat", animation_key="S_GREATERGREMLINCOAT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_helmet_basicvisor1(coords):
    x, y = coords

    bonus_dex = (random.randint(1, 2)+1)
    bonus_ac = 1


    equipment_com = com_Equipment(dexterity_bonus=bonus_dex, ac_bonus=bonus_ac,
                                  slot="head",
                                  equipment_d="protection for the head but not for the teeth")

    return_object = obj_Actor(x, y, "Basic Visor+1", animation_key="S_BASICVISOR",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_helmet_thinkcap1(coords):
    x, y = coords

    bonus_int = (random.randint(2, 3)+1)
    bonus_wis = (random.randint(2, 3)+1)

    equipment_com = com_Equipment(intelligence_bonus=bonus_int, wisdom_bonus=bonus_wis,
                                  slot="head",
                                  equipment_d="the pulsating live brain helps you think betterer")

    return_object = obj_Actor(x, y, "Thinking cap+1", animation_key="S_THINKCAP",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_helmet_vixhelmet(coords):
    x, y = coords

    bonus_dex = random.randint(4, 8)
    equipment_com = com_Equipment(dexterity_bonus=bonus_dex,
                                  slot="head",
                                  equipment_d="cant stop yourself from spittin bars while wearing this")

    return_object = obj_Actor(x, y, "VIXLAX HELMET", animation_key="S_VIXHELMET",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_weapon_blackjack1(coords):
    x, y = coords

    bonus_atk = (random.randint(1, 4)+1)
    bonus_str = (random.randint(1, 2)+1)
    bonus_dex = (random.randint(1, 2)+1)


    equipment_com = com_Equipment(attack_bonus=bonus_atk, dexterity_bonus=bonus_dex,strength_bonus=bonus_str, slot="hand_right",
                                  equipment_d="simple and efficient")

    return_object = obj_Actor(x, y, "Blackjack+1", animation_key="S_BLACKJACK",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_weapon_sleechlash(coords):
    x, y = coords


    bonus_atk = random.randint(3, 6)
    bonus_str = random.randint (2, 3)

    equipment_com = com_Equipment(attack_bonus=bonus_atk, strength_bonus=bonus_str,
                                  slot="hand_right",
                                  equipment_d="pretty much just a tube with teeth")

    return_object = obj_Actor(x, y, "sleech lash", animation_key="S_SLEECHLASH",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

# BOSS LOOT

def gen_helmet_usmskull(coords):
    x, y = coords

    bonus_str = 6
    bonus_dex = 6
    bonus_int = 6
    bonus_wis = 6

    equipment_com = com_Equipment(strength_bonus=bonus_str, dexterity_bonus=bonus_dex,
                                  intelligence_bonus=bonus_int, wisdom_bonus=bonus_wis,
                                  slot="head",
                                  equipment_d="wearing this makes you feel like eating grass and sleeping in a coffin")

    return_object = obj_Actor(x, y, "undead space minotaur skull", animation_key="S_USMSKULL",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_armor_chogguskingmantle(coords):
    x, y = coords

    bonus_ac = 3
    bonus_con = 4
    bonus_def = 2

    equipment_com = com_Equipment(ac_bonus=bonus_ac,constitution_bonus=bonus_con,defense_bonus=bonus_def, slot="body_coat",
                                  equipment_d="huge cozy mantle, definetly makes you feel like a king")

    return_object = obj_Actor(x, y, "choggus king mantle", animation_key="S_CHOGGUSKINGMANTLE",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_accessory_chogguskingcrown(coords):
    x, y = coords

    bonus_str = 3
    bonus_con = 3

    equipment_com = com_Equipment(constitution_bonus=bonus_con, strength_bonus=bonus_str, slot="head",
                                  equipment_d="huge shining simbol of royalty")

    return_object = obj_Actor(x, y, "choggus king crown", animation_key="S_CHOGGUSKINGCROWN",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_weapon_serpentwhip(coords):
    x, y = coords

    bonus_atk = 3
    bonus_dex = 1
    bonus_int = 1
    bonus_wis = 1

    equipment_com = com_Equipment(attack_bonus=bonus_atk,
                                  dexterity_bonus=bonus_dex,
                                  intelligence_bonus=bonus_int,
                                  wisdom_bonus=bonus_wis,
                                  slot="hand_right",
                                  equipment_d="surprisingly tough and painful to be whipped with")

    return_object = obj_Actor(x, y, "shifting serpent whip", animation_key="S_SERPENTWHIP",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_accessory_serpenthead(coords):
    x, y = coords

    bonus_dex = 2
    bonus_wis = 2
    bonus_int = 2

    equipment_com = com_Equipment(dexterity_bonus=bonus_dex,
                                  intelligence_bonus=bonus_int,
                                  wisdom_bonus=bonus_wis,
                                  slot="hand_left",
                                  equipment_d="the makeup will absolutely not come off")

    return_object = obj_Actor(x, y, "shifting serpent head", animation_key="S_SERPENTHEAD",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

def gen_item_spwizardstaff(coords):
    x, y = coords

    damage = random.randint(5, 10)
    charges = random.randint(6, 10)

    item_com = com_Item(use_function=cast_spwizardmagic, value=damage, num_charges=charges,
                        item_name="space wizard staff",
                        item_d="pushes a target away, also deals some damage")

    return_object = obj_Actor(x, y, "space wizard staff", animation_key="S_SPWIZARDSTAFF",
                              depth=Constants.DEPTH_ITEM, item=item_com)

    return return_object

def gen_accessory_spwizardhat(coords):
    x, y = coords

    bonus_int = 3
    bonus_wis = 3

    equipment_com = com_Equipment(intelligence_bonus=bonus_int,
                                  wisdom_bonus=bonus_wis,
                                  slot="head",
                                  equipment_d="breezy hat, doesnt offer much protection but makes you feel smarter")

    return_object = obj_Actor(x, y, "space wizard hat", animation_key="S_SPWIZARDHAT",
                              depth=Constants.DEPTH_ITEM, equipment=equipment_com)

    return return_object

## ENEMIES

def gen_enemy_tier_1(coords):
    random_num = random.randint(0, 100)

    if random_num <= 5:
        new_item = gen_enemy_sleech(coords)
        GAME.current_objects.append(new_item)

    elif 5 < random_num <= 20:
        new_item1 = gen_enemy_podman(coords)
        new_item2 = gen_enemy_podman(coords)
        new_item3 = gen_enemy_podman(coords)

        GAME.current_objects.append(new_item1)
        GAME.current_objects.append(new_item2)
        GAME.current_objects.append(new_item3)

    elif 20 < random_num <= 40:
        new_item = gen_enemy_gogy(coords)
        GAME.current_objects.append(new_item)

    elif 40 < random_num <= 50:
        new_item = gen_enemy_gremlin(coords)
        GAME.current_objects.append(new_item)

    elif 50 < random_num <= 60:
        new_item = gen_enemy_spittingspug(coords)
        GAME.current_objects.append(new_item)

    elif random_num > 60:
        new_item = gen_enemy_choggus(coords)
        GAME.current_objects.append(new_item)

def gen_boss_tier_1(coords):

    random_num = random.randint(1, 99)

    if random_num <= 33:
        new_item = gen_enemy_shiftingserpent(coords)
        GAME.current_objects.append(new_item)

    if 33 < random_num <= 66:
        new_item = gen_enemy_choggusking(coords)
        GAME.current_objects.append(new_item)

    if 66 < random_num:
        new_item = gen_enemy_spacewizard(coords)
        GAME.current_objects.append(new_item)

def gen_boss_tier_2(coords):
    new_item = gen_enemy_usm(coords)

    GAME.current_objects.append(new_item)

def gen_enemy_choggus(coords):
    x, y = coords
    hp_random = random.randint(6, 10) + (2*(int(len(GAME.maps_previous)+1)))
    choggus_type = random.randint(0, 1000)

    choggus_name = random.choice(["Retch", "Chunder", "Upchuck", "Hurl", "Yodel", "Brake", "Ralph", "Eject", "Belch",
                                  "Discharge", "Fetchup", "Purge"])

    ai_com = ai_Chase()
    if choggus_type <= 500:
        item_com = com_Item(corpse="S_RED_CHOGGUS_CORPSE", item_name="Corpse of a RED CHOGGUS",
                            use_function=consume_this,
                            value=1,
                            item_d="yup, blubber and skin")
        creature_com = com_Creature(choggus_name, death_function=death_monster, hp=hp_random, xp_reward=100,level=1,
                                    creature_d="a lumbering beast of blubber and skin")
        choggus = obj_Actor(x, y, "Red Choggus", animation_key="A_RED_CHOGGUS", depth=Constants.DEPTH_CREATURES,
                            creature=creature_com, ai=ai_com, item=item_com)

        return choggus

    elif 500 < choggus_type <= 999:
        item_com = com_Item(corpse="S_PURPLE_CHOGGUS_CORPSE", item_name="Corpse of a PURPLE CHOGGUS",
                            use_function=consume_this,
                            value=1,
                            item_d="yup, blubber and skin")
        creature_com = com_Creature(choggus_name, death_function=death_monster, hp=hp_random, xp_reward=100,level=1,
                                    creature_d="a lumbering beast of blubber and skin")
        choggus = obj_Actor(x, y, "Purple Choggus", animation_key="A_PURPLE_CHOGGUS", depth=Constants.DEPTH_CREATURES,
                            creature=creature_com, ai=ai_com, item=item_com)

        return choggus
    else:
        item_com = com_Item(corpse="S_TEAL_CHOGGUS_CORPSE", item_name="Corpse of a TEAL CHOGGUS",
                            use_function=consume_this,
                            value=1,
                            item_d="yup, blubber and skin")
        creature_com = com_Creature(choggus_name, death_function=death_monster, hp=hp_random, xp_reward=100,level=1,
                                    creature_d="a lumbering beast of blubber and skin, whoa this one is teal")
        choggus = obj_Actor(x, y, "Teal Choggus", animation_key="A_TEAL_CHOGGUS", depth=Constants.DEPTH_CREATURES,
                            creature=creature_com, ai=ai_com, item=item_com)

        return choggus

def gen_enemy_sleech(coords):
    x, y = coords


    random_str = random.randint(12, 14) + (len(GAME.maps_previous)+1)
    random_dex = random.randint(14, 16)
    hp_random = random.randint(12, 20) + ((len(GAME.maps_previous)+1)*2)

    sleech_name = random.choice(["Slump", "Slide", "Slick", "Slow", "Slither", "Squeeze"])

    ai_com = ai_Chase()
    item_com = com_Item(corpse="S_SLEECH_CORPSE", item_name="Corpse of a SLEECH",
                        use_function=consume_this,
                        value=9,
                        item_d="pretty much just a tube with teeth")
    creature_com = com_Creature(sleech_name,
                                death_function=death_monster, xp_reward=200,level=3,
                                base_str=random_str, base_dex=random_dex,
                                hp=hp_random,
                                creature_d="The one natural predator of chogguses, but you look like a tastier treat")
    sleech = obj_Actor(x, y, "Sleech", animation_key="A_SLEECH", depth=Constants.DEPTH_CREATURES,
                       creature=creature_com, ai=ai_com, item=item_com)

    return sleech

def gen_enemy_gremlin(coords):
    x, y = coords

    chance_random = random.randint(1, 2)
    hp_random = random.randint(6, 10)

    gremlin_name = random.choice(["pilfer", "sneak", "sleight", "handsy", "pussyfoot", "tiptoe", "purloin", "larcen",
                                  "burgl", "pinch", "nick", "borrow"])

    ai_com = ai_Fleefight()
    item_com = com_Item(corpse="S_GREMLIN_CORPSE", item_name="Corpse of a GREMLIN", use_function=get_drop, value=1,
                        item_d="yuck! this guy didn't clean his nails, use this to get his item")
    creature_com = com_Creature(gremlin_name, xp_reward=75,
                                death_function=death_monster,
                                base_chance=chance_random,
                                level=4,
                                hp=hp_random,
                                creature_d="a skittering gremlin he's holding something in his big hands")
    gremlin = obj_Actor(x, y, "gremlin", animation_key="A_GREMLIN", depth=Constants.DEPTH_CREATURES,
                        creature=creature_com, ai=ai_com, item=item_com)

    return gremlin

def gen_enemy_spittingspug(coords):
    x, y = coords

    chance_random = random.randint(1, 3)
    hp_random = random.randint(4, 6)

    spittingspug_name = random.choice(["totorantula", "buddy recluse", "bella widow", "doggy long legs", "wolf dog",
                                       "fido funnelweb", "oscar orbweaver"])

    ai_com = ai_Ranged()
    item_com = com_Item(corpse="S_SPITTINGSPUG_CORPSE", item_name="Corpse of a SPITTING SPUG",
                        use_function=consume_this,
                        value=4,
                        item_d="mind the stinger")
    creature_com = com_Creature(spittingspug_name, xp_reward=175,
                                death_function=death_monster,
                                base_chance=chance_random,
                                level=2,
                                hp=hp_random,
                                creature_d="an abominable freak of nature fused with a spider, and it spits")
    spittingspug = obj_Actor(x, y, "spitting spug", animation_key="A_SPITTINGSPUG", depth=Constants.DEPTH_CREATURES,
                             creature=creature_com, ai=ai_com, item=item_com)

    return spittingspug

def gen_enemy_podman(coords):
    x, y = coords

    chance_random = random.randint(0, 1)
    hp_random = random.randint(4, 8)

    podman_name = random.choice(["Cabbie", "Raddie", "Hempie", "Carrie", "Tomie", "Lettie", "Cottie", "Wammie", "Appie",
                                 "Orie", "Potie"])

    ai_com = ai_Chase()
    item_com = com_Item(corpse="S_PODMAN_CORPSE", item_name="Corpse of a PODMAN", use_function=consume_this, value=5,
                        item_d="a pile of healthy green vegetables, snack on this for hp")
    creature_com = com_Creature(podman_name, xp_reward=75,
                                death_function=death_monster,
                                base_chance=chance_random,
                                level=0,
                                hp=hp_random,
                                creature_d="a fragile humanoid made out of vegetables")
    podman = obj_Actor(x, y, "podman", animation_key="A_PODMAN", depth=Constants.DEPTH_CREATURES,
                       creature=creature_com, ai=ai_com, item=item_com)

    return podman

def gen_enemy_gogy(coords):
    x, y = coords

    gogy_name = random.choice(["Strech", "Pole", "Legs", "Lank", "Beanstalk", "Longs", "Speedy"])

    ai_com = ai_Flee()
    item_com = com_Item(corpse="S_GOGY_CORPSE", item_name="Corpse of a GOGY",
                        use_function=consume_this,
                        value=1,
                        item_d="you should be ashamed")
    creature_com = com_Creature(gogy_name,
                                death_function=death_monster, xp_reward=50,
                                base_atk=0,
                                base_chance=0,
                                level=0,
                                hp=5,
                                creature_d="only a monster would want to hurt this poor, sad thing")
    gogy = obj_Actor(x, y, "Gogy", animation_key="A_GOGY", depth=Constants.DEPTH_CREATURES,
                     creature=creature_com, ai=ai_com, item=item_com)

    return gogy

# TIER 2

def gen_enemy_tier_2(coords):
    random_num = random.randint(0, 100)

    if random_num <= 20:
        new_item = gen_enemy_sleech(coords)
        GAME.current_objects.append(new_item)

    elif 20 < random_num <= 30:
        new_item = gen_enemy_monstermatron(coords)
        GAME.current_objects.append(new_item)

    elif 30 < random_num <= 45:
        new_item = gen_enemy_boxlox(coords)
        GAME.current_objects.append(new_item)

    elif 45 < random_num <= 55:
        new_item = gen_enemy_greatergremlin(coords)
        GAME.current_objects.append(new_item)

    elif 55 < random_num <= 60:
        new_item = gen_enemy_jugo(coords)
        GAME.current_objects.append(new_item)

    elif 60 < random_num <= 75:
        new_item = gen_enemy_vixlax(coords)
        GAME.current_objects.append(new_item)

    elif random_num > 75:
        new_item = gen_enemy_choggus(coords)
        GAME.current_objects.append(new_item)

def gen_enemy_monstermatron(coords):
    x, y = coords

    matron_name = random.choice(["Madame monstrous", "Duchess devilish", "countess contemptible", "marquess malevolent",
                                 "viscountess villanous", "princess peccable"])

    random_hp = random.randint(70, 90)

    ai_com = ai_Spawner()

    item_com = com_Item(corpse="S_MONSTERMATRON_CORPSE", item_name="Corpse of a MONSTER MATRON",
                        use_function=consume_this,
                        value=17,
                        item_d="instead of looking at this you should be killing the minions")
    creature_com = com_Creature(matron_name,
                                death_function=death_monster, xp_reward=350,
                                level=4,
                                base_def=2,
                                hp=random_hp,
                                creature_d="an evil creature, kill it fast or it will swarm you with minions")
    monstermatron = obj_Actor(x, y, "MONSTER MATRON", animation_key="A_MONSTERMATRON", depth=Constants.DEPTH_CREATURES,
                     creature=creature_com, ai=ai_com, item=item_com)


    return monstermatron

def gen_enemy_matronminion(coords):
    x, y = coords

    minion_name = random.choice(["intern iniquitous", "apprentice atrocious", "pupil pernicious", "neophyte nefarious",
                                 "rookie rancorous", "lackey loathsome", "steward spiteful"])

    random_hp = random.randint(6, 9)
    random_chance = random.randint(2, 4)
    random_str = random.randint(14, 18)

    ai_com = ai_Chase()

    item_com = com_Item(corpse="S_MATRONMINION_CORPSE", item_name="Corpse of a MATRON MINION",
                        item_d="this guy is definetly filing a complaint to hr")
    creature_com = com_Creature(minion_name,
                                death_function=death_monster, xp_reward=5,
                                base_chance=random_chance,
                                base_str=random_str,
                                hp=random_hp,
                                creature_d="first days on the job are never easy")
    matronminion = obj_Actor(x, y, "MATRON MINION", animation_key="A_MATRONMINION", depth=Constants.DEPTH_CREATURES,
                              creature=creature_com, ai=ai_com, item=item_com)

    return matronminion

def gen_enemy_boxlox(coords):
    x, y = coords

    randomname = random.choice(["billy lightweight", "bobby liverpunch", "ben lacing", "luis bantamweight",
                                "leo breadbasket", "limmy bodypunch"])

    random_hp = random.randint(40, 50)
    random_str = random.randint(11, 13)
    random_dex = random.randint(16, 18)

    ai_com = ai_Doublehit()
    item_com = com_Item(corpse="S_BOXLOX_CORPSE", item_name="Corpse of a BOX LOX",
                        use_function=consume_this,
                        value=10,
                        item_d="the bell was a little late for this one")
    creature_com = com_Creature(randomname,
                                death_function=death_monster, xp_reward=300,
                                base_str=random_str,
                                base_dex=random_dex,
                                level=1,
                                base_def=1,
                                hp=random_hp,
                                creature_d="A powerful creature hellbent on throwing hands, attacks twice every turn")
    return_object = obj_Actor(x, y, "BOX LOX", animation_key="A_BOXLOX", depth=Constants.DEPTH_CREATURES,
                              creature=creature_com, ai=ai_com, item=item_com)

    return return_object

def gen_enemy_jugo(coords):
    x, y = coords

    randomname = random.choice(["jimmy transposition", "julie translocation", "jeff translation", "john transportation"])

    random_hp = random.randint(21, 26)
    random_str = random.randint(14, 16)

    ai_com = ai_Fleetp()
    item_com = com_Item(corpse="S_JUGO_CORPSE", item_name="Corpse of a JUGO",
                        use_function=consume_this,
                        value=6,
                        item_d="if you wait long enough he might teleport into a coffin")
    creature_com = com_Creature(randomname,
                                death_function=death_monster, xp_reward=275,
                                base_str=random_str,
                                level=1,
                                base_ac=15,
                                base_def=1,
                                hp=random_hp,
                                creature_d="A monster with an unreliable power of teleportation which it uses when cornered")
    return_object = obj_Actor(x, y, "Jugo", animation_key="A_JUGO", depth=Constants.DEPTH_CREATURES,
                              creature=creature_com, ai=ai_com, item=item_com)

    return return_object

def gen_enemy_greatergremlin(coords):
    x, y = coords

    randomname = random.choice(["fracas", "rumpus", "wrangle", "shindig", "dustup", "tussle", "scuffle"])

    random_hp = random.randint(34, 40)
    random_str = random.randint(16, 18)
    random_dex = random.randint(12, 14)

    ai_com = ai_Chase()
    item_com = com_Item(corpse="S_GREATERGREMLIN_CORPSE", item_name="Corpse of a GREATER GREMLIN",
                        use_function=get_drop,
                        value=2,
                        item_d="something shiny in this corpse")
    creature_com = com_Creature(randomname,
                                death_function=death_monster, xp_reward=325,
                                base_str=random_str,
                                base_dex=random_dex,
                                level=3,
                                hp=random_hp,
                                creature_d="bigger cousin of the gremlin, has anger management issues")
    return_object = obj_Actor(x, y, "greater gremlin", animation_key="A_GREATERGREMLIN", depth=Constants.DEPTH_CREATURES,
                              creature=creature_com, ai=ai_com, item=item_com)

    return return_object

def gen_enemy_vixlax(coords):
    x, y = coords

    randomname = random.choice(["benji yard", "scrilla scrappa", "feddie cod", "bread dough"])

    random_hp = random.randint(36, 46)
    random_str = random.randint(14, 18)
    random_dex = random.randint(15, 17)

    ai_com = ai_Ranged()
    item_com = com_Item(corpse="S_VIXLAX_CORPSE", item_name="Corpse of a VIXLAX",
                        use_function=consume_this,
                        value=14,
                        item_d="not spittin anymore")
    creature_com = com_Creature(randomname,
                                death_function=death_monster, xp_reward=350,
                                base_str=random_str,
                                base_dex=random_dex,
                                level=1,
                                hp=random_hp,
                                creature_d="this guy spits fire, and also attacks from a range")
    return_object = obj_Actor(x, y, "vixlax", animation_key="A_VIXLAX", depth=Constants.DEPTH_CREATURES,
                              creature=creature_com, ai=ai_com, item=item_com)

    return return_object

# BOSSES

def gen_enemy_choggusking(coords):
    x, y = coords

    chogking_name = random.choice(["dry heave the XVIIII", "regurgitate the XXIII", "urp the XVXVXV", "ruminate the XXXL"])

    random_hp = random.randint(70, 80)
    random_con = random.randint(14, 18)
    random_chance = random.randint(4, 5)

    ai_com = ai_Chogking()

    item_com = com_Item(corpse="S_CHOGGUSKING_CORPSE", item_name="Corpse of the choggus king", use_function=get_drop, value=32,
                        item_d="use this corpse to get a unique item!")
    creature_com = com_Creature(chogking_name,
                                death_function=death_monster, xp_reward=900,
                                base_chance=random_chance,
                                base_con=random_con,
                                level=0,
                                hp=random_hp,
                                creature_d="a lumbering beast of blubber and skin and a lot of gold")
    choggus_king = obj_Actor(x, y, "CHOGGUS KING", animation_key="A_CHOGGUSKING", depth=Constants.DEPTH_CREATURES,
                              creature=creature_com, ai=ai_com, item=item_com)

    return choggus_king

def gen_enemy_shiftingserpent(coords):
    x, y = coords

    serpent_name = random.choice(["slinky", "slider", "noodle", "pretzel"])

    random_hp = random.randint(50, 60)
    random_con = random.randint(11, 14)
    random_dex = random.randint(12, 16)
    random_chance = random.randint(1, 3)
    random_str = random.randint(12, 14)

    ai_com = ai_Shiftingserpent()

    item_com = com_Item(corpse="S_SHIFTINGSERPENT_CORPSE", item_name="Corpse of the SHIFTING SERPENT",use_function=get_drop, value=31,
                        item_d="use this corpse to get a unique item!")
    creature_com = com_Creature(serpent_name,
                                death_function=death_monster, xp_reward=900,
                                base_chance=random_chance,
                                base_con=random_con,
                                base_dex=random_dex,
                                base_str=random_str,
                                level=0,
                                hp=random_hp,
                                creature_d="a creature with the ability to teleport and uses it to escape social situations")
    serpent = obj_Actor(x, y, "SHIFTING SERPENT", animation_key="A_SHIFTINGSERPENT", depth=Constants.DEPTH_CREATURES,
                             creature=creature_com, ai=ai_com, item=item_com)

    return serpent

def gen_enemy_spacewizard(coords):
    x, y = coords

    wizard_name = random.choice(["squiggly b. chimbles", "pinglebeep r. spijjy", "shwimble dee pee",
                                 "reducius plurus magnus", "goncho b. pimbledee"])

    random_hp = random.randint(50, 60)
    random_con = random.randint(10, 14)
    random_dex = random.randint(12, 14)
    random_chance = random.randint(1, 3)
    random_str = random.randint(11, 12)

    ai_com = ai_Spacewizard()

    item_com = com_Item(corpse="S_SPACEWIZARD_CORPSE", item_name="Corpse of the SPACE WIZARD",use_function=get_drop, value=33,
                        item_d="use this corpse to get a unique item!")
    creature_com = com_Creature(wizard_name,
                                death_function=death_monster, xp_reward=900,
                                base_chance=random_chance,
                                base_con=random_con,
                                base_dex=random_dex,
                                base_str=random_str,
                                level=0,
                                hp=random_hp,
                                creature_d="the one thing worse than a real monster, a larper")
    wizard = obj_Actor(x, y, "SPACE WIZARD ", animation_key="A_SPACEWIZARD", depth=Constants.DEPTH_CREATURES,
                        creature=creature_com, ai=ai_com, item=item_com)

    return wizard

def gen_enemy_usm(coords):
    x, y = coords

    name = random.choice(["dracula sirius longhorn", "frankenstein betelgeuse mimosa", "wight proxima rodeo"])

    random_hp = random.randint(240, 260)
    random_con = random.randint(10, 14)
    random_dex = random.randint(12, 14)
    random_chance = random.randint(1, 3)
    random_str = random.randint(16, 18)

    ai_com = ai_USM()

    item_com = com_Item(corpse="S_USM_CORPSE", item_name="Corpse of the UNDEAD SPACE MINOTAUR", use_function=get_drop,
                        value=61,
                        item_d="use this corpse to get a unique item!")
    creature_com = com_Creature(name,
                                death_function=death_monster, xp_reward=900,
                                base_chance=random_chance,
                                base_con=random_con,
                                base_dex=random_dex,
                                base_str=random_str,
                                level=0,
                                hp=random_hp,
                                creature_d="the mastermind behind all of this, kill him and retrieve the corenucleus")
    return_object = obj_Actor(x, y, "Undead space minotaur ", animation_key="A_USM", depth=Constants.DEPTH_CREATURES,
                       creature=creature_com, ai=ai_com, item=item_com)

    return return_object

#   ____    _    __  __ _____
#  / ___|  / \  |  \/  | ____|
# | |  _  / _ \ | |\/| |  _|
# | |_| |/ ___ \| |  | | |___
#  \____/_/   \_\_|  |_|_____|


def game_main_loop():
    # function loops main game
    game_quit = False

    # player action definition
    player_action = "no-action"

    pygame.mixer.music.load(ASSETS.music_background)
    pygame.mixer.music.play(-1)

    while not game_quit:

        # handle player keys
        player_action = game_handle_keys()

        map_calculate_fov()

        if player_action == "QUIT":
            game_exit()

        for obj in GAME.current_objects:
            if obj.ai:
                if player_action != "no-action":
                    obj.ai.take_turn()
            if obj.exitportal:
                obj.exitportal.update()

        if (PLAYER.state == "STATUS_DEAD" or
                PLAYER.state == "STATUS_WIN"):
            game_quit = True

        # DRAW GAME
        draw_game()

        # updates display
        pygame.display.flip()

        # ticks clock
        CLOCK.tick(Constants.GAME_FPS)

    # QUITS


def game_initialize():
    # main pygame window function

    global SURFACE_MAIN, SURFACE_MAP
    global CLOCK, FOV_CALCULATE, PLAYER, ENEMY, ENEMY2, ASSETS, CAMERA, PREFERENCES

    # initialize pygame
    pygame.init()

    # applies setting so that player can hold down buttonpress to have that be recognized as many presses, e.g holding
    # movement key to move many times without having to repeatedly press the move button
    pygame.key.set_repeat(200, 50)

    # initializes preferences
    PREFERENCES = struc_Preferences()

    # sets parameters for game camera
    SURFACE_MAIN = pygame.display.set_mode((Constants.CAMERA_WIDTH,
                                            Constants.CAMERA_HEIGHT))

    # sets parameters for game map
    SURFACE_MAP = pygame.Surface((Constants.MAP_WIDTH * Constants.CELL_WIDTH,
                                  Constants.MAP_HEIGHT * Constants.CELL_HEIGHT))

    # initializes game camera
    CAMERA = obj_Camera()

    # initializes game assets
    ASSETS = struc_Assets()

    # keeps track of time and keeps animations on track
    CLOCK = pygame.time.Clock()

    pygame.display.set_caption("globin game")

    FOV_CALCULATE = True


def game_handle_keys():
    global FOV_CALCULATE
    # GET INPUT
    keys_list = pygame.key.get_pressed()
    events_list = pygame.event.get()

    # check for modkey
    MOD_KEY = (keys_list[pygame.K_RSHIFT] or keys_list[pygame.K_LSHIFT])

    # PROCESS INPUT
    for event in events_list:
        if event.type == pygame.QUIT:
            return "QUIT"

        if PLAYER.creature:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    PLAYER.creature.move(0, -1)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_DOWN:
                    PLAYER.creature.move(0, 1)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_LEFT:
                    PLAYER.creature.move(-1, 0)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_RIGHT:
                    PLAYER.creature.move(1, 0)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_KP1:
                    PLAYER.creature.move(-1, 1)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_KP2:
                    PLAYER.creature.move(0, 1)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_KP3:
                    PLAYER.creature.move(1, 1)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_KP4:
                    PLAYER.creature.move(-1, 0)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_KP5:
                    FOV_CALCULATE = True
                    return "player-waited"

                if event.key == pygame.K_KP6:
                    PLAYER.creature.move(1, 0)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_KP7:
                    PLAYER.creature.move(-1, -1)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_KP8:
                    PLAYER.creature.move(0, -1)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_KP9:
                    PLAYER.creature.move(1, -1)
                    FOV_CALCULATE = True
                    return "player-moved"

                if event.key == pygame.K_g:
                    objects_at_player = map_object_at_coords(PLAYER.x, PLAYER.y)

                    for obj in objects_at_player:
                        if obj.item:
                            obj.item.pick_up(PLAYER)

                            return "player pickup"

                if event.key == pygame.K_d:
                    if len(PLAYER.container.inventory) > 0:
                        PLAYER.container.inventory[-1].item.drop(PLAYER.x, PLAYER.y)

                if event.key == pygame.K_i:
                    menu_inventory()

                if event.key == pygame.K_l:
                    menu_look()

                if event.key == pygame.K_h:
                    menu_help()

                if event.key == pygame.K_c:
                    menu_character()

                if event.key == pygame.K_ESCAPE:
                    menu_options()

                if event.key == pygame.K_f:
                    list_of_objs = map_object_at_coords(PLAYER.x, PLAYER.y)

                    for obj in list_of_objs:
                        if obj.stairs:
                            obj.stairs.use()
                        if obj.exitportal:
                            obj.exitportal.use()

    return "no-action"


def game_message(game_msg, msg_color=Constants.COLOR_WHITE):
    GAME.message_history.append((game_msg, msg_color))


def game_new():
    global GAME

    # initializes the game object, game object tracks game progress
    GAME = obj_Game()

    # creates player and new map
    gen_player((0, 0))

    PLAYER.update_name(obj_Game.name)
    game_message("Press h for help", Constants.COLOR_GREY)

    map_place_objects(GAME.current_rooms)


def game_exit():
    game_save()

    pygame.quit()
    exit()


def game_save():
    for obj in GAME.current_objects:
        obj.animation_destroy()

    with gzip.open('data/savedata/savegame', 'wb') as file:
        pickle.dump([GAME, PLAYER], file)


def game_load():
    global GAME, PLAYER

    with gzip.open('data/savedata/savegame', 'rb') as file:
        GAME, PLAYER = pickle.load(file)

    map_make_fov(GAME.current_map)

    for obj in GAME.current_objects:
        obj.animation_init()


def preferences_save():
    with gzip.open('data\savedata\pref', 'wb') as file:
        pickle.dump(PREFERENCES, file)


def preferences_load():
    global PREFERENCES

    with gzip.open('data\savedata\pref', 'rb') as file:
        PREFERENCES = pickle.load(file)


#  ___ _   _ ___ _____
# |_ _| \ | |_ _|_   _|
#  | ||  \| || |  | |
#  | || |\  || |  | |
# |___|_| \_|___| |_|
if __name__ == '__main__':
    menu_main()
