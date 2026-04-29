'''
1. Initialize hashmap to count frequency of nums
2. Initialize frequency array and fill with empty array slots, 
    same length as nums + 1 (including zero)
3. Fill hashmap with frequency of each num
4. For each number and its frequency, add it to freq[freq]
5. Initialize empty result array
6. Loop from largest possible frequency down to 1
    - For each num in freq[i], add to res array
    - Once length of res equals k, return it
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        res = []
        for num, cnt in count.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
