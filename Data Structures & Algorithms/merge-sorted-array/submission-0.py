class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # increasing order, but dupes allowed
        # m -> num of ints in nums1
        # n -> num of ints in num2
        # edit nums1

        nums1[m:] = nums2

        nums1.sort()
            

        