class Solution {
    public int[] getConcatenation(int[] nums) {
        int doubled[] = new int[nums.length * 2];
        for (int i = 0; i < nums.length * 2; i++) {
            doubled[i] = nums[i % nums.length];
        } 
        return doubled;
}
}