class Solution:
    def partition(self, s: str) -> List[List[str]]:

        output = []

        def helper(index, subIndex, currList):
            if subIndex >= len(s):
                output.append(list(currList))
                return
            
            if index >= len(s):
                return
            
            substr = s[subIndex:index + 1]
            check = True
            for i in range(0, len(substr) // 2):
                if substr[i] != substr[len(substr) - 1 - i]:
                    check = False
            
            if check:
                currList.append(substr)
                helper(index + 1, index + 1, currList)
                currList.pop()
            
            helper(index + 1, subIndex, currList)

        helper(0, 0, [])
        return output