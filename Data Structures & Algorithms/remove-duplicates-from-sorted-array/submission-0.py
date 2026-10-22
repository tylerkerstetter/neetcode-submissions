class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        l = r = 0

        while r < length:
            nums[l] = nums[r]
            while r < length and nums[l] == nums[r]:
                r += 1
            l += 1
        return l