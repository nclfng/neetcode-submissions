class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # return all strings u can generate w n pairs
        # add close or dont add close

        output = []

        def helper(opened, closed, currStr):
            nonlocal output

            if opened >= n and closed >= n:
                output.append(currStr)
                return

            if opened < n:
                helper(opened + 1, closed, currStr + "(")
            
            if closed < opened:
                helper(opened, closed + 1, currStr + ")")
        
        helper(0, 0, "")
        return output