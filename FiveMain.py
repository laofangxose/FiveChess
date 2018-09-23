import numpy as np


class Five:
    def __init__(self):
        # Initialization of the game on a 10*10 board
        self.size = 10
        self.board = np.zeros((self.size, self.size))
        self.masks = []

    def startGame(self):
        pass

    def play(self, player, row, col):
        if self.board[row, col] == 0:
            self.board[row, col] = player.piece
            print("current board:")
            print(self.board)
            if self.isWin(player):
                self.endGame()
        else:
            print("Invalid Move")

    def isWin(self, player):
        for mask in self.masks:
           if np.sum(self.board[mask]) == 5 * player.piece:
               print("Game over, {} wins!".format(player.name))
               return True
        return False

    def endGame(self):
        pass

class Player:
    def __init__(self, piece):
        self.piece = piece
        self.name = "White" if piece == -1 else "Black" if self.piece == 1 else "Invalid"

if __name__ == '__main__':
    print("Welcome to Five!")
    piece = int(input("Please enter your player, 1 for black, -1 for white:"))
    while piece not in [-1, 1]:
        piece = input("Invalid player, please input 1 for black, -1 for white:")
    player1 = Player(piece)
    aiPlayer = Player(-piece)
    five = Five()
    five.play(player1, 2, 3)