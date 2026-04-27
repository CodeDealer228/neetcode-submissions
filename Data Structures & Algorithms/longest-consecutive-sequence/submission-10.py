# gpt решение
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        visited = set()        # отмечаем, что уже «в интервале»
        ans = 0

        for n in num_set:
            if n in visited:
                continue
            # найти левый конец
            start = n
            while start - 1 in num_set:
                start -= 1
            # расширяться вправо
            end = n
            while end + 1 in num_set:
                end += 1
            # пометить весь [start, end] как посещённый
            for x in range(start, end + 1):
                visited.add(x)

            ans = max(ans, end - start + 1)

        return ans