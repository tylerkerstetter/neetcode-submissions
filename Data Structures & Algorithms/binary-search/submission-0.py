class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums: 
            return -1
            
        middleIdx = len(nums) // 2

        if nums[middleIdx] == target: 
            return middleIdx 
        elif nums[middleIdx] > target: 
            return self.search(nums[:middleIdx], target) 
        else: 
            result = self.search(nums[middleIdx + 1:], target)
            return middleIdx + 1 + result if result != -1 else -1