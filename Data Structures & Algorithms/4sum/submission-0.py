class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)

        quadSet = set()

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                l = j + 1
                r = len(nums) - 1

                while l < r:
                    quadSum = nums[i] + nums[j] + nums[l] + nums[r] #
                    quadList = [nums[i], nums[j], nums[l], nums[r]] #
                    if quadSum == target: #
                        if tuple(sorted(quadList)) not in quadSet: #
                            quadSet.add(tuple(sorted(quadList))) #
                    if quadSum > target:
                        r -= 1
                    else:
                        l += 1

        return [list(quad) for quad in quadSet]
