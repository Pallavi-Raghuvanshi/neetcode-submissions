from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                
                if num != '.':
                    # Create unique identifiers for row, column, and 3x3 box block
                    row_tag = f"row-{r}-{num}"
                    col_tag = f"col-{c}-{num}"
                    box_tag = f"box-{r // 3}-{c // 3}-{num}"
                    
                    # If any identifier already exists, it is a duplicate
                    if row_tag in seen or col_tag in seen or box_tag in seen:
                        return False
                    
                    # Store the identifiers
                    seen.add(row_tag)
                    seen.add(col_tag)
                    seen.add(box_tag)
                    
        return True