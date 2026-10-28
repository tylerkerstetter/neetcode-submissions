class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)
        returned = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = len(nums) - 1

                while l < r:
                    quadList = [nums[i], nums[j], nums[l], nums[r]]
                    quadSum = sum(quadList)

                    if quadSum == target:
                        returned.append(quadList)
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                    elif quadSum > target:
                        r -= 1
                    else:
                        l += 1

        return returned