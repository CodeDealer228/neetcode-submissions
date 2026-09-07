class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while (numbers[l] + numbers[r]) != target:
            if (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                r -= 1
        return [l + 1, r + 1]
        
"""
[-5, -1, 1,3,4,5], 3
      l      r
"""