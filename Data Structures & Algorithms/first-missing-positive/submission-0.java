class Solution {
    public int firstMissingPositive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        int smallestPos = 1;
        while (set.contains(smallestPos)) { 
            smallestPos++;
        }
        
        return smallestPos;
    }
}