import pygame
from GameSettings.DefaultSettings import *
from Menu.MainMenu import Menu

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Trò chơi cờ caro')

# menu = pygame_menu.Menu('Welcome', 600, 600,
#                        theme=pygame_menu.themes.THEME_BLUE)
#
# menu.add.text_input('Name :', default='John Doe')
# menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)])
# menu.add.button('Play', None)
# menu.add.button('Quit', pygame_menu.events.EXIT)
# menu.mainloop(screen)

if __name__ == "__main__":
    # gl = GameAction(screen, BlackTheme)
    # pygame.draw.rect(screen, (70, 145, 219), pygame.Rect(600, 0, 200, 600))
    # menu = pygame_menu.Menu('Welcome', 400, 300)
    # menu.add.text_input('Name :', default='John Doe')
    # panel = GamePanel(screen)
    # panel.run()

    # pygame.display.flip()
    # gl.runGamePVP()
    menu = Menu(screen)
    menu.loop()

