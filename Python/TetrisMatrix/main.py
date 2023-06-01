# Import modules and the pieces from the pieces.py
from pieces import PIECES_DICT
from board import BoardTable
from game import GameController

def drawBoard(board):
    """ This function is to show in the console
     the matrix M x N and the actual values that the matrix have.
     The first matrix is assigned with '0' this means that is
     without any piece."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()
    print("====================")


# GameController
# Asking the user to create the matrix (or the board) M x N
rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))

# Creates the Board with the size previously captured.
board = BoardTable(rows, columns).createBoard()
drawBoard(board)

playingGame = GameController(board)
keepPlaying = True

while keepPlaying:
    print("****")
    newPiece = int(input("Choose a piece (number 1-10):"))
    while newPiece < 1 or newPiece > 10:
        newPiece = int(input("Please, choose a piece (number 1-10):"))

    print(f"The piece selected was #{newPiece}")
    piece = PIECES_DICT[str(newPiece)]
    playingGame.addPieceToBoard(board, piece, (len(board) - 1, 0))
    drawBoard(board)
    keepPlaying = input("Continue adding pieces? (y/n): ")
    if keepPlaying == "n":
        keepPlaying = False
        print("Goodbye!")
