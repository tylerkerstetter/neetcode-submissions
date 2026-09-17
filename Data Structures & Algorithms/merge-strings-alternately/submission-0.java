class Solution {
    public String mergeAlternately(String word1, String word2) {
        int lengthOne = word1.length();
        int lengthTwo = word2.length();
        int min = Math.min(lengthOne, lengthTwo);

        String s = "";

        for (int i = 0; i < min; i++) {
            s += "" + word1.charAt(i) + word2.charAt(i);
        }

        if (lengthOne > min) {
            s += word1.substring(min);
        } else if (lengthTwo > min) {
            s += word2.substring(min);
        }

        return s;
    }
}