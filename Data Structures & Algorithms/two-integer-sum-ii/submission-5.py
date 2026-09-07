class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)
        s = (numbers[l - 1] + numbers[r - 1])
        while s != target:
            if (numbers[l - 1] + numbers[r - 1]) < target:
                l += 1
            else:
                r -= 1
            s = (numbers[l - 1] + numbers[r - 1])
        return [l, r]
        
"""
[-5, -1, 1,3,4,5], 3
      l      r
"""