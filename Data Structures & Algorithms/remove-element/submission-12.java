class Solution {
    public int removeElement(int[] nums, int val) {
        int open = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[open] = nums[i];
                open += 1; }
    } return open;
    }
}