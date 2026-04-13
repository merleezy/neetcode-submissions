class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            low, high = i + 1, len(numbers) - 1
            complement = target - numbers[i]

            while low <= high:
                middle = low + (high - low) // 2;

                if numbers[middle] == complement:
                    return [i + 1, middle + 1]
                elif numbers[middle] < complement:
                    low = middle + 1
                else: 
                    high = middle - 1

        return []