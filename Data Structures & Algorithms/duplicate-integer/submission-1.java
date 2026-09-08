class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> checkNums = new HashSet<>();
        for (int num : nums) {
            checkNums.add(num);
        }
        if (checkNums.size() == nums.length) {
            return false;
        } else {
            return true;
        }
    }
}