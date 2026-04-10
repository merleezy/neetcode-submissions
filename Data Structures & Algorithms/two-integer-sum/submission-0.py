class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # complement = target - num
        addends = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in addends:
                return [addends[complement], i]
            addends[num] = i
            
