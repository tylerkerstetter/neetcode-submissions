class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0

        for start in range(len(nums)):
            currIdx = start
            carried = nums[start]
            while count < len(nums):
                swapIdx = (currIdx + k) % len(nums)
                temp = nums[swapIdx]
                nums[swapIdx] = carried
                carried = temp
                count += 1
                currIdx = swapIdx

                if currIdx == start:
                    break

            



            


            
            
