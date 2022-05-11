from Board.BoardLogic import AdvancedBoardLogic
from GameSettings.DefaultSettings import *
from GameSettings import Caro3x3Size
from GameSettings import Caro10x10Size
from GameSettings import Caro15x15Size
# from GameSettings import *
import pygame


class BoardGUI(AdvancedBoardLogic):

    def __init__(self, screen, theme, row, col):
        super().__init__(row, col)
        self.screen = screen
        # self.theme = LightTheme if isLight else BlackTheme
        self.theme = theme
        self.size = None
        if row == 3:
            self.size = Caro3x3Size
        elif row == 10:
            self.size = Caro10x10Size
        else:
            self.size = Caro15x15Size
        self.number_score_to_win = self.size.number_square_to_win

    def drawBoardGames(self):
        self.screen.fill(self.theme.background_color)
        # Draw vertical lines
        x_index = self.square_size
        for col in range(self.board_col):
            pygame.draw.line(self.screen, self.theme.line_color, (x_index, 0), (x_index, board_height), self.size.line_width)
            x_index += self.square_size
        # Draw horizontal lines
        y_index = self.square_size
        for row in range(self.board_col):
            pygame.draw.line(self.screen, self.theme.line_color, (0, y_index), (board_width, y_index), self.size.line_width)
            y_index += self.square_size

    # Override BasicBoardLogic function
    def markSquare(self, playerId, row, col):
        super().markSquare(playerId, row, col)
        self.drawPlayerMark(playerId, row, col)
        boardState = self.getWinningState()
        if boardState != 0:
            startPoint, endPoint = self._winningLine
            self.drawWinningLine(boardState, startPoint, endPoint)
        return boardState

    def drawPlayerMark(self, playerId, row, col):
        # Draw cross shape
        if playerId == cross_player:
            # Main cross line
            main_cross_start = (col * self.square_size + self.size.offset, row * self.square_size + self.size.offset)
            main_cross_end = (
                col * self.square_size + self.square_size - self.size.offset, row * self.square_size + self.square_size - self.size.offset)
            pygame.draw.line(self.screen, self.theme.cross_color, main_cross_start, main_cross_end, self.size.cross_width)
            # Extra cross line
            extra_cross_start = (col * self.square_size + self.square_size - self.size.offset, row * self.square_size + self.size.offset)
            extra_cross_end = (col * self.square_size + self.size.offset, row * self.square_size + self.square_size - self.size.offset)
            pygame.draw.line(self.screen, self.theme.cross_color, extra_cross_start, extra_cross_end, self.size.cross_width)
        # Draw circle shape
        elif playerId == circle_player:
            center = (col * self.square_size + self.square_size // 2, row * self.square_size + self.square_size // 2)
            pygame.draw.circle(self.screen, self.theme.circle_color, center, self.size.circle_radius, self.size.circle_width)

    def drawWinningLine(self, playerId, startPoint, endPoint):
        # Get line color for player 1 or player 2
        color = None
        if playerId == cross_player:
            color = self.theme.cross_color
        elif playerId == circle_player:
            color = self.theme.circle_color
        else:
            return
        # Draw lines main diagonal
        if startPoint[0] - endPoint[0] == startPoint[1] - endPoint[1]:
            start = (startPoint[1] * self.square_size + self.size.offset, startPoint[0] * self.square_size + self.size.offset)
            end = (endPoint[1] * self.square_size + self.square_size - self.size.offset,
                   endPoint[0] * self.square_size + self.square_size - self.size.offset)
            pygame.draw.line(self.screen, color, start, end, self.size.win_width)
        # Draw lines auxiliary diagonal
        elif startPoint[0] - endPoint[0] == -(startPoint[1] - endPoint[1]):
            start = (
                startPoint[1] * self.square_size + self.square_size - self.size.offset, startPoint[0] * self.square_size + self.size.offset)
            end = (endPoint[1] * self.square_size + self.size.offset, endPoint[0] * self.square_size + self.square_size - self.size.offset)
            pygame.draw.line(self.screen, color, start, end, self.size.win_width)
        # Draw line row
        elif startPoint[1] == endPoint[1]:
            start = (
                startPoint[1] * self.square_size + self.square_size // 2, startPoint[0] * self.square_size + self.size.offset)
            end = (endPoint[1] * self.square_size + self.square_size // 2,
                   endPoint[0] * self.square_size + self.square_size - self.size.offset)
            pygame.draw.line(self.screen, color, start, end, self.size.win_width)
        # Draw line column
        else:
            start = (
                startPoint[1] * self.square_size + self.size.offset, startPoint[0] * self.square_size + self.square_size // 2)
            end = (endPoint[1] * self.square_size + self.square_size - self.size.offset,
                   endPoint[0] * self.square_size + self.square_size // 2)
            pygame.draw.line(self.screen, color, start, end, self.size.win_width)

    @staticmethod
    def drawPlayerShape(screen, theme, playerId, pos_x, pos_y, default_size=20, shape_offset=20):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos_x, pos_y, default_size, default_size), default_size,
                         15)
        # Draw cross shape
        if playerId == cross_player:
            # Main cross line
            main_cross_start = (pos_x + shape_offset, pos_y + shape_offset)
            main_cross_end = (pos_x + default_size - shape_offset, pos_y + default_size - shape_offset)
            pygame.draw.line(screen, theme.cross_color, main_cross_start, main_cross_end, 8)
            # Extra cross line
            extra_cross_start = (pos_x + default_size - shape_offset, pos_y + shape_offset)
            extra_cross_end = (pos_x + shape_offset, pos_y + default_size - shape_offset)
            pygame.draw.line(screen, theme.cross_color, extra_cross_start, extra_cross_end, 8)
        # Draw circle shape
        elif playerId == circle_player:
            center = (pos_x + default_size // 2, pos_y + default_size // 2)
            pygame.draw.circle(screen, theme.circle_color, center, default_size // 3, 8)
