class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        result = []

        for i in range(k):
            most_frequent = max(hashMap, key=hashMap.get)
            result.append(most_frequent)
            del hashMap[most_frequent]

        return result