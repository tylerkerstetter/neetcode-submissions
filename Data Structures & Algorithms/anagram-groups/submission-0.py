class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        empty_list = []
        for word in strs:
            key = "".join(sorted(word))
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(word)
        for lst in hashMap:
            empty_list.append(hashMap[lst])
        return empty_list
                
        