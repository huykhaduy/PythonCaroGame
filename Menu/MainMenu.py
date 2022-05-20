import pygame
import pygame_menu

from GamePlay.GameAction import GameAction
from GameSettings.DefaultSettings import *
from GameSettings import LightTheme
from GameSettings import BlackTheme
from pygame_menu import sound


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.menuTheme = pygame_menu.Theme(
            background_color=pygame_menu.baseimage.BaseImage(image_path="./Image/background.jpg"),
            title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
            widget_alignment=pygame_menu.locals.ALIGN_CENTER,
            title=False,
            widget_selection_effect=pygame_menu.widgets.LeftArrowSelection(arrow_size=(50, 50)).set_background_color(
                (0, 10, 51))
        )
        self.menu = pygame_menu.Menu(
            height=screen_height,
            theme=self.menuTheme,
            title='',
            width=screen_width,
            center_content=False,
            mouse_motion_selection=True

        )
        self.menu.add.label("Game Caro",
                            font_name=pygame_menu.font.FONT_8BIT,
                            font_color=(11, 156, 255)
                            ).translate(0, 50)

        items = [('3 x 3', 3),
                 ('10 x 10', 10),
                 ('15 x 15', 15)]
        self.selector1 = self.menu.add.selector(
            title='',
            items=items,
            selection_effect=pygame_menu.widgets.NoneSelection(),
            cursor=pygame_menu.locals.CURSOR_HAND,
            font_color=(254, 0, 143),
            font_name=pygame_menu.font.FONT_8BIT,
            font_size=20,
            style=pygame_menu.widgets.SELECTOR_STYLE_FANCY,
            style_fancy_bgcolor=pygame_menu.themes.TRANSPARENT_COLOR,
            style_fancy_bordercolor=pygame_menu.themes.TRANSPARENT_COLOR,
            style_fancy_arrow_color=(255, 255, 255),
            style_fancy_arrow_margin=(15, 15, 0)
        ).translate(0, 80)

        levels = [("Easy", 1), ("Medium", 2), ("Hard", 3)]
        self.selector2 = self.menu.add.selector(
            title='\t\tGame level:',
            items=levels,
            align=pygame_menu.locals.ALIGN_CENTER,
            selection_effect=pygame_menu.widgets.NoneSelection(),
            cursor=pygame_menu.locals.CURSOR_HAND,
            font_color=(254, 0, 143),
            font_name=pygame_menu.font.FONT_NEVIS,
            font_size=24,
            style=pygame_menu.widgets.SELECTOR_STYLE_FANCY,
            style_fancy_bgcolor=pygame_menu.themes.TRANSPARENT_COLOR,
            style_fancy_bordercolor=pygame_menu.themes.TRANSPARENT_COLOR,
            style_fancy_arrow_color=(255, 255, 255),
            # style_fancy_arrow_margin=(15, 15, 0)
        ).translate(0, 100)

        self.menu.add.label("(Game level for player vs computer only)",
                            font_name=pygame_menu.font.FONT_OPEN_SANS_ITALIC,
                            font_color=(255, 255, 255),
                            font_size=16,
                            align=pygame_menu.locals.ALIGN_CENTER
                            ).translate(0, 100)

        self.menu.add.button('PLAYER VS COMPUTER (PVC)', action=self.initPVCGame,
                             font_color=(51, 191, 251),
                             font_name=pygame_menu.font.FONT_FIRACODE_BOLD,
                             align=pygame_menu.locals.ALIGN_CENTER,
                             border_width=1,
                             font_size=24,
                             padding=(5, 30),
                             cursor=pygame_menu.locals.CURSOR_HAND,
                             border_color=(3, 160, 253),
                             background_color=(0, 14, 51),
                             ).translate(0, 150)
        self.menu.add.button('PLAYER VS PLAYER (PVP)', action=self.initPVPGame,
                                           font_color=(253, 0, 143),
                                           font_name=pygame_menu.font.FONT_FIRACODE_BOLD,
                                           align=pygame_menu.locals.ALIGN_CENTER,
                                           border_width=1,
                                           cursor=pygame_menu.locals.CURSOR_HAND,
                                           font_size=24,
                                           padding=(5, 45),
                                           border_color=(3, 160, 253),
                                           background_color=(0, 14, 51)
                                           ).translate(0, 165)

        self.menu.add.label("Settings",
                            font_name=pygame_menu.font.FONT_8BIT,
                            font_color=(255, 255, 255),
                            align=pygame_menu.locals.ALIGN_LEFT,
                            font_size=16
                            ).translate(0, 250)
        self.theme = self.menu.add.toggle_switch('Theme', False, width=100,
                                                 font_name=pygame_menu.font.FONT_NEVIS,
                                                 font_color=(255, 255, 255), padding=0,
                                                 selection_effect=pygame_menu.widgets.NoneSelection(),
                                                 align=pygame_menu.locals.ALIGN_LEFT,
                                                 font_size=16, state_text=('Light', 'Dark'),
                                                 slider_color=(48, 94, 140),
                                                 state_color=((255, 255, 255), (8, 14, 58)),
                                                 switch_margin=(20, 0),
                                                 state_text_font_color=((8, 14, 58), (255, 255, 255)),
                                                 switch_height=1.8,
                                                 switch_border_width=1,
                                                 cursor=pygame_menu.locals.CURSOR_HAND
                                                 ).translate(30, 265)
        # self.menu.add.button('QUIT GAME', action=pygame_menu.events.PYGAME_QUIT,
        #                      font_color=(255, 255, 255),
        #                      font_name=pygame_menu.font.FONT_FIRACODE_BOLD,
        #                      align=pygame_menu.locals.ALIGN_CENTER,
        #                      # border_width=1,
        #                      font_size=16,
        #                      padding=(5, 10),
        #                      cursor=pygame_menu.locals.CURSOR_HAND,
        #                      selection_effect=pygame_menu.widgets.NoneSelection(),
        #                      # border_color=(3, 160, 253),
        #                      background_color=(191, 46, 82),
        #                      ).translate(0, 160)

    def initPVPGame(self):
        boardSize = self.selector1.get_value()[0][1]
        gameTheme = LightTheme
        if self.theme.get_value():
            gameTheme = BlackTheme
        game = GameAction(self.screen, gameTheme, self.loop, boardSize)
        game.runGamePVP()

    def initPVCGame(self):
        boardSize = self.selector1.get_value()[0][1]
        aiLevel = self.selector2.get_value()[0][1]
        gameTheme = LightTheme
        if self.theme.get_value():
            gameTheme = BlackTheme
        game = GameAction(self.screen, gameTheme, self.loop, boardSize)
        game.runGameAI(aiLevel)

    def run(self):
        self.menu.mainloop(self.screen)

    def loop(self):
        self.menu.mainloop(self.screen)