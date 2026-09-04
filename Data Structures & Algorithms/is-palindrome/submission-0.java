class Solution {
    public boolean isPalindrome(String s) {
        String newS = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int left = 0;
        int right = newS.length() - 1;
        while (left < right) {
            if (newS.charAt(left) != newS.charAt(right)) {
                return false;
            } 
            left++;
            right--; 
        }

        return true;
    }
}
