class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()

        def helper(row, col, index):
            if index >= len(word):
                return True

            if not (row >= 0 and row < len(board) and col >= 0 and col < len(board[0])):
                return
            
            if (row, col) in visited or board[row][col] != word[index]:
                return
            
            visited.add((row, col))
            result = helper(row + 1, col, index + 1) or helper(row - 1, col, index + 1) or helper(row, col + 1, index + 1) or helper(row, col - 1, index + 1)
            visited.remove((row, col))

            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                result = helper(i, j, 0)
                if result: return True

        return False