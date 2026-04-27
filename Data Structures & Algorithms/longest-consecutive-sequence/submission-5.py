class Solution:
    def merge_n(self, n, map_end_to_start, map_start_to_end):
        # (start,n)+(n,end) -> (start, end)
        if n in map_end_to_start and n in map_start_to_end:
            start = map_end_to_start[n]
            end = map_start_to_end[n]
            del map_end_to_start[end],map_start_to_end[start]
            map_start_to_end[start] = end
            map_end_to_start[end] = start

    def longestConsecutive(self, nums: List[int]) -> int:
        map_start_to_end = {}
        map_end_to_start = {}
        for n in set(nums):
            must_add_new = True
            if n-1 in map_end_to_start:
                #(start,n-1) -> (start,n)
                start = map_end_to_start[n-1]
                del map_end_to_start[n-1]
                map_end_to_start[n] = start
                map_start_to_end[start] = n
                must_add_new = False
                self.merge_n(n, map_end_to_start, map_start_to_end)

            if n+1 in map_start_to_end:
                #(n+1,end) -> (n,end)
                end = map_start_to_end[n+1]
                del map_start_to_end[n+1]
                map_start_to_end[n] = end
                map_end_to_start[end] = n
                must_add_new = False
                self.merge_n(n, map_end_to_start, map_start_to_end)
            
            if must_add_new:
                map_start_to_end[n] = n
                map_end_to_start[n] = n

        ans = 0
        for start, end in map_start_to_end.items():
            #assert map_end_to_start[end] == start, 'маппинги разсинхронились'
            ans = max(ans, end-start+1)
        return ans
