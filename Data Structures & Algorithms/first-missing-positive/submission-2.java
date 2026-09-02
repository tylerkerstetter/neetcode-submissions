class Solution {
    public int firstMissingPositive(int[] nums) {
        int arrLength = nums.length;
        for (int i = 0; i < arrLength; i++) {
            if (nums[i] < 1 || nums[i] > arrLength) {
                nums[i] = 0;
            }
            while (nums[i] != i + 1 && nums[i] >= 1 && nums[i] <= arrLength && nums[i] != nums[nums[i] - 1]) {
                int here = nums[i];
                int there = nums[nums[i] - 1];
                nums[nums[i] - 1] = here;
                nums[i] = there;

            }
        } 
        for (int j = 0; j < arrLength; j++) {
            if (nums[j] != j + 1) {
                return j + 1;
            }
        } return arrLength + 1;
    }
}