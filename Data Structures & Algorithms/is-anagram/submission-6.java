class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (sMap.containsKey(s.charAt(i))) {
                sMap.put(s.charAt(i), sMap.get(s.charAt(i)) + 1);
            } else {sMap.put(s.charAt(i), 1);
            }
        }

        for (int j = 0; j < s.length(); j++) {
            if (tMap.containsKey(t.charAt(j))) {
                tMap.put(t.charAt(j), tMap.get(t.charAt(j)) + 1);
            } else {tMap.put(t.charAt(j), 1);
            }
        }  

        return sMap.equals(tMap);

    }
}
