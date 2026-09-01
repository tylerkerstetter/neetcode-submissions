

class Solution {
    
    public int longestConsecutive(int[] nums) {

        Set<Integer> mySet = new HashSet<>();

        for (int num : nums) {
            mySet.add(num);
        }
        
        int longest = 0;

        for (int i = 0; i < nums.length; i++) {
            if (!mySet.contains(nums[i] - 1)) {
                int length = 0;
                while (mySet.contains(nums[i] + length)) {
                    length += 1;
                }
                longest = Math.max(length, longest);
            }
        }

        return longest;
    }
}
