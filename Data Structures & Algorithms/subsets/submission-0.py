class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return all possible subsets of nums
        # no duplicates (sets?)

        output = []

        def helper(index, currSet):
            if (index >= len(nums)): # base case
                output.append(list(currSet))
                return

            if nums[index] not in currSet:
                currSet.append(nums[index])
                helper(index + 1, currSet)
            
            currSet.remove(nums[index])
        
            helper(index + 1, currSet)

        helper(0, [])
        return output