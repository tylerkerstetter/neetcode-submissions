class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            left_arr = nums[:len(nums) // 2] # first half CAN BE arr[0:len(arr) // 2]
            right_arr = nums[len(nums) // 2:] # last half CAN BE arr[len(arr) // 2:len(arr)]

        # recursion
            self.sortArray(left_arr)
            self.sortArray(right_arr)

         #merge
            i = 0 # left_arr idx
            j = 0 # right_arr idx
            k = 0 # merged_arr idx

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    nums[k] = left_arr[i]
                    i += 1
                else:
                    nums[k] = right_arr[j]
                    j += 1
                k += 1
        
            while i < len(left_arr):
                nums[k] = left_arr[i]
                i += 1
                k += 1
        
            while j < len(right_arr):
                nums[k] = right_arr[j]
                j += 1
                k += 1

        return nums