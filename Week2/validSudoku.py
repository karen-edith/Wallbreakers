from collections import Counter
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # set up columns to for validity checks
        row, column, square = {}, {}, {}
        # set up helper Arrays
        rowHelperArray, colHelperArray, squareHelperArray = [], [], []

        # count numbers in row and column
        for i in range(len(board)):
            for j in range (len(board)):
                if board[i][j] != '.':
                     rowHelperArray.append(board[i][j])
                if board[j][i] != '.':
                    colHelperArray.append(board[j][i])
            column[str(i)], row[str(i)] = Counter(colHelperArray), Counter(rowHelperArray)
            rowHelperArray, colHelperArray = [], []

        # count numbers in 3x3 square
        for k in range(9):
            if k % 3 == 0:
                for l in range(9):
                    if (board[k + 0][l] != '.'):
                        squareHelperArray.append(board[k + 0][l])
                    if (board[k + 1][l] != '.'):
                        squareHelperArray.append(board[k + 1][l])
                    if (board[k + 2][l] != '.'):
                        squareHelperArray.append(board[k + 2][l])
                    if (l == 2 or l == 5 or l == 8):
                        square[str(int(k + ((l+1)/3) - 1))] = Counter(squareHelperArray)
                        squareHelperArray = []
        # divide the sum of counter dictionary by length of counter dicitionary to determine
        # if each requirement is met
        for c in range(9):
            rowCounterSum, rowCounterLength  = sum(row[str(c)].values()), len(row[str(c)].values())
            columnCounterSum, columnCounterLength = sum(column[str(c)].values()), len(column[str(c)].values())
            squareCounterSum, squareCounterLength = sum(square[str(c)].values()), len(square[str(c)].values())

            if (rowCounterLength != 0 and (rowCounterSum/rowCounterLength != 1)):
                return False
            if (columnCounterLength != 0 and (columnCounterSum/columnCounterLength != 1)):
                return False
            if (squareCounterLength != 0 and (squareCounterSum/squareCounterLength != 1)):
                return False
            elif (c == 8):
                return True
