class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = "".join(sorted(s))
        t_sort = "".join(sorted(t))

        return s_sort == t_sort
