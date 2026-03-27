class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        buckets = [[] for i in range(len(nums) + 1 )]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, count in freq.items():
            buckets[count].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                if len(ans) < k:
                    ans.append(num)
        
        return ans
        