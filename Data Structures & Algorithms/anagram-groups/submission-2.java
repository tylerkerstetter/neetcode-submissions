class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        Map<String, List<String>> map = new HashMap<>();

        for (int i = 0; i < strs.length; i++) {

            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);

            String key = new String(chars);

            if (map.containsKey(key)) {
                List<String> temp = map.get(key);
                temp.add(strs[i]);
            }
            else {
                map.put(key, new ArrayList<>(Arrays.asList(strs[i])));
            }
        }

        return new ArrayList<>(map.values());

        }
    }