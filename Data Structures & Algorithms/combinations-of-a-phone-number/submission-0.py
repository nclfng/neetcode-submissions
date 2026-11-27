class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # all possible letter combs dig could represent
        output = []
        chars = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        def helper(index, currStr):
            if index >= len(digits):
                if len(currStr) == 0:
                    return
                output.append(currStr)
                return
            
            val = int(digits[index])
            
            for i in range(len(chars[val])):
                helper(index + 1, currStr + chars[val][i])

        
        helper(0, "")
        return output