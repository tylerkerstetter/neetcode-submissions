class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        empty_list = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hashMap:
                hashMap[sorted_word] = []
                hashMap[sorted_word].append(word)
            else:
                hashMap[sorted_word].append(word)
        for value in hashMap.values():
            empty_list.append(value)
        return empty_list