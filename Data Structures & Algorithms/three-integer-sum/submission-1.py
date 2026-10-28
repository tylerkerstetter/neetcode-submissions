class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ourMap = {}
        output = set()

        for i, num in enumerate(nums):
            ourMap[num] = i

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                target = -1 * (nums[i]) - nums[j]
                if target in ourMap:
                    if i != j and i != ourMap[target] and j != ourMap[target]:
                        triplet = tuple(sorted([nums[i], nums[j], target]))
                        output.add(triplet)
        

        return [list(triplet) for triplet in output]