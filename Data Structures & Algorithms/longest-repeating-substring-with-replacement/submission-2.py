class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        for char in set(s):
            replaces = 0
            cur_len = 0
            l = 0
            for r in range(n):
                cur_len+=1
                if s[r] != char:
                    replaces+=1
                while replaces > k:
                    if s[l] != char:
                        replaces-=1 
                    l+=1
                    cur_len-=1
                ans = max(ans, cur_len)
        return ans