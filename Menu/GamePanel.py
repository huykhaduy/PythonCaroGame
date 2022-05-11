import pygame_menu
import pygame

from Board.BoardGUI import BoardGUI
from GameSettings import BlackTheme
from GameSettings.DefaultSettings import *


class GamePanel:
    def __init__(self, screen, theme, resetGameFunc, loop, panelSize):
        self.screen = screen
        self.theme = theme
        self.loop = loop
        pygame.draw.rect(self.screen, (70, 145, 219), pygame.Rect(600, 0, 200, 600))
        self.custom_theme_menu = pygame_menu.Theme(
            background_color=pygame_menu.themes.TRANSPARENT_COLOR,
            title=False,
            widget_font=pygame_menu.font.FONT_NEVIS,
            widget_font_color=(255, 255, 255),
            widget_margin=(0, 5),
            widget_selection_effect=pygame_menu.widgets.NoneSelection(),
            widget_font_antialias=True,
            widget_alignment=pygame_menu.locals.ALIGN_CENTER,
        )

        self.menu = pygame_menu.Menu(height=600,
                                     mouse_motion_selection=True,
                                     position=(600, 25, False),
                                     theme=self.custom_theme_menu,
                                     title='',
                                     width=200,
                                     center_content=False, )

        self.menu.add.button("    HOME   ", font_size=25, font_color=(255, 255, 255),
                             background_color=pygame_menu.baseimage.BaseImage(r"./Image/background.jpg"),
                             action=self.click
                             )
        headerText = 'GAME CARO'
        headerSize = str(panelSize)+" x "+str(panelSize)
        self.menu.add.label(headerText, font_size=20).translate(0, 40)
        self.menu.add.label(headerSize, font_size=20).translate(0, 40)
        turnOfPlayerText = "Player turn: "
        player_turn_label = self.menu.add.label(turnOfPlayerText, font_size=20,
                                                font_name=pygame_menu.font.FONT_OPEN_SANS).translate(0, 70)

        player_turn_num = ""
        self.playerId_label = self.menu.add.label(player_turn_num, font_size=20, background_color=(70, 145, 219),
                                                  font_name=pygame_menu.font.FONT_OPEN_SANS_ITALIC)
        self.playerId_label.translate(0, 170)
        winning_Text = ""
        self.winning_label = self.menu.add.label(winning_Text, font_size=20, background_color=(70, 145, 219),
                                                 font_name=pygame_menu.font.FONT_OPEN_SANS_BOLD).translate(0, 180)
        self.menu.add.button("Reset game", action=resetGameFunc, font_size=20, font_color=(70, 145, 219),
                             background_color=(255, 255, 255), padding=(5, 20)).translate(0, 210)

    def click(self):
        self.loop()

    def display(self, events, screen):
        if self.menu.is_enabled():
            self.menu.update(events)
            self.menu.draw(screen)

    def run(self, events, playerId, title):
        # while True:
        #     events = pygame.event.get()
        #     for event in events:
        #         if event.type == pygame.QUIT:
        #             exit()

        if self.menu.is_enabled():
            self.playerId_label.set_title(title)
            self.menu.draw(self.screen)
            BoardGUI.drawPlayerShape(self.screen, self.theme, playerId, 660, 255, 80)
        pygame.display.update()

    def showWinningTitle(self, title):
        self.winning_label.set_title(title)
