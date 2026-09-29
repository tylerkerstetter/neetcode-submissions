class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int weNeed = target - nums[i];
            if (hashMap.containsKey(weNeed)) {
                return new int[] {hashMap.get(weNeed), i};
            }
            
            hashMap.put(nums[i], i);
            
        } return new int[] {};
    }
}
