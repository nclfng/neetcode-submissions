class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # unique combinations of nums, chosen nums sum = target
        # if bigger than target, reject path

        output = []

        def helper(index, currList):
            # base case
            if sum(currList) == target:
                output.append(list(currList))
                return
            
            if sum(currList) > target or index >= len(nums):
                return
            
            currList.append(nums[index])

            helper(index, currList)

            currList.pop()
            helper(index + 1, currList)

        helper(0, [])
        return output