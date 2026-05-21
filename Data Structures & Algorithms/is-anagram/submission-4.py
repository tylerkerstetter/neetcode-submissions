class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1 = {}
        hashMap2 = {}
        for a in s:
            if a in hashMap1:
                hashMap1[a] += 1
            else:
                hashMap1[a] = 1
        for b in t:
            if b in hashMap2:
                hashMap2[b] += 1
            else:
                hashMap2[b] = 1
            
        return hashMap1 == hashMap2