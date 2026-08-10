class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use defaultdict to avoid having to initialize a set each time
        # idea: dictionary to store row/col/square idx -> set mapping
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # iterate through board
        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue
                if (digit in rows[r]
                    or digit in cols[c]
                    or digit in squares[(r // 3, c // 3)]):
                    return False

                rows[r].add(digit)
                cols[c].add(digit)
                squares[(r // 3, c // 3)].add(digit)

        return True