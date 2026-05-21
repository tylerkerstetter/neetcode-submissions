class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in hashMap:
                return [hashMap[need], i]
            
            hashMap[num] = i