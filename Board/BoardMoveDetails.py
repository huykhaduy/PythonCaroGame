
class BoardTurnDetails:
    def __init__(self, playerId, pos_x, pos_y):
        self.playerId = playerId
        self.position = (pos_x, pos_y)

    def show_details(self):
        print("{} has been reveal at position ({}, {})".format(self.playerId, self.position[0], self.position[1]))


