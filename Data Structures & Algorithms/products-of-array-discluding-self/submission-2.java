class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        Arrays.fill(output, 1);
        for (int i = 0; i < output.length; ++i) {
            for (int j = 0; j < output.length; ++j) {
                if (i != j) {
                    output[i] *= nums[j];
                }
            }
        }
        return output;
    }
}  
