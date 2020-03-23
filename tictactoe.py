import random

class TicTacToe:

    
    
    def changePlayer(player):
    """Returns the opposite player given any player"""
    if player == "X":
        return "O"
    else:
        return "X"
    
    
    def __init__(self):
        """Initialize with empty board"""
        self.board = [" ", " ", " ", 
                      " ", " ", " ", 
                      " ", " ", " "]

    def show(self):
        """Format and print board"""
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def availableMoves(self):
        """Return empty spaces on the board"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def getMoves(self, player):
        """Get all moves made by a given player"""
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def checkWin(self):
        """Return the player that wins the game"""
        combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMoves(player)
            for combo in combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def gameOver(self):
        """Return True if X wins, O wins, or draw, else return False"""
        if self.checkWin() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

if __name__ == '__main__':
    game = TicTacToe()
    game.show()
