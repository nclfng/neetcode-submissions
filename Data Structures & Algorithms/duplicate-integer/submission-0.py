class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkNums = set(nums)
        if len(nums) == len(checkNums):
            return False
        else:
            return True