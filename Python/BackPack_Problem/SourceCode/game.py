class GameController:

    def __init__(self, board):
        self.board = board

    def findAvailablePosition(self, board, startingPosition, isDebug=False):
        """ This functions finds the first available position.
        It will return a tuple with the position with the first '0' found.
        The tuple will help to use the position in the matrix (or board) matrix[i][j]"""

        rowIndex = startingPosition[0]
        colIndex = startingPosition[1]

        # The Debug parameter help the developer to print values when needed.
        # To use the print in the function call pass the parameter isDebug = "True"
        if isDebug:
            print(f"Starting position {startingPosition}")

        # From the starting position checks a "0" value, from left to right and bottom to top.
        while rowIndex > 0:
            while colIndex < len(board[rowIndex]):
                if board[rowIndex][colIndex] == 0:
                    return (rowIndex, colIndex)
                else:
                    colIndex += 1
            colIndex = 0
            rowIndex -= 1

        return None

    def checkPieceFits(self, board, piece, position):
        """ This function will verify if the selected piece can fit inside the board.
         Also, it will check if the piece don't go over the boundaries of the board.
         The function will return a boolean flag helping the function addPieceToBoard to add the piece."""

        if position is None:
            return False

        rowStep = 0
        row = len(piece) - 1
        col = 0

        while row >= 0:
            while col < len(piece[row]):
                if piece[row][col] != 0:

                    # If the next position is more than the board boundaries means it doesn't fit
                    if (position[1] + col >= len(board[position[0] - rowStep]) or (position[0] - rowStep) < 0):
                        return False

                    # If the next position is different that "0" it means it doesn't fit
                    if board[position[0] - rowStep][position[1] + col] != 0:
                        return False
                col += 1
            col = 0
            row -= 1
            rowStep += 1

        return True

    def addPieceToBoard(self, board, piece, startingPosition=(0, 0), isDebug=False):
        """ With the first available position and with the flag that the piece fits on the board
         the piece will be drawn on the board."""

        # Assign the tuple with the first "0" available position
        position = self.findAvailablePosition(board, startingPosition, isDebug)

        # Check if there is no available position
        if position is None:
            print("Piece doesn't fit in the board")
            return False

        # If the checkPieceFits returns "True"
        if self.checkPieceFits(board, piece, position):
            rowStep = 0
            drawRowIndex = len(piece) - 1
            drawColIndex = 0

            # The Debug parameter help the developer to print values when needed.
            # To use the print in the function call pass the parameter isDebug = "True"
            if isDebug:
                print(f"Last available position={position}")

            # Draw the piece inside the board.
            while drawRowIndex >= 0:
                while drawColIndex < len(piece[drawRowIndex]):
                    if piece[drawRowIndex][drawColIndex] != 0:
                        board[position[0] - rowStep][position[1] + drawColIndex] = piece[drawRowIndex][drawColIndex]
                    drawColIndex += 1
                rowStep += 1
                drawRowIndex -= 1
                drawColIndex = 0
            return True
        else:
            # Verify that the scan has reach the end of the board.
            if startingPosition[0] == 0 and startingPosition[1] == ((len(board[0]) - 1)):
                return False
            else:
                newPosition = ()
                # Check if there is still columns to check in the row and increase the columns in position
                if position[1] < len(board[0]):
                    newPosition = (position[0], position[1] + 1)

                # If not decrease the rows and the columns back to 0 position
                else:
                    newPosition = (position[0] - 1, 0)
                # Recursion to start the whole process again with the new position.
                return self.addPieceToBoard(board, piece, newPosition, isDebug)
        return False