from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n]+=1

        a = sorted(list(freq.items()), key = lambda x: -x[1])
        return [n for n,freq in a][:k]