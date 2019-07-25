class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for all elements in the board, function recursively checks for path that produces string
        def backtrack(board, i, j, word):
            # for empty strings
            if len(word) == 0:
                return True
            # deals with edges (out of bounds)
            if i < 0 or i >= len(board):
                return False
            # deals with edges (out of bounds)
            if j < 0 or j >= len(board[i]):
                return False
            # marks if first letter of current string matches current board value replace that value with # so that
            # we indicate its been visited
            if board[i][j] == word[0]:
                board[i][j] = "#"
                # if either bottom, top, left, or right neighbors of current board value return true, go to that tile
                # persue that path, if either of those path matches the word, return True will be returned and the for
                # for loop stops and returns True (no need to pursue any other paths)
                if backtrack(board, i+1, j, word[1:]) or backtrack(board, i-1, j, word[1:]) or backtrack(board, i, j+1, word[1:]) or backtrack(board, i, j-1, word[1:]):
                    return True
                board[i][j] = word[0]
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(board, i, j, word):
                    return True
        return False
