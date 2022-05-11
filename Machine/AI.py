import copy
import random
from threading import Thread

import Board.BoardLogic
from Board.BoardLogic import AdvancedBoardLogic


class AI:
    def __init__(self, aiLevel=1, aiPlayer=2, userPlayer=1):
        self.aiLevel = aiLevel
        self.aiPlayer = aiPlayer
        self.userPlayer = userPlayer

    def minimax_empty_sqrs(self, board, isMaximizing, alpha, beta, depth):
        if board.isFull() or depth == 0:
            return 0, None

        if board.getWinningState() == self.userPlayer:
            return 1, None

        if board.getWinningState() == self.aiPlayer:
            return -1, None

        if isMaximizing:
            maxEval = -100
            bestMove = None
            emptySqrs = board.getEmptySquares()
            for (row, col) in emptySqrs:
                tempBoard = copy.deepcopy(board)
                tempBoard.markSquare(self.userPlayer, row, col)
                myEval = self.minimax_empty_sqrs(tempBoard, False, alpha, beta, depth)[0]
                if myEval > maxEval:
                    maxEval = myEval
                    bestMove = (row, col)
                alpha = max(alpha, myEval)
                if beta <= alpha:
                    break
            return maxEval, bestMove

        if not isMaximizing:
            minEval = 100
            bestMove = None
            emptySqrs = board.getEmptySquares()
            for (row, col) in emptySqrs:
                tempBoard = copy.deepcopy(board)
                tempBoard.markSquare(self.aiPlayer, row, col)
                myEval = self.minimax_empty_sqrs(tempBoard, True, alpha, beta, depth)[0]
                if myEval < minEval:
                    minEval = myEval
                    bestMove = (row, col)
                alpha = min(beta, myEval)
                if beta <= alpha:
                    break
            return minEval, bestMove

    def minimax(self, board: AdvancedBoardLogic, isMaximizing, depth):
        if board.isFull() or depth == 0:
            return 0, None

        if board.getWinningState() == self.userPlayer:
            return 1, None

        if board.getWinningState() == self.aiPlayer:
            return -1, None

        if isMaximizing:
            maxEval = -100
            bestMove = None
            emptySqrs = board.getEmptySquares()
            for (row, col) in emptySqrs:
                tempBoard = copy.deepcopy(board)
                tempBoard.markSquare(self.userPlayer, row, col)
                myEval = self.minimax(tempBoard, False, depth - 1)[0]
                if myEval > maxEval:
                    maxEval = myEval
                    bestMove = (row, col)
            return maxEval, bestMove

        if not isMaximizing:
            minEval = 100
            bestMove = None
            emptySqrs = board.getEmptySquares()
            for (row, col) in emptySqrs:
                tempBoard = copy.deepcopy(board)
                tempBoard.markSquare(self.aiPlayer, row, col)
                myEval = self.minimax(tempBoard, True, depth - 1)[0]
                if myEval < minEval:
                    minEval = myEval
                    bestMove = (row, col)
            return minEval, bestMove

    def evalMove(self, main_board: Board.BoardLogic.AdvancedBoardLogic):
        # print(self.aiLevel)
        print(main_board.getMostBenefitSqrs(self.aiPlayer, self.userPlayer))
        if self.aiLevel == 1:
            # print("Easy")
            return self.mostMove(main_board)
        elif self.aiLevel == 2:
            # print("Medium")
            return self.mediumLevel(main_board)
        else:
            # print("Hard")
            return self.hardLevel(main_board)

    def mostMove(self, main_board):
        return main_board.getMostBenefitSqrs(self.aiPlayer,self.userPlayer)

    def randomLevel(self, main_board):
        emptySqrs = main_board.getEmptySquares()
        move = emptySqrs[random.randint(0, len(emptySqrs) - 1)]
        return move

    def mediumLevel(self, main_board):
        if main_board.getNumberOfTurn() < 2:
            move = self.randomLevel(main_board)
        else:
            myEval, move = self.minimax(main_board, False, 1000)
        return move

    def hardLevel(self, main_board):
        myEval, move = self.minimax_empty_sqrs(main_board, False, -100, 100, 1000)
        # print(f'AI has chosen to mark the square in pos {move} with an eval of: {myEval}')
        return move



# class AIThreading(Thread):
#     def __init__(self, group=None, target=None, name=None,
#                  args=(), kwargs={}, Verbose=None):
#         Thread.__init__(self, group, target, name, args, kwargs)
#         self._return = None
#
#     def run(self):
#         # noinspection PyUnresolvedReferences
#         if self._target is not None:
#             # noinspection PyUnresolvedReferences
#             self._return = self._target(*self._args,
#                                         **self._kwargs)
#
#     def join(self, *args):
#         Thread.join(self, *args)
#         return self._return


