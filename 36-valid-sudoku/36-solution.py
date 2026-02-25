from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list) -> bool:
        """
        Row divided by 3 tells me which horizontal band of 3×3 boxes I’m in.
        Column divided by 3 tells me which vertical band.
        Since each band has 3 boxes, I multiply the row band by 3 and add the column band to get a unique box index from 0 to 8.
        """
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                if (val in rows[r]
                    or val in cols[c]
                    or val in squares[(r // 3) * 3 + (c // 3)]
                ): return False

                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3) * 3 + (c // 3)].add(val)

        return True
        