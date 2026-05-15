class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = "" 
        
        first_word = strs[0] #bat

        for i in range(len(first_word)): #
            for word in strs[1:]: # bag
                if i >= len(word) or word[i] != first_word[i]:
                    return prefix
                
                
            prefix += first_word[i] #"" + "b"

        return prefix