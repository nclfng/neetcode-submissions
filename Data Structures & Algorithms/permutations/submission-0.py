class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return all possible permutations
        # any order can return

        output = []

        def helper(currList):
            # base case
            if len(currList) >= len(nums):
                output.append(list(currList))
                return
            
            for num in nums:
                if num in currList:
                    continue
                else:
                    currList.append(num)
                    helper(currList)
                    currList.remove(num)

        helper([])
        return output