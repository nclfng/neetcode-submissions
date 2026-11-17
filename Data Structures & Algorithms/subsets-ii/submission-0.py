class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # dupes exist
        # return all possible subsets

        output = []

        def helper(idx, subsets):
            if idx >= len(nums):
                output.append(list(subsets))
                return

            subsets.append(nums[idx])
            helper(idx + 1, subsets)
            subsets.pop()

            while (idx + 1 < len(nums) and nums[idx] == nums[idx + 1]):
                idx += 1
            
            helper(idx + 1, subsets)
        
        nums.sort()

        helper(0, [])
        return output