import sys

from Board.BoardGUI import *
from Board.BoardLogic import *
from Machine.AI import *
from Menu.GamePanel import GamePanel


class GameAction:
    def __init__(self, screen, theme, menu, boardSize):
        self.screen = screen
        self.theme = theme
        self.row = boardSize
        self.col = boardSize
        self.board = BoardGUI(self.screen, theme, self.row, self.col)
        self.playerTurn = 1
        self.game_mode = mode_pvp
        self.is_running = True
        self.board.drawBoardGames()
        self.menu = menu
        self.panel = GamePanel(screen, theme, self.resetGame, self.menu, boardSize)

    # Thực hiện thao tác đánh cờ
    def move(self, row, col):
        boardState = self.board.markSquare(self.playerTurn, row, col)
        if boardState != 0:
            self.panel.showWinningTitle("Player " + str(self.playerTurn) + " won !")
            self.panel.menu.draw(self.screen)
            self.is_running = False
        if self.board.isFull() and boardState == 0:
            self.is_running = False
            self.panel.showWinningTitle("Draw game !")
        self.nexTurn()

    # Chuyển đến lượt tiếp theo
    def nexTurn(self):
        self.playerTurn = self.playerTurn % 2 + 1

    # Kiểm tra game kết thúc
    def isOver(self):
        if self.board.getWinningState() != 0 or self.board.isFull():
            self.is_running = False
            return True
        return False

    # Reset game
    def resetGame(self):
        self.playerTurn = 1
        self.is_running = True
        self.board = BoardGUI(self.screen, self.theme, self.row, self.col)
        self.board.drawBoardGames()
        self.panel = GamePanel(self.screen, self.theme, self.resetGame, self.menu, self.row)
        self.panel.showWinningTitle(" " * 30)

    # Chơi với người
    def runGamePVP(self):
        while True:
            events = pygame.event.get()
            self.panel.display(events, self.screen)
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.panel.run(events, self.playerTurn, "Player " + str(self.playerTurn))
                if self.is_running and event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    row = pos[1] // self.board.square_size
                    col = pos[0] // self.board.square_size
                    if self.board.isSquareEmpty(row, col):
                        self.move(row, col)
                    pygame.display.update()
            pygame.display.update()

    # Chơi với máy
    def runGameAI(self, aiLevel=1):
        ai = AI(aiLevel)
        while True:
            events = pygame.event.get()
            self.panel.display(events, self.screen)
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.is_running and ai.userPlayer == self.playerTurn:
                    self.panel.run(events, self.playerTurn, "Player " + str(self.playerTurn))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = event.pos
                        row = pos[1] // self.board.square_size
                        col = pos[0] // self.board.square_size
                        if self.board.isSquareEmpty(row, col):
                            self.move(row, col)
                    pygame.display.update()

                if self.is_running and ai.aiPlayer == self.playerTurn:
                    self.panel.run(events, self.playerTurn, "Computer")
                    none_gui_board = AdvancedBoardLogic()
                    none_gui_board.copyBoard(self.board)
                    row, col = ai.evalMove(none_gui_board)
                    self.move(row, col)
                    pygame.display.update()
            pygame.display.update()
