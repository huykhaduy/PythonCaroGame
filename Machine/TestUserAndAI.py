from Board.BoardLogic import AdvancedBoardLogic
from AI import AI

if __name__ == "__main__":
    ai_win = 0
    user_win = 0
    ai = AI()
    total = 100
    for i in range(0, total):
        board = AdvancedBoardLogic()
        playerId = 1
        print(f"Game number: {i}")
        value = 0
        while not board.isOver():
            print(playerId)
            if playerId == ai.userPlayer:
                if board.isEmpty():
                    row, col = ai.randomLevel(board)
                    board.markSquare(playerId, row, col)
                    print(f"{playerId} has move {row},{col}")
                else:
                    row, col = ai.mostMove(board)
                    board.markSquare(playerId, row, col)
                    print(f"{playerId} has move {row},{col}")
                playerId = playerId % 2 + 1

            if playerId == ai.aiPlayer and not board.isOver():
                row, col = ai.hardLevel(board)
                board.markSquare(playerId, row, col)
                print(f"{playerId} has move {row},{col}")
                playerId = playerId % 2 + 1
            # board.markSquare(playerId, )
        winning = board.getWinningState()
        value += 1
        if winning == ai.aiPlayer:
            ai_win += 1
            print("AI win!")
        elif winning == ai.userPlayer:
            user_win += 1
            print("User win!")

    print(f"Total game: {total}")
    print(f"User agorithms has won {user_win} times")
    print(f"Minmax has won {ai_win} times")



