class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += (str(len(string)) + "#" + string)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            result.append(word)
            i = j + 1 + length
        return result
                


    # check if '#'
    # if '#' look at character before, tells how long string was
    # check i - 1 index, loop through that many next characters, add to
    # list
            
