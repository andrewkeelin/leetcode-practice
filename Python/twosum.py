class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):

            if nums[i] in hash:
                indexOne = hash[nums[i]]
                indexTwo = i
                return indexOne,indexTwo
            else:
                diff = target - nums[i]
                hash[diff] = i