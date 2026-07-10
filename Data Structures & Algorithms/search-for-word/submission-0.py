class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def backtrack(currentWord, row, col):
            if currentWord == word:
                return True

            visited[row][col] = 1

            validPaths = [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1)
            ]

            for newRow, newCol in validPaths:
                if (
                    0 <= newRow < rows
                    and 0 <= newCol < cols
                    and visited[newRow][newCol] == 0
                ):
                    currentWord += board[newRow][newCol]

                    if backtrack(currentWord, newRow, newCol):
                        return True

                    currentWord = currentWord[:-1]

            visited[row][col] = 0
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(board[i][j], i, j):
                    return True

        return False