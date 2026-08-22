class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returned_list = []
        initial_product = 1
        for i in range(len(nums)):
            returned_list.append(initial_product)
            initial_product *= nums[i]
        initial_product = 1
        for i in range( (len(nums) - 1) , -1 , -1 ):
            returned_list[i] *= initial_product
            initial_product *= nums[i]
        return returned_list