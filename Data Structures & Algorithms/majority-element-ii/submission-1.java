class Solution {
    public List<Integer> majorityElement(int[] nums) {      
        Map<Integer, Integer> myDict = new HashMap<>();
        List<Integer> myList = new ArrayList<>();
        int myLength = nums.length;
        for (int i = 0; i < nums.length; i++) {
            Integer count = myDict.get(nums[i]);
            if (count != null) {
                myDict.put(nums[i], count + 1);
            } else {
                myDict.put(nums[i], 1);
            }
        }
        for (Integer num : myDict.keySet()) {
            if (myDict.get(num) > myLength / 3) {
                myList.add(num);
            }
        } return myList;
    }
}