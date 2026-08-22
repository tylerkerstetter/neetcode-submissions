class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []
        running_prod = 1
        for i in range(len(nums)):
            new_list.append(running_prod)
            running_prod *= nums[i]
        running_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            new_list[i] *= running_prod
            running_prod *= nums[i]
        return new_list
            