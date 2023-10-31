class BoardTable:

    def __init__(self, input_rows, input_columns):
        self.rows = input_rows
        self.columns = input_columns

    def createBoard(self):
        """Create a Matrix Rows x Columns and assign a '0' value by default"""

        boardMatrix = [[0 for x in range(self.columns)] for y in range(self.rows)]
        return boardMatrix

