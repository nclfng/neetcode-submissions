class Solution {
    public int[] twoSum(int[] nums, int target) {
        int lennums = nums.length;
        for (int i = 0; i < lennums; ++i) {
            for (int j = 0; j < lennums; ++j) {
                if (i == j) {
                    continue;
                }

                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{0};
    }
}
